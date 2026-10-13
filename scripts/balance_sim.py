#!/usr/bin/env python3
"""Monte Carlo balance simulator for High-Performance Team (rulebook v0.33).

Focus areas:
  1. WORK COST     - is 18 Work deliverable in 8 weeks (week 8 is the deadline week), and when does it land?
  2. ADAPTABILITY  - token income vs. Event cost, Habits, Hero, Team Reflexivity wells
  3. MOTIVATION    - the grind, Celebrate, Needs, Legs tendencies, quits

Standard library only. Run from anywhere:
    python balance_sim.py                       (3 strategies x 2000 games)
    python balance_sim.py --runs 5000 --players 5
    python balance_sim.py --set pool_start=2    (override a rule, see class Rules)
    python balance_sim.py --sweep pool_start=2,3,4 --strategies balanced
    python balance_sim.py --strategies optimal   (searches for the best policy, then plots it)
    python balance_sim.py --set weeks=7          (the printed rulebook length; any number works)
    python balance_sim.py --json out.json
    python balance_sim.py --csv results.csv     (default: balance_sim_results.csv next to this file,
                                                 plus balance_sim_results_summary.csv)

THIS IS A MODEL, NOT THE GAME. Every number it prints is only as good as the rules it encodes
and the player policies in STRATEGIES. Read the ASSUMPTIONS block below before trusting a result,
and change a policy or a rule rather than arguing with the output.

ASSUMPTIONS (places where the rulebook is silent or ambiguous; each is a switch or a constant):
  - Capital for a banked feature goes to one nominated character (the lowest-Capital one).
  - Standing is live (it tracks the highest Capital). Rules.standing_live = False freezes it.
  - A Capability +1 is paid only when a Zone tile is first put down, not when it flips.
  - Legs strengths and tendencies are read once a week at step 7, from week 2.
  - Bookish / Hands-On Base effects apply to the character who learns / teaches.
  - The adapt policy cancels an Event if severity / cost >= Strategy.adapt_threshold. Severity
    values in EVENTS are rough guesses in "days of damage"; tune them first.
  - Onboarding is modelled as one day, one a week; the replacement joins at once with no penalty.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import io
import json
import math
import os
import random
import shutil
import statistics
import sys
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field, fields, replace
from itertools import combinations

# --------------------------------------------------------------------------------------
# Rules (every constant the rulebook states; override with --set name=value)
# --------------------------------------------------------------------------------------


@dataclass
class Rules:
    weeks: int = 8                              # 7 working weeks + the deadline week
    days: int = 5
    players: int = 5
    mot_start: int = 5
    mot_cap: int = 5
    sheltered_cap: int = 3
    grind: int = 1
    celebrate: int = 1
    celebrate_banked: int = 1                   # was 2; equal to celebrate = no timing bonus (slight nerf)
    need_bonus: int = 1
    quality_penalty: int = 3
    ledger_start: int = 1
    ledger_max: int = 5
    habit_at: int = 4
    legs_strength_at: int = 3                   # a Legs strength pays +1 Motivation at this track value or more (was 4)
    speakup_strength: int = 2                   # ... except Speak Up, which pays this much
    engage_low_weeks: tuple = (5, 6)            # Engage loses 1 Motivation in these weeks (+1 in weeks 2 to 3, nothing otherwise)
    speakup_gift: bool = True                   # Speak Up no longer reads Standing; once a game its holder gives any teammate +1 Motivation
    ownit_trust: bool = True                    # Own It: pays no strength; takes the blame for a landed Event (-own_cost Motivation, team +1 Trust); keeps -1 Motivation at Trust 1 or less
    own_min_mot: int = 3                        # sim policy only: the character taking the blame has at least this much Motivation
    own_cost: int = 1
    gift_trust_min: int = 3                     # the gift needs Trust at least this high (Trust over 2); speaking up needs safety
    gift_receiver_max: int = 2                  # policy: give to the lowest teammate once someone is on this much or less (or about to quit, or in the last week)
    gift_from_week: int = 1
    base_like: int = 2                          # Bookish learning / Hands-On teaching: +this Motivation (was 1)
    base_dislike: int = 1                       # Bookish teaching / Hands-On learning: -this Motivation
    habit_discount: int = 1
    habit_min_cost: int = 0
    early_discount: int = 1                     # The Audit / Everyone Is Equal: this much cheaper while the plinth is nearly empty
    early_max_features: int = 1                 # "nearly empty" = this many banked features or fewer
    trust_cancel: bool = False                  # Trust 4+ cancelling one Event a week: removed from the game
    trust_cancel_at: int = 4                    # only read when trust_cancel is on
    reflect_mot: int = 1                        # a Reflect with evidence lifts every character at or below celebrate_max_mot by this
    low_band: int = 1
    plan_dead_at: int = 1                       # Plan does nothing when Shared Practice is at or below this (the low band: nothing in week 1)
    demo_from_week: int = 2                     # first week the Demo card can be laid
    need_from_week: int = 1                     # first week a character's Need is read at the close
    plan_from_week: int = 1                     # first week the Plan card can be laid
    cards_from_week: int = 2                    # first week Learn, Teach and Reflect can be laid
    quality_demo: bool = False                  # a Demo also meets the Quality Need (off: only Work meets it)
    cap_first_len: int = 5                      # tiles in a row or column that pay the FIRST Capability gain (later lines need 5)
    cap_per_tiles: int = 0                      # 0 = off; else every Nth tile on the Zone pays Capability +1
    cross_rows: int = 2                         # a character's first square in this many rows pays the TEAM Capability +1 (once each); no Capital
    cap_bonus_at: int = 4
    sp_bonus_at: int = 4
    reflect_trust: int = 3
    plan_bonus: int = 1
    pool_start: int = 1                         # was 3: a thin pool forces an early Workshop
    av_categories: str = "MC"                   # Authorized Voice cancels only Events of these categories (M anagement, C ustomer, P eople, E nvironment; empty = any)
    pool_cap: int = 6
    tr_wells: int = 3
    hero_min_mot: int = 3
    hero_from_week: int = 3
    hero_capital: int = 2
    events_per_week: int = 2
    events_from_week: int = 2
    date_moves_from_week: int = 3               # THE DATE MOVES UP is put back and redrawn before this week (nobody can say no yet)
    dependable_cost: int = 2                    # Take One For The Team (Dependable only): Motivation paid for +1 Trust and +1 Capital
    combos_from_week: int = 1
    threshold_base: int = 75                    # lower line: 75 + 5 x 5 players = 100 (set by hand; random play is no longer a reference)
    threshold_high_base: int = 125              # upper line: 125 + 5 x 5 players = 150
    threshold_per_player: int = 5
    habit_score: int = 12                       # Team Score per Habit held at the end (5 Habits = up to 60)
    feature_value: int = 12
    quit_penalty: int = 40
    quit_mot_cost: int = 1                      # every remaining character loses this much Motivation for each character who quits
    flex_penalty: int = 2
    low_track_penalty: int = 5                  # Team Score lost per Ledger track that finishes at 0-1
    capital_cap: int = 5
    legs_tendencies: bool = True
    autonomy_max_landed: int = 1                # Autonomy Need holds if at most this many Events landed (printed rule)
    autonomy_rule: str = "events"               # events (count landed Events) | management (no Management Event landed)
    align_tokens: int = 3                       # WORKSHOP (the merged meeting): tokens it adds (0 = card not in the game)
    workshop_from_week: int = 1                 # first week the Workshop card is open
    align_cost: int = 1                         # Motivation every character pays (one way: Motivation -> Adaptability)
    align_min_mot: int = 3                      # policy: nobody pays below this (pay 1, then the grind takes 1: at 2 that is a quit)
    celebrate_repeat: int = 1                   # Celebrate gives this much less if the team celebrated last week (1 = nothing)
    celebrate_max_mot: int = 3                  # Celebrate only lifts a character at or below this Motivation (5 = everyone, off)
    celebrate_needs_reason: bool = True         # Celebrate gives nothing unless a feature was banked this week or every Event was cancelled
    stand: bool = False                         # Torso Stand: once per game, pay Motivation to cancel your Torso's category
    stand_cost: int = 2
    habit_cancel: bool = False                  # a held Habit cancels one Event of its category a week, free
    standing_live: bool = True


# --------------------------------------------------------------------------------------
# Static game data
# --------------------------------------------------------------------------------------

TORSOS = ["Autonomy", "Hierarchy", "Community", "Quality", "Recognition"]
NEED_SOFT_LO, NEED_SOFT_HI = 75.0, 95.0   # soft goal: each Need is met in this share of character-weeks
NEED_HABIT = {"Autonomy", "Hierarchy", "Community"}   # a Habit meets these Needs outright, so they may reach 100%
NEED_NO_GOAL = {"Quality"}                # Needs with no met-rate goal: still reported, never scored
ONBOARDING_MAX = 0.15                      # goal in optimal play: Onboarding plays a game (about three quits in four are replaced)
UPPER_GOAL = 80.0                          # goal: this share of optimal games reach the upper threshold
HAND_ZERO_MIN = 1.0                        # goal: balanced and invested end on 0 points in more than this share of games (they can fail)
OPT_ZERO_MAX = 2.0                         # goal: optimal ends on 0 points in at most this share of games
QUIT_WEIGHT = 1000.0                       # optimiser priority 1: no quits. A quit outweighs finishing, which outweighs points
FINISH_WEIGHT = 9.0                        # optimiser priority 2: objective points per percent of games that deliver every feature (max 900, below one quit)
QUIT_RATE_HARD = 5.0                       # hard goal in optimal play: at most this many quits per 100 character-weeks
QUIT_RATE_SOFT_MIN = 0.25                  # soft goal in optimal play: every habitus card sees at least this many quits per 100 character-weeks
HUMAN_KIND = {"torso": "values", "legs": "instinct", "base": "upbringing"}
CARD_MISSING_MAX = 1                       # goal a: in a game at most this many action cards go unplayed
CARD_MISSING_SHARE = 95.0                  # goal a: this share of games (percent) must meet CARD_MISSING_MAX
CARD_SHARE_MIN = 50.0                      # goal b: every action card is played in more than this share of games
PLAY_RANGES = {"Plan": (1.0, 2.5), "Workshop": (1.0, 2.5)}   # goal: plays a game for each of these cards
LEGS = ["OwnIt", "Analyze", "Support", "Engage", "SpeakUp"]
BASES = ["Bookish", "HandsOn", "Sheltered", "Dependable", "Competitive"]

# feature: (work cost, complexity, depends on)
FEATURES = {
    "A": (3, "L", None),
    "B": (3, "M", None),
    "C": (3, "M", None),
    "D": (4, "H", "B"),
    "E": (2, "L", None),
    "F": (3, "H", "C"),
}

CAT_HIT = {"M": "Autonomy", "E": "Hierarchy", "P": "Community", "C": "Quality"}
CAT_IMMUNE = {"M": "Hierarchy", "E": "Autonomy", "P": "Quality", "C": "Community"}
CAT_HABIT = {"P": "PS", "E": "WKW", "M": "SR", "C": "TR"}
TORSO_CAT = {"Autonomy": "M", "Hierarchy": "E", "Community": "P", "Quality": "C"}
HABIT_TORSO = {"SR": "Autonomy", "WKW": "Hierarchy", "PS": "Community"}


@dataclass(frozen=True)
class Ev:
    name: str
    cat: str                 # M anagement, C ustomer, P eople, E nvironment
    cost: int | None         # None = cannot be cancelled
    hero: str | None         # Legs that can cancel it
    everyone: int = 0        # Motivation every character loses
    hit: str | None = None   # Torso override (replaces the category's Torso, no immunity)
    torso: bool = True       # False = no Torso reaction line on the card
    sev: float = 1.0         # rough damage in "days"; used only by the adapt policy
    early: bool = False      # costs R.early_discount less while the plinth holds R.early_max_features or fewer
    say_no: bool = False     # only a Hero or Authorized Voice cancels it: tokens, Habits and Trust cannot buy it off


EVENTS = [
    Ev("STATUS MEETING", "M", 3, "OwnIt", sev=1.0),
    Ev("BUDGET CUT", "M", 2, "OwnIt", everyone=1, sev=0.6),
    Ev("REORGANISED", "M", 2, "Engage", sev=1.0),
    Ev("THE AUDIT", "M", 2, None, everyone=1, sev=1.0, early=True),
    Ev("THE BIKESHED", "M", 1, "OwnIt", hit="Quality", sev=0.7),
    Ev("LEADS FROM BEHIND", "M", 1, "SpeakUp", everyone=1, torso=False, sev=0.5),
    Ev("EVERYONE IS EQUAL", "M", 2, None, everyone=1, sev=0.8, early=True),
    Ev("THE WOLF", "M", None, None, torso=False, sev=3.0),
    Ev("REQUIREMENTS CHANGE", "C", 2, "OwnIt", sev=1.0),
    Ev("NEGATIVE FEEDBACK", "C", 3, "Analyze", sev=2.0),
    Ev("SCOPE CREEP", "C", 3, "Analyze", sev=2.0),
    Ev("PRIORITY CHANGES", "C", 2, "Analyze", sev=1.0),
    Ev("THE DATE MOVES UP", "C", 3, "SpeakUp", sev=3.0, say_no=True),
    Ev("THE DASHBOARD", "C", 3, "Analyze", sev=2.5),
    Ev("ALWAYS REACTING", "C", 1, "SpeakUp", sev=0.7),
    Ev("KNOWLEDGE HOARDING", "P", 2, "Support", sev=0.8),
    Ev("BURNOUT WARNING", "P", 2, "Support", sev=1.0),
    Ev("MORE HANDS", "P", 2, "Engage", torso=False, sev=1.5),
    Ev("THE TEAM SPLITS", "P", 2, "SpeakUp", everyone=1, sev=1.2),
    Ev("A FLAT WEEK", "P", 1, "SpeakUp", everyone=1, sev=0.6),
    Ev("EQUIPMENT OUTAGE", "E", 3, "Support", sev=1.5),
    Ev("OLD FOUNDATIONS", "E", 2, "Engage", sev=2.0),
    Ev("FALSE START", "E", 2, None, sev=1.0),
    Ev("EVERYTHING AT ONCE", "E", 3, "SpeakUp", sev=2.5),
    Ev("SHAKY GROUND", "E", 3, "Engage", sev=2.0),
]

# Removal preference when an Event takes one of the week's cards away.
REMOVE_ORDER = ["Workshop", "Learn", "Reflect", "Plan", "Demo", "Teach", "Celebrate", "Work"]


# --------------------------------------------------------------------------------------
# Player policies
# --------------------------------------------------------------------------------------


@dataclass
class Strategy:
    name: str
    work_days: tuple = (3, 3, 3, 3, 3, 3, 3)   # Work cards wanted per week (of 5)
    trust_goal: int = 3                        # lay Engagement while Trust is below this
    celebrate_min: int = 1                     # Celebrate if anyone is at or below this
    celebrate_mean: float = 2.0                # ...or the mean is at or below this
    celebrate_every: int = 0                   # ...or every n-th week (0 = never)
    pool_goal: int = 4                         # lay Workshop while the pool is below this
    learn: int = 1                             # Learn/Teach cards per week from week 3
    reflect: bool = True
    plan: bool = True
    demo: bool = True
    overtime_weeks: tuple = ()
    repay_flex: bool = True
    adapt_threshold: float = 0.8               # cancel if severity / cost >= this
    hero_min_cost: int = 2                     # only spend the Hero on Events at least this big
    bank_tokens: bool = True                   # unused: a Reflect now always fills a well AND gives the pool token
    wolf: str = "if_mot"                       # always | never | if_mot
    take_one: bool = True                      # Take One For The Team / Dependable when Trust is low
    use_stand: bool = True                     # use Torso Stand when the rule exists
    random_play: bool = False                  # lay the five cards at random from what is open
    celebrate_needs_reason: bool = False       # lay Celebrate only when a feature should bank or the Events can all be covered
    plan_weeks: tuple = ()                     # weeks in which to lay a Plan whatever `plan` says
    workshop_weeks: tuple = ()                 # weeks in which to lay the Workshop whatever the pool holds
    care: bool = False                         # watch for characters at risk of quitting: Celebrate, and lay the card that meets their Need
    care_at: int = 1                           # at risk = this Motivation or lower at the start of the week
    finish_first: bool = False                 # add Work days when the planned days cannot cover the Work still owed


STRATEGIES = {
    # Pours every day into Work, ignores the Ledger, crunches the last weeks.
    "hero": Strategy(
        "hero", work_days=(5, 5, 5, 5, 5, 5, 5, 5), trust_goal=0, celebrate_min=1, celebrate_mean=0.0,
        pool_goal=0, learn=0, reflect=False, plan=False, demo=False, overtime_weeks=(6, 7, 8),
        adapt_threshold=99.0, hero_min_cost=1, bank_tokens=False, wolf="never", take_one=False),
    # Some investment early, Work-heavy late. Small tweaks from what optimal does: a full first week, Trust 4,
    # two Learn/Teach a week, cancel more Events, and only celebrate when there is something to mark.
    "balanced": Strategy("balanced", work_days=(4, 3, 3, 3, 3, 3, 4, 4), trust_goal=4, learn=2, adapt_threshold=0.5,
                         hero_min_cost=1, celebrate_needs_reason=True, care=True, finish_first=True),
    # Heavy early investment in Trust, the Zone and the pool.
    "invested": Strategy(
        "invested", work_days=(4, 2, 2, 3, 3, 4, 4, 4), trust_goal=4, pool_goal=4, learn=2,
        celebrate_every=3, adapt_threshold=0.5, hero_min_cost=1, celebrate_needs_reason=True, care=True, finish_first=True),
    # Lays five random cards from the ones that are open (Work twice as likely) and never plans ahead.
    "random": Strategy("random", random_play=True, take_one=False, repay_flex=False),
}


# --------------------------------------------------------------------------------------
# State
# --------------------------------------------------------------------------------------


class Char:
    def __init__(self, rng: random.Random, cid: int):
        self.id = cid
        self.head = rng.randrange(5)
        self.item = rng.randrange(5)
        self.torso = rng.choice(TORSOS)
        self.legs = rng.choice(LEGS)
        self.base = rng.choice(BASES)
        self.mot = 3
        self.capital = 0
        self.hero_used = False
        self.stand_used = False
        self.gift_used = False
        self.squares = {(self.head, self.item)}
        self.new_squares: set = set()
        self.flex = False
        self.cross_trained = False
        self.cap_gain_week = 0
        self.q_streak = 0


class Week:
    """Everything that is reset at the start of a week."""

    def __init__(self):
        self.coord = False
        self.trust_up = False
        self.trust_boost = False
        self.cap_up = False
        self.sp_up = False
        self.adds = 0
        self.banked: list = []
        self.adapted2 = False
        self.token_used = False
        self.hero_by: set = set()
        self.hero_log: list = []
        self.witness: dict = defaultdict(int)
        self.wit_named: set = set()
        self.take_dep = 0
        self.take_other = 0
        self.rec_met = 0
        self.equal = False
        self.false_start = False
        self.dashboard = False
        self.one_per = False
        self.halve = False
        self.flat = False
        self.track_lowered = False
        self.celebrated = False
        self.teach_played = False
        self.work_added = False
        self.blocked: set = set()
        self.ev_loss: dict = defaultdict(int)
        self.ev_by: dict = defaultdict(lambda: defaultdict(int))
        self.mot_adj: dict = defaultdict(int)
        self.survivors: list = []
        self.carry_next: str | None = None


class Game:
    def __init__(self, rules: Rules, strat: Strategy, rng: random.Random):
        self.R = rules
        self.st = strat
        self.rng = rng
        self.chars = [Char(rng, i) for i in range(rules.players)]
        for c in self.chars:
            c.mot = rules.mot_start
        self.next_id = rules.players
        self.feat = {
            k: {"cost": v[0], "cx": v[1], "dep": v[2], "work": 0, "banked": False}
            for k, v in FEATURES.items()
        }
        self.tiles: dict = {}
        for c in self.chars:
            sq = next(iter(c.squares))
            self.tiles[sq] = self.tiles.get(sq, 0) + 1
        self.trust = self.cap = self.sp = rules.ledger_start
        self.standing = 0
        self.pool = rules.pool_start
        self.habits: dict = {}
        self.wells: set = set()
        self.deck = EVENTS[:]
        rng.shuffle(self.deck)
        self.flex_owed = 0
        self.max_flex = 0
        self.deadline = rules.weeks
        self.burnout_ids: list = []
        self.celebrated_prev = False
        self.no_work_streak = 0
        self.prev = {"banked": False, "adapted2": False, "process": False, "work": False}
        self.burnout_new: list = []
        self.vacant = 0                      # seats left empty by quits, filled one per Onboarding card played
        self.carry: str | None = None
        self.quits = 0
        self.m: dict = defaultdict(float)
        self.mot_week_mean: list = []
        self.mot_week_min: list = []
        self.mot_hist_week: list = []
        self.mot_med_week: list = []
        self.mot_flow: Counter = Counter()
        self.need_met: Counter = Counter()
        self.need_seen: Counter = Counter()
        self.cancel_by: Counter = Counter()
        self.ps: Counter = Counter()
        self.pair_ps: Counter = Counter()
        self.pool_week: list = []
        self.last_bank_week = 0
        self.work_by_week: list = []
        self.trust_week: list = []
        self.cap_week: list = []
        self.sp_week: list = []
        self.standing_week: list = []
        self.capital_week: list = []
        self.banked_week: list = []
        self.drawn_week: list = []
        self.cancel_week: list = []
        self.cards_week: list = []
        self.wells_week: list = []
        self.evidence_week: list = []
        self.habitus_week: list = []
        self.habit_week: list = []
        self.prev_ev_by: dict = {}
        self.w = Week()

    # ------------------------------------------------------------------ helpers

    def eff_cost(self, ev: Ev):
        if ev.cost is None:
            return None
        c = ev.cost
        if ev.early and sum(1 for f in self.feat.values() if f["banked"]) <= self.R.early_max_features:
            c = max(0, c - self.R.early_discount)
        if CAT_HABIT[ev.cat] in self.habits:
            c = max(self.R.habit_min_cost, c - self.R.habit_discount)
        return c

    def remaining(self, k: str, pending: Counter | None = None) -> int:
        f = self.feat[k]
        return f["cost"] - f["work"] - (pending[k] if pending else 0)

    def candidates(self, pending: Counter | None = None, done_per: Counter | None = None):
        out = []
        for k, f in self.feat.items():
            if f["banked"] or k in self.w.blocked:
                continue
            if f["dep"] and not self.feat[f["dep"]]["banked"]:
                continue
            if self.w.one_per and done_per and done_per[k] >= 1:
                continue
            if self.remaining(k, pending) <= 0:
                continue
            out.append(k)
        return out

    def plan_target(self):
        cands = [k for k in self.candidates() if self.feat[k]["cx"] != "L"]
        if not cands:
            return None
        return min(cands, key=lambda k: (0 if k in ("B", "C") else 1, self.remaining(k)))

    def gain_capital(self, c: Char, amt: int, hero: bool = False, direct: bool = False):
        if self.w.equal:
            return
        if not hero and not direct and c.cap_gain_week >= 1:
            return
        before = c.capital
        c.capital = min(self.R.capital_cap, c.capital + amt)
        if not hero and not direct:
            c.cap_gain_week += 1
        self.m["capital_gained"] += amt
        if c.capital > before and not self.w.wit_named:
            for r in [x for x in self.chars if x.torso == "Recognition"]:
                others = [x for x in self.chars if x is not r]
                if others:
                    self.w.wit_named.add(r.id)
                    self.w.witness[min(others, key=lambda x: x.mot).id] += 1
                    break

    def lower(self, track: str):
        cur = getattr(self, track)
        if cur > 0:
            setattr(self, track, cur - 1)
            self.w.track_lowered = True

    def mot_cap_for(self, c: Char) -> int:
        return self.R.sheltered_cap if c.base == "Sheltered" else self.R.mot_cap

    def add_mot(self, c: Char, amt: int, source: str):
        before = c.mot
        c.mot = max(0, min(self.mot_cap_for(c), c.mot + amt))
        self.mot_flow[source] += c.mot - before

    def team_avg_capital(self) -> float:
        return statistics.mean(c.capital for c in self.chars) if self.chars else 0.0

    # ------------------------------------------------------------------ Zone

    def neighbours(self, sq, own_row_only: bool):
        r, c = sq
        steps = [(0, -1), (0, 1)] if own_row_only else [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in steps:
            rr, cc = r + dr, c + dc
            if 0 <= rr < 5 and 0 <= cc < 5:
                yield (rr, cc)

    def score_square(self, sq, p: Char) -> float:
        s = 0.0
        if sq in self.tiles:
            s += 2
        r, c = sq
        row_full = all(((r, cc) in self.tiles) or cc == c for cc in range(5))
        col_full = all(((rr, c) in self.tiles) or rr == r for rr in range(5))
        if sq not in self.tiles and (row_full or col_full):
            s += 3
        if len({q[0] for q in p.squares}) < 3 and r not in {q[0] for q in p.squares}:
            s += 0.5
        return s + self.rng.random() * 0.01

    def learn_option(self, c: Char):
        opts = []
        for sq in c.squares:
            if sq[0] != c.head:
                continue
            for nb in self.neighbours(sq, True):
                if nb not in c.squares:
                    opts.append(nb)
        return opts

    def teach_options(self, t: Char, p: Char):
        opts = set()
        for sq in t.squares - t.new_squares:
            for nb in self.neighbours(sq, False):
                if nb not in p.squares and nb in self.tiles:
                    opts.add(nb)
        return list(opts)

    def zone_add(self, c: Char, sq):
        if sq in c.squares:
            return
        c.squares.add(sq)
        c.new_squares.add(sq)
        n = self.tiles.get(sq, 0) + 1
        self.tiles[sq] = n
        if n == 2:
            self.w.sp_up = True
            self.m["stack_flips"] += 1
        r, col = sq
        R = self.R
        if n == 1:
            need = R.cap_first_len if self.m["lines_filled"] == 0 else 5
            in_row = sum(1 for cc in range(5) if (r, cc) in self.tiles)
            in_col = sum(1 for rr in range(5) if (rr, col) in self.tiles)
            if need in (in_row, in_col):
                self.w.cap_up = True
                self.m["lines_filled"] += 1
            elif R.cap_per_tiles and len(self.tiles) % R.cap_per_tiles == 0:
                self.w.cap_up = True
                self.m["tile_gains"] += 1
        rows = {q[0] for q in c.squares}
        if len(rows) >= R.cross_rows and not c.cross_trained:
            c.cross_trained = True
            self.w.cap_up = True

    def do_learn(self):
        learned = 0
        for c in self.chars:
            opts = self.learn_option(c)
            if not opts:
                continue
            self.zone_add(c, max(opts, key=lambda s: self.score_square(s, c)))
            learned += 1
            if c.base == "Bookish":
                self.w.mot_adj[c.id] += self.R.base_like
            elif c.base == "HandsOn":
                self.w.mot_adj[c.id] -= self.R.base_dislike
        if learned:
            self.m["learn_done"] += 1
            self.m["squares_learned"] += learned
        else:
            self.m["learn_wasted"] += 1

    def do_teach(self):
        used_t, used_p = set(), set()
        for _ in range(2):
            best, best_s = None, -1.0
            for t in self.chars:
                if t.id in used_t:
                    continue
                for p in self.chars:
                    if p.id == t.id or p.id in used_p:
                        continue
                    for sq in self.teach_options(t, p):
                        s = self.score_square(sq, p)
                        if s > best_s:
                            best, best_s = (t, p, sq), s
            if not best:
                break
            t, p, sq = best
            used_t.add(t.id)
            used_p.add(p.id)
            self.zone_add(p, sq)
            self.gain_capital(t, 1)
            self.m["teach_done"] += 1
            if t.base == "HandsOn":
                self.w.mot_adj[t.id] += self.R.base_like
            elif t.base == "Bookish":
                self.w.mot_adj[t.id] -= self.R.base_dislike
        if not used_t:
            self.m["teach_wasted"] += 1

    def zone_room_teach(self) -> bool:
        return any(self.teach_options(t, p) for t in self.chars for p in self.chars if t is not p)

    # ------------------------------------------------------------------ planning

    def bank_expected(self, plan: list) -> bool:
        n = plan.count("Work") * (2 if "Plan" in plan else 1)
        return n > 0 and any(self.remaining(k) <= n for k in self.candidates())

    def cover_capacity(self, w: int) -> int:
        R = self.R
        cap = self.pool
        if R.trust_cancel and self.trust >= R.trust_cancel_at:
            cap += 2
        if "AV" in self.habits:
            cap += 2 if not R.av_categories else max(1, 2 * len(R.av_categories) // 4)
        if w >= R.hero_from_week:
            heroes = sum(1 for c in self.chars if c.mot >= R.hero_min_mot and (not c.hero_used or c.base == "Competitive"))
            cap += 2 * min(2, heroes)
        return cap

    def celebrate_worth(self, w: int, plan: list) -> bool:
        if self.celebrated_prev and self.R.celebrate_repeat >= self.R.celebrate_banked:
            return False
        if self.bank_expected(plan):
            return True
        return w >= self.R.events_from_week and self.cover_capacity(w) >= 5

    def reflect_wells_open(self) -> list:
        """Team Reflexivity wells that last week's evidence could fill right now."""
        if "TR" in self.habits:
            return []
        p = self.prev
        out = []
        if p["banked"] and "OBJ" not in self.wells:
            out.append("OBJ")
        if p["adapted2"] and "STRAT" not in self.wells:
            out.append("STRAT")
        if p["process"] and "PROC" not in self.wells:
            out.append("PROC")
        return out

    def work_out(self, n: int) -> int:
        """Work that n Work cards would deliver at the Ledger as it stands (the first card is dead while Capability is low)."""
        R, total = self.R, 0
        for idx in range(1, n + 1):
            if idx == 1 and self.cap <= R.low_band:
                continue
            total += 1 + (1 if self.cap >= R.cap_bonus_at else 0) + (1 if idx >= 2 and self.sp >= R.sp_bonus_at else 0)
        return total

    def care_cards(self, w: int, cards: list):
        """A team that watches its people: for anyone at risk of quitting, lay Celebrate and the card that meets their Need."""
        risky = sorted((c for c in self.chars if c.mot <= self.st.care_at), key=lambda c: c.mot)
        quality_exposed = any(c.torso == "Quality" and c.mot <= self.R.quality_penalty + self.R.grind for c in self.chars)

        def put(card):
            if card in cards or cards.count("Work") <= 1:
                return
            cards[len(cards) - 1 - cards[::-1].index("Work")] = card

        # At most two cards change: a Motivation lift, and the Need card of the character closest to quitting
        if risky:
            p = self.prev
            if self.celebrate_worth(w, cards):
                put("Celebrate")
            elif w >= self.R.cards_from_week and self.trust >= self.R.reflect_trust and (p["banked"] or p["adapted2"] or p["process"]):
                put("Reflect")
            need_card = {"Community": "Engagement", "Hierarchy": "Learn" if w >= self.R.cards_from_week else None,
                         "Recognition": "Demo" if w >= self.R.demo_from_week else None}
            if need_card.get(risky[0].torso):
                put(need_card[risky[0].torso])
        if quality_exposed and "Work" not in cards and not ("Demo" in cards and self.demo_meets_quality()):
            spare = [i for i, x in enumerate(cards) if x not in ("Onboarding", "Celebrate")]
            if spare:
                cards[spare[-1]] = "Work"

    def plan_week(self, w: int):
        R, st = self.R, self.st
        self.m["empty_seat_weeks"] += self.vacant
        if st.random_play:
            open_cards = ["Work", "Work", "Engagement", "Celebrate"]
            if self.vacant:
                open_cards.append("Onboarding")
            if R.workshop_from_week <= w:
                open_cards.append("Workshop")
            if w >= R.plan_from_week:
                open_cards.append("Plan")
            if w >= R.cards_from_week:
                open_cards += ["Learn", "Teach", "Reflect"]
            if w >= R.demo_from_week:
                open_cards.append("Demo")
            picks = [self.rng.choice(open_cards) for _ in range(R.days)]
            for single in ("Reflect", "Celebrate", "Workshop", "Engagement"):
                if picks.count(single) > 1:
                    first = picks.index(single)
                    picks = [("Work" if c == single and i != first else c) for i, c in enumerate(picks)]
            if picks.count("Onboarding") > 1:
                first = picks.index("Onboarding")
                picks = [("Work" if c == "Onboarding" and i != first else c) for i, c in enumerate(picks)]
            return picks
        mots = [c.mot for c in self.chars] or [0]
        wanted = []
        if (min(mots) <= st.celebrate_min or statistics.mean(mots) <= st.celebrate_mean or (
                st.celebrate_every and w % st.celebrate_every == 0)) and not (
                self.celebrated_prev and R.celebrate_repeat >= R.celebrate_banked):
            wanted.append("Celebrate")
        if self.trust < st.trust_goal:
            wanted.append("Engagement")
        if R.workshop_from_week <= w < R.cards_from_week and self.pool < st.pool_goal and self.can_workshop():
            wanted.append("Workshop")
        if w >= R.cards_from_week:
            for k in range(st.learn):
                can_learn = any(self.learn_option(c) for c in self.chars)
                can_teach = self.trust > R.low_band and self.zone_room_teach()
                if can_teach and (not can_learn or (w + k) % 2 == 0):
                    wanted.append("Teach")
                else:
                    wanted.append("Learn")
            if st.reflect and self.trust >= R.reflect_trust:
                wanted.append("Reflect")
        if w >= R.plan_from_week and st.plan and self.sp > R.plan_dead_at and self.plan_target():
            wanted.append("Plan")
        if w >= R.cards_from_week:
            if self.pool < st.pool_goal and self.can_workshop():
                wanted.append("Workshop")
        if w >= R.demo_from_week and st.demo and self.chars:
            wanted.append("Demo")
        wd = st.work_days[min(w, len(st.work_days)) - 1]
        if st.finish_first and w >= 3 and self.chars:
            owed = sum(max(0, self.remaining(k)) for k, f in self.feat.items() if not f["banked"])
            short = owed - sum(st.work_days[w - 1:])
            if short > 0:
                wd = min(R.days, wd + -(-short // (self.deadline - w + 1)))
        slots = max(0, R.days - wd)
        # Plan makes every Work card on the feature produce double (+1 on top of its base 1), so Plan + 2 Work = 4 beats
        # 3 Work = 3: with 3 or more Work cards wanted, Plan takes one Work day; with 2 it takes a free slot.
        if (w >= R.plan_from_week and (st.plan or w in st.plan_weeks) and self.sp > R.plan_dead_at and self.plan_target() is not None
                and (wd >= 2 or w in st.plan_weeks)):
            wanted = [c for c in wanted if c != "Plan"]
            wanted.insert(1 if "Celebrate" in wanted else 0, "Plan")
            if wd >= 3 or slots < 1:
                slots += 1
        open_wells: list = []
        if w in st.workshop_weeks and w >= R.workshop_from_week and self.can_workshop():
            wanted = [c for c in wanted if c != "Workshop"]
            wanted.insert(1 if "Celebrate" in wanted else 0, "Workshop")
            slots = max(slots, 1)
        if w >= R.cards_from_week and st.reflect and self.trust >= R.reflect_trust:
            open_wells = self.reflect_wells_open()
            wanted = [c for c in wanted if c != "Reflect"]
            if open_wells:
                at = wanted.index("Plan") + 1 if "Plan" in wanted else (1 if "Celebrate" in wanted else 0)
                wanted.insert(at, "Reflect")
            else:
                wanted.append("Reflect")
        cards = wanted[:slots]
        if "Celebrate" in wanted and "Celebrate" not in cards:
            if cards:
                cards[-1] = "Celebrate"
            else:
                cards = ["Celebrate"]
        cards += ["Work"] * (R.days - len(cards))
        while cards.count("Reflect") > 1:
            cards[len(cards) - 1 - cards[::-1].index("Reflect")] = "Work"
        while cards.count("Engagement") > 1:
            cards[len(cards) - 1 - cards[::-1].index("Engagement")] = "Work"
        if self.vacant > 0 and "Onboarding" not in cards:
            cards[cards.index("Work") if "Work" in cards else -1] = "Onboarding"
        if st.celebrate_needs_reason and "Celebrate" in cards and not self.celebrate_worth(w, cards):
            cards[cards.index("Celebrate")] = "Work"
        if st.care:
            self.care_cards(w, cards)
        # Read the Ledger: with Capability in the low band the first Work card of the week delivers nothing
        spare = lambda: [i for i, x in enumerate(cards) if x not in ("Work", "Onboarding", "Celebrate")]
        if cards.count("Work") and self.work_out(cards.count("Work")) == 0 and spare():
            cards[spare()[-1]] = "Work"
        # The Quality Need is met only by Work added, so Quality characters need Work that delivers, plus one spare
        # card once Events are in play (an Event can remove a card after the week is laid)
        if any(c.torso == "Quality" for c in self.chars) and not ("Demo" in cards and self.demo_meets_quality()):
            spare_work = 1 if w >= R.events_from_week else 0
            while (self.work_out(cards.count("Work") - spare_work) == 0) and spare():
                cards[spare()[-1]] = "Work"
        # Plan + 2 Work beats 3 Work once Capability is out of the low band (the first Work card then delivers); in the low
        # band that first card is dead either way, so Plan only pays from 4 Work cards
        plan_pays_at = 4 if self.cap <= R.low_band else 3
        if w >= R.plan_from_week and "Plan" not in cards and cards.count("Work") >= plan_pays_at and self.plan_target() is not None:
            if self.sp > R.plan_dead_at:
                cards[cards.index("Work")] = "Plan"
            else:
                self.m["plan_skipped"] += 1
        if open_wells:
            self.m["tr_chances"] += 1
            if "Reflect" not in cards:
                self.m["tr_missed"] += 1
        if self.flex_owed > 0 and w < self.deadline and st.repay_flex and "Work" in cards:
            cards[cards.index("Work")] = "Flex"
            self.flex_owed -= 1
            for c in self.chars:
                if c.flex:
                    c.flex = False
                    break
        if w in st.overtime_weeks and self.flex_owed == 0:
            who = [c for c in self.chars if not c.flex and c.mot >= 3]
            if who:
                c = max(who, key=lambda x: x.mot)
                self.add_mot(c, -1, "overtime")
                c.flex = True
                self.flex_owed += 1
                self.m["overtime_cards"] += 1
                cards.append("Work")
        self.max_flex = max(self.max_flex, sum(1 for c in self.chars if c.flex), self.flex_owed)
        return cards

    # ------------------------------------------------------------------ events

    def draw(self, w: int):
        if w < self.R.events_from_week:
            return []
        n = min(self.R.events_per_week, len(self.deck))
        evs, held = [], []
        while len(evs) < n and self.deck:
            e = self.deck.pop()
            if e.name == "THE DATE MOVES UP" and w < self.R.date_moves_from_week:
                held.append(e)
                continue
            evs.append(e)
        for e in held:
            self.deck.insert(self.rng.randrange(len(self.deck) + 1), e)
        for e in evs:
            self.m["ev_drawn_w%d|%s" % (w, e.name)] += 1
        self.m["events_drawn"] += len(evs)
        return evs

    def pick_hero(self, ev: Ev, w: int):
        if ev.hero is None or w < self.R.hero_from_week or self.w.equal:
            return None
        ok = [c for c in self.chars if c.legs == ev.hero and c.mot >= self.R.hero_min_mot
              and (not c.hero_used or c.base == "Competitive")]
        return max(ok, key=lambda c: c.mot) if ok else None

    def can_workshop(self) -> bool:
        """The team only holds the Workshop when everyone can pay for it (nobody pays below align_min_mot)."""
        R = self.R
        return bool(R.align_tokens and self.chars and all(c.mot >= R.align_min_mot for c in self.chars))

    def do_workshop(self):
        R = self.R
        if not self.chars or any(c.mot - R.align_cost < 1 for c in self.chars):
            self.m["workshop_dead"] += 1
            return
        for c in self.chars:
            self.add_mot(c, -R.align_cost, "workshop")
        self.w.adds += R.align_tokens
        self.m["tokens_workshop"] += R.align_tokens

    def pick_stand(self, ev: Ev):
        ok = [c for c in self.chars if not c.stand_used and TORSO_CAT.get(c.torso) == ev.cat
              and c.mot - self.R.stand_cost >= 1]
        return max(ok, key=lambda c: c.mot) if ok else None

    def adapt(self, w: int, evs: list):
        R, st = self.R, self.st
        order = sorted(evs, key=lambda e: -e.sev)
        equal = [e for e in order if e.name == "EVERYONE IS EQUAL"]
        order = equal + [e for e in order if e.name != "EVERYONE IS EQUAL"]
        cancelled = set()
        used_trust = False
        used_av = False
        used_habit: set = set()
        hero_ok = True
        # a Celebrate laid without a feature about to bank only pays if every Event is cancelled
        push = st.celebrate_needs_reason and "Celebrate" in self.plan_now and not self.bank_expected(self.plan_now)
        thr = 0.0 if push else st.adapt_threshold
        for e in order:
            c = self.eff_cost(e)
            if c is None:
                continue
            self.m["event_cost_faced"] += c
            how = None
            if c == 0:
                how = "free"
            elif R.habit_cancel and not e.say_no and CAT_HABIT[e.cat] in self.habits and e.cat not in used_habit:
                used_habit.add(e.cat)
                how = "habit"
            elif R.trust_cancel and not e.say_no and not used_trust and self.trust >= R.trust_cancel_at:
                used_trust, how = True, "trust"
            elif not used_av and hero_ok and "AV" in self.habits and (not R.av_categories or e.cat in R.av_categories):
                used_av, how = True, "av"
            else:
                h = self.pick_hero(e, w) if hero_ok else None
                if h is not None and c >= st.hero_min_cost:
                    how = "hero"
                    if h.base != "Competitive":
                        h.hero_used = True
                    self.gain_capital(h, R.hero_capital, hero=True)
                    others = [x for x in self.chars if x is not h]
                    if others:
                        self.w.mot_adj[min(others, key=lambda x: x.mot).id] += 1
                    self.w.hero_by.add(h.id)
                    self.w.hero_log.append(h.id)
                    self.m["hero_plays"] += 1
                    self.ps[("legs", h.legs, "hero")] += 1
                elif (R.stand and st.use_stand and hero_ok and w >= R.hero_from_week and c >= st.hero_min_cost
                      and e.sev / c >= thr and self.pick_stand(e) is not None):
                    s = self.pick_stand(e)
                    s.stand_used = True
                    self.add_mot(s, -R.stand_cost, "stand")
                    self.m["stand_plays"] += 1
                    how = "stand"
                elif not e.say_no and self.pool >= c and e.sev / c >= thr:
                    self.pool -= c
                    self.m["tokens_spent"] += c
                    how = "token"
            if how:
                cancelled.add(e.name)
                self.cancel_by[how] += 1
                if how == "token":
                    self.w.token_used = True
            elif e.name == "EVERYONE IS EQUAL":
                hero_ok = False
                self.w.equal = True
        wolf = [e for e in evs if e.cost is None]
        self.w.survivors = [e for e in evs if e.name not in cancelled]
        self.w.adapted2 = len(evs) == 2 and not wolf and len(cancelled) == 2

    def remove_card(self, plan: list):
        if plan.count("Engagement") > 1:
            plan.remove("Engagement")
            return
        for k in REMOVE_ORDER:
            if k in plan:
                plan.remove(k)
                return

    def apply_mot(self, e: Ev):
        for c in self.chars:
            if e.name == "LEADS FROM BEHIND":
                top = max(x.capital for x in self.chars)
                loss = 0 if c.capital == top and top > 0 else e.everyone
            elif not e.torso:
                loss = e.everyone
            else:
                hit = e.hit or CAT_HIT[e.cat]
                imm = None if e.hit else CAT_IMMUNE[e.cat]
                if e.everyone and c.torso == imm:
                    loss = 0
                    self.m["immune_saved"] += e.everyone
                    self.m["immune_saved_" + c.torso] += e.everyone
                else:
                    loss = e.everyone + (1 if c.torso == hit else 0)
                    if c.torso == hit:
                        self.m["hit_extra"] += 1
            if loss:
                self.w.ev_loss[c.id] += loss
                self.w.ev_by[c.id][e.name] += loss

    def resolve_events(self, w: int, plan: list):
        W = self.w
        R, st = self.R, self.st
        # Own the mistake: the Trust step is shared with Engagement and Take One For The Team (one a week)
        if (R.ownit_trust and W.survivors and "Engagement" not in plan and not W.trust_boost
                and self.trust < st.trust_goal and self.trust < R.ledger_max):
            owners = [c for c in self.chars if c.legs == "OwnIt" and c.mot >= R.own_min_mot]
            if owners:
                c = max(owners, key=lambda x: x.mot)
                self.add_mot(c, -R.own_cost, "own_it")
                self.trust = min(R.ledger_max, self.trust + 1)
                W.trust_boost = True
                self.m["own_it"] += 1
        for e in W.survivors:
            n = e.name
            self.m["ev_landed|" + n] += 1
            self.m["ev_landed_w%d|%s" % (w, n)] += 1
            if n == "THE WOLF":
                self.resolve_wolf()
                continue
            if not (n == "THE AUDIT" and "Workshop" in plan):
                self.apply_mot(e)
            if n in ("STATUS MEETING", "PRIORITY CHANGES"):
                self.remove_card(plan)
            elif n == "REORGANISED":
                self.lower("sp")
            elif n == "THE AUDIT":
                if "Workshop" not in plan:
                    self.remove_card(plan)
                    self.lower("trust")
            elif n == "THE BIKESHED":
                avail = [k for k, f in self.feat.items() if not f["banked"]]
                if avail:
                    easy = min(avail, key=lambda k: self.remaining(k))
                    self.feat[easy]["work"] += 1
                    hard = max(avail, key=lambda k: ("LMH".index(self.feat[k]["cx"]), self.remaining(k)))
                    if hard != easy:
                        W.blocked.add(hard)
            elif n == "EVERYONE IS EQUAL":
                W.equal = True
            elif n == "REQUIREMENTS CHANGE":
                avail = [k for k, f in self.feat.items() if not f["banked"]]
                if avail:
                    f = self.feat[max(avail, key=lambda k: self.remaining(k))]
                    if f["work"] > 0:
                        f["work"] -= 1
                        self.m["rework_lost"] += 1
            elif n == "NEGATIVE FEEDBACK":
                banked = [k for k, f in self.feat.items() if f["banked"]]
                if banked:
                    k = max(banked, key=lambda x: self.feat[x]["cost"])
                    f = self.feat[k]
                    f["work"] = max(0, f["work"] - 2)
                    self.m["rework_lost"] += 2
                    if f["work"] < f["cost"]:
                        f["banked"] = False
            elif n == "SCOPE CREEP":
                avail = [k for k, f in self.feat.items() if not f["banked"]]
                if avail:
                    k = max(avail, key=lambda x: self.feat[x]["work"] / self.feat[x]["cost"])
                    self.feat[k]["cost"] += 2
                    self.m["cost_added"] += 2
            elif n == "THE DATE MOVES UP":
                if self.deadline > w:
                    self.deadline -= 1
                    self.m["deadline_moved"] += 1
            elif n == "THE DASHBOARD":
                W.dashboard = True
            elif n == "ALWAYS REACTING":
                if self.pool > 0:
                    self.pool -= 1
                    self.m["tokens_lost"] += 1
            elif n == "KNOWLEDGE HOARDING":
                plan[:] = [x for x in plan if x != "Teach"]
            elif n == "BURNOUT WARNING":
                self.burnout_new = [c.id for c in self.chars if c.mot <= 1]
            elif n == "MORE HANDS":
                W.halve = True
            elif n == "THE TEAM SPLITS":
                self.lower("trust")
            elif n == "A FLAT WEEK":
                W.flat = True
            elif n == "EQUIPMENT OUTAGE":
                if "Work" in plan:
                    plan.remove("Work")
            elif n == "OLD FOUNDATIONS":
                banked = [k for k, f in self.feat.items() if f["banked"]]
                if banked:
                    k = max(banked, key=lambda x: self.feat[x]["work"])
                    self.feat[k]["cost"] += 2
                    self.m["cost_added"] += 2
                    if self.feat[k]["work"] < self.feat[k]["cost"]:
                        self.feat[k]["banked"] = False
            elif n == "FALSE START":
                W.false_start = True
            elif n == "EVERYTHING AT ONCE":
                W.one_per = True
            elif n == "SHAKY GROUND":
                self.lower("cap")

    def resolve_wolf(self):
        if not self.chars:
            return
        top = max(c.capital for c in self.chars)
        if top <= 0:
            return
        shepherd = self.rng.choice([c for c in self.chars if c.capital == top])
        mean_mot = statistics.mean(c.mot for c in self.chars)
        step = self.st.wolf == "always" or (self.st.wolf == "if_mot" and mean_mot >= 3)
        if step:
            shepherd.capital = min(self.R.capital_cap, shepherd.capital + 1)
            for c in self.chars:
                self.w.ev_loss[c.id] += 1
                self.w.ev_by[c.id]["THE WOLF"] += 1
            self.m["wolf_stepped_up"] += 1
        else:
            shepherd.capital = 0
            self.m["wolf_capital_erased"] += 1

    # ------------------------------------------------------------------ the week runs

    def pick_target(self, plan_f, pending: Counter, done_per: Counter):
        cands = self.candidates(pending, done_per)
        if not cands:
            return None
        if plan_f in cands:
            return plan_f
        W = self.w
        return min(cands, key=lambda k: (
            0 if (W.dashboard and self.feat[k]["cx"] == "L") else 1,
            0 if k in ("B", "C") else 1,
            self.remaining(k, pending)))

    def do_work(self, w: int, plan: list):
        R, W = self.R, self.w
        n = plan.count("Work")
        plan_f = None
        if "Plan" in plan and self.s0 > R.plan_dead_at:
            t = self.plan_target()
            if t:
                plan_f = t
                if self.feat[t]["cx"] == "H":
                    W.carry_next = t
        pending: Counter = Counter()
        done_per: Counter = Counter()
        idx = 0
        for _ in range(n):
            f = self.pick_target(plan_f, pending, done_per)
            idx += 1
            if f is None:
                self.m["work_cards_wasted"] += 1
                continue
            first_dead = idx == 1 and (self.c0 <= R.low_band or W.false_start)
            if first_dead:
                out = 0
            else:
                out = 1
                if self.c0 >= R.cap_bonus_at:
                    out += 1
                if idx >= 2 and self.s0 >= R.sp_bonus_at:
                    out += 1
                if self.feat[f]["cx"] != "L" and (f == plan_f or f == self.carry):
                    out += R.plan_bonus
                    self.m["plan_extra_work"] += R.plan_bonus
                if W.dashboard and self.feat[f]["cx"] != "L":
                    out = 0
                out = max(0, out)
            pending[f] += out
            done_per[f] += 1
        if W.halve and pending:
            top = max(pending, key=lambda k: pending[k])
            pending[top] //= 2
        total = 0
        for f, o in pending.items():
            self.feat[f]["work"] += o
            total += o
        W.work_added = total > 0
        self.m["work_out"] += total
        self.m["work_cards"] += n
        self.work_by_week.append(total)

    def banked_now(self):
        return [k for k, f in self.feat.items() if not f["banked"] and f["work"] >= f["cost"]]

    def run_cards(self, w: int, plan: list):
        R, W, st = self.R, self.w, self.st
        self.do_work(w, plan)
        if "Onboarding" in plan and self.vacant > 0:
            self.vacant -= 1
            self.m["onboarding_played"] += 1
            c = Char(self.rng, self.next_id)
            self.next_id += 1
            c.mot = R.mot_start
            self.chars.append(c)
            sq = next(iter(c.squares))
            self.tiles[sq] = self.tiles.get(sq, 0) + 1
        if w == 1:
            self.m["week1_coordinate"] += plan.count("Engagement")
        newly = self.banked_now()
        for c in self.chars:
            c.new_squares = set()
        if "Engagement" in plan:
            W.coord = True
            W.trust_up = True
        if "Celebrate" in plan:
            W.celebrated = True
            amt = R.celebrate_banked if (newly and not W.flat) else R.celebrate
            if self.celebrated_prev:
                amt = max(0, amt - R.celebrate_repeat)
            reason = (bool(newly) and not W.flat) or (self.drawn_week[-1] > 0 and not W.survivors)
            if R.celebrate_needs_reason and not reason:
                amt = 0
                self.m["celebrate_empty"] += 1
            for c in self.chars:
                if c.mot <= R.celebrate_max_mot:
                    self.add_mot(c, amt, "celebrate")
                else:
                    self.m["celebrate_capped"] += 1
            self.m["celebrates"] += 1
        for card in plan:
            if card == "Workshop":
                self.do_workshop()
        for _ in range(plan.count("Learn")):
            self.do_learn()
        n_teach = plan.count("Teach")
        if n_teach and self.t0 > R.low_band:
            W.teach_played = True
            for _ in range(n_teach):
                self.do_teach()
        elif n_teach:
            self.m["teach_dead"] += n_teach
        if "Demo" in plan:
            elig = [c for c in self.chars if c.capital >= self.team_avg_capital()]
            if elig:
                tgt = min(elig, key=lambda c: c.capital)
                self.gain_capital(tgt, 1)
                W.mot_adj[tgt.id] += 1
                W.adds += 1
                self.m["tokens_demo"] += 1
        for _ in range(min(1, plan.count("Reflect"))):
            self.do_reflect(newly)
        if st.take_one and not W.coord and not W.trust_boost and self.t0 < st.trust_goal:
            def floor(c):
                # the Need can cancel the grind from week 1, but it is not guaranteed, so keep one spare point
                return R.dependable_cost + 1
            who = [c for c in self.chars if c.base == "Dependable" and c.mot >= floor(c)]
            if who:
                c = max(who, key=lambda x: x.mot)
                cost = R.dependable_cost
                self.add_mot(c, -cost, "take_one")
                W.take_dep += 1
                W.trust_boost = True
                self.trust = min(R.ledger_max, self.trust + 1)
                self.gain_capital(c, 1)

    def do_reflect(self, newly: list):
        R, W, st = self.R, self.w, self.st
        if self.t0 < R.reflect_trust:
            self.m["reflect_dead"] += 1
            return
        p = self.prev
        self.m["reflect_played"] += 1
        evidence = p["banked"] or p["adapted2"] or p["process"]
        if not evidence:
            self.m["reflect_no_evidence"] += 1
        if evidence:
            W.sp_up = True
            for c in self.chars:
                if c.mot <= R.celebrate_max_mot:
                    self.add_mot(c, R.reflect_mot, "reflect")
        wells = []
        if p["banked"] and "OBJ" not in self.wells:
            wells.append("OBJ")
        if p["adapted2"] and "STRAT" not in self.wells:
            wells.append("STRAT")
        if p["process"] and "PROC" not in self.wells:
            wells.append("PROC")
        if wells and "TR" not in self.habits:
            self.wells.add(wells[0])
            self.m["tokens_banked_tr"] += 1
        W.adds += 1
        self.m["tokens_reflect"] += 1

    # ------------------------------------------------------------------ close the week

    def vindicate(self, habit: str):
        for c in self.chars:
            if c.torso == HABIT_TORSO.get(habit):
                c.capital = min(self.R.capital_cap, c.capital + 1)

    def flip(self, name: str, w: int):
        if name not in self.habits:
            self.habits[name] = w
            self.vindicate(name)

    def close_week(self, w: int):
        R, W = self.R, self.w
        for k in self.banked_now():
            self.feat[k]["banked"] = True
            W.banked.append(k)
            self.last_bank_week = w
        if w >= 2:
            if W.trust_up:
                self.trust = min(R.ledger_max, self.trust + 1)
            if W.cap_up:
                self.cap = min(R.ledger_max, self.cap + 1)
            if W.sp_up:
                self.sp = min(R.ledger_max, self.sp + 1)
        for name, val in (("PS", self.trust), ("WKW", self.cap), ("SR", self.sp)):
            if val >= R.habit_at:
                self.flip(name, w)
        if R.standing_live and self.chars:
            self.standing = max(c.capital for c in self.chars)
        if self.standing >= R.habit_at:
            self.flip("AV", w)
        room = R.pool_cap - self.pool
        self.m["tokens_wasted_cap"] += max(0, W.adds - room)
        self.pool = min(R.pool_cap, self.pool + W.adds)
        self.m["tokens_earned"] += W.adds
        if len(self.wells) >= R.tr_wells:
            self.flip("TR", w)
        if w >= R.combos_from_week:
            self.combos(w)

    def combos(self, w: int):
        W = self.w
        plan = self.plan_now
        if not self.chars:
            return
        if "Demo" in plan and W.celebrated:
            self.trust = min(self.R.ledger_max, self.trust + 1)
        elif "Engagement" in plan and "Workshop" in plan:
            self.gain_capital(min(self.chars, key=lambda c: c.capital), 1)
        elif W.hero_by and W.celebrated:
            for c in self.chars:
                W.mot_adj[c.id] += 1
        elif "Workshop" in plan and self.cancelled_any:
            self.pool = min(self.R.pool_cap, self.pool + 1)
        else:
            return
        self.m["combos"] += 1

    # ------------------------------------------------------------------ Motivation (step 7)

    def demo_meets_quality(self) -> bool:
        return self.R.quality_demo

    def need_ok(self, c: Char) -> bool:
        W, plan = self.w, self.plan_now
        t = c.torso
        hab = {"Autonomy": "SR", "Hierarchy": "WKW", "Community": "PS"}.get(t)
        if hab and hab in self.habits and not (t == "Community" and any(e.cat in ("P", "M") for e in W.survivors)):
            return True
        if t == "Autonomy":
            if self.R.autonomy_rule == "management":
                return not any(e.cat == "M" for e in W.survivors)
            return len(W.survivors) <= self.R.autonomy_max_landed
        if t == "Hierarchy":
            return W.teach_played or any(x in plan for x in ("Learn", "Workshop"))
        if t == "Community":
            return any(x in plan for x in ("Engagement", "Reflect"))
        if t == "Quality":
            return W.work_added or (self.demo_meets_quality() and "Demo" in plan)
        return bool(W.banked) or c.id in W.hero_by or "Demo" in plan

    def legs_delta(self, c: Char, w: int) -> int:
        R = self.R
        if not R.legs_tendencies or w < 2:
            return 0
        if c.legs == "Engage":
            return 1 if w <= 3 else -1 if w in R.engage_low_weeks else 0
        v = {"OwnIt": self.trust, "Analyze": self.cap, "Support": self.sp, "SpeakUp": self.standing}[c.legs]
        if c.legs == "SpeakUp" and R.speakup_gift:
            return 0
        if c.legs == "OwnIt" and R.ownit_trust:
            return -1 if self.trust <= R.low_band else 0
        if v >= R.legs_strength_at:
            return R.speakup_strength if c.legs == "SpeakUp" else 1
        if v <= R.low_band:
            return -1
        return 0

    def motivation_step(self, w: int):
        R, W = self.R, self.w
        quitters = []
        causes: dict = {}
        if w >= R.need_from_week:
            if W.work_added:
                self.no_work_streak = 0
            else:
                self.no_work_streak += 1
                self.m["no_work_weeks"] += 1
                self.m["max_no_work_streak"] = max(self.m["max_no_work_streak"], self.no_work_streak)
        for c in list(self.chars):
            d = 0
            neg: dict = {}
            if c.base != "Sheltered":
                d -= R.grind
                neg["the weekly grind"] = R.grind
                self.mot_flow["grind"] -= R.grind
            ev = W.ev_loss.get(c.id, 0)
            for e_name, e_loss in W.ev_by.get(c.id, {}).items():
                for kind, val in ("torso", c.torso), ("legs", c.legs), ("base", c.base):
                    self.m["evx|%s|%s|%s" % (kind, val, e_name)] += e_loss
            if ev:
                d -= ev
                neg["Events"] = ev
                self.mot_flow["event"] -= ev
            if w >= R.need_from_week:
                self.need_seen[c.torso] += 1
                if self.need_ok(c):
                    self.need_met[c.torso] += 1
                    if c.torso == "Quality":
                        c.q_streak = 0
                    if c.torso == "Recognition":
                        W.rec_met += 1
                    d += R.need_bonus
                    self.mot_flow["need"] += R.need_bonus
                elif c.torso == "Quality":
                    c.q_streak += 1
                    d -= R.quality_penalty
                    neg["a week without Work (Quality Need)"] = R.quality_penalty
                    self.mot_flow["quality_penalty"] -= R.quality_penalty
            if c.base == "Competitive":
                lost = sum(1 for h in W.hero_log if h != c.id)
                if lost:
                    d -= lost
                    neg["another character's Hero"] = lost
                    self.mot_flow["competitive"] -= lost
            wit = W.witness.get(c.id, 0)
            if wit:
                d += wit
                self.mot_flow["recognition_witness"] += wit
            ld = self.legs_delta(c, w)
            if ld:
                d += ld
                self.mot_flow["legs_up" if ld > 0 else "legs_down"] += ld
                if ld < 0:
                    neg["a track in the low band (instinct)"] = -ld
            adj = W.mot_adj.get(c.id, 0)
            if adj:
                d += adj
                self.mot_flow["base_hero_gift"] += adj
            c.mot = max(0, min(self.mot_cap_for(c), c.mot + d))
            if c.mot <= 0:
                quitters.append(c)
                causes[c.id] = max(neg, key=neg.get) if neg else "spent it on Workshop, Overtime or Take One"
        if R.speakup_gift and w >= R.gift_from_week and self.trust >= R.gift_trust_min:
            for g in sorted(self.chars, key=lambda x: x.id):
                if g.legs != "SpeakUp" or g.gift_used or g in quitters:
                    continue
                mates = [c for c in self.chars if c is not g]
                if not mates:
                    continue
                c = min(mates, key=lambda x: x.mot)
                if not (c in quitters or c.mot <= R.gift_receiver_max or (w == R.weeks and c.mot < self.mot_cap_for(c))):
                    continue
                g.gift_used = True
                c.mot = min(self.mot_cap_for(c), c.mot + 1)
                self.mot_flow["speakup_gift"] += 1
                self.m["gifts"] += 1
                if c in quitters:
                    quitters.remove(c)
                    causes.pop(c.id, None)
                    self.m["gift_rescues"] += 1
        if self.burnout_ids:
            if not W.celebrated:
                for c in self.chars:
                    if c.id in self.burnout_ids and c not in quitters and c.mot <= 1:
                        quitters.append(c)
        self.burnout_ids, self.burnout_new = self.burnout_new, []
        for c in self.chars:
            for kind, val in ("torso", c.torso), ("legs", c.legs), ("base", c.base):
                self.ps[(kind, val, "weeks")] += 1
                self.ps[(kind, val, "mot")] += c.mot
                self.ps[(kind, val, "capital")] += c.capital
                if c in quitters:
                    self.ps[(kind, val, "quits")] += 1
            tags = (("values", c.torso), ("instinct", c.legs), ("upbringing", c.base))
            for i in range(3):
                for j in range(i + 1, 3):
                    pk = "%s %s + %s %s" % (tags[i][0], tags[i][1], tags[j][0], tags[j][1])
                    self.pair_ps[pk + "|weeks"] += 1
                    if c in quitters:
                        self.pair_ps[pk + "|quits"] += 1
        for c in quitters:
            if c in self.chars:
                self.chars.remove(c)
                self.quits += 1
                self.m["quit_cause_" + causes.get(c.id, "the burnout Event")] += 1
                look = Counter()
                for src in (W.ev_by, self.prev_ev_by):
                    look.update(src.get(c.id, {}))
                look_total = sum(look.values())
                if look_total:
                    for e_name, e_loss in look.items():
                        for kind, val in ("torso", c.torso), ("legs", c.legs), ("base", c.base):
                            self.m["evq|%s|%s|%s" % (kind, val, e_name)] += e_loss / look_total
                if causes.get(c.id) == "Events" and W.ev_by.get(c.id):
                    by = W.ev_by[c.id]
                    self.m["ev_quit|" + max(by, key=by.get)] += 1
                    if c.torso == "Quality":
                        self.m["ev_quit_q|" + max(by, key=by.get)] += 1
                if c.torso == "Quality":
                    self.m["quit_q_cause|" + causes.get(c.id, "the burnout Event")] += 1
                for kind, val in (("torso", c.torso), ("legs", c.legs), ("base", c.base)):
                    self.m["quit_who_%d|%s|%s" % (w, kind, val)] += 1
                if c.torso == "Quality":
                    self.m["quality_quits"] += 1
                    if c.q_streak >= 1:
                        self.m["quality_quit_nowork"] += 1
                    if c.q_streak >= 2:
                        self.m["quality_quit_multiweek"] += 1
                self.m["quit_week_%d" % w] += 1
                self.vacant += 1
        if R.quit_mot_cost and quitters:
            gone = sum(1 for c in quitters if c not in self.chars)
            for c in self.chars:
                self.add_mot(c, -R.quit_mot_cost * gone, "quit_knock_on")

    # ------------------------------------------------------------------ driver

    def begin_week(self, w: int):
        for c in self.chars:
            c.cap_gain_week = 0
        self.carry = self.w.carry_next if w > 1 else None
        self.celebrated_prev = self.w.celebrated
        self.prev_ev_by = self.w.ev_by
        self.prev = {"banked": bool(self.w.banked), "adapted2": self.w.adapted2, "work": self.w.work_added,
                     "process": bool(self.w.track_lowered or self.w.hero_by or self.w.token_used)}
        self.w = Week()
        self.t0, self.c0, self.s0 = self.trust, self.cap, self.sp
        self.cancelled_any = False

    def run(self) -> dict:
        R = self.R
        for w in range(1, R.weeks + 1):
            if w > self.deadline:
                self.pad_week()
                continue
            self.begin_week(w)
            self.evidence_week.append({k: int(bool(v)) for k, v in self.prev.items()})
            plan = self.plan_week(w)
            self.plan_now = plan
            evs = self.draw(w)
            before = Counter(self.cancel_by)
            self.adapt(w, evs)
            self.cancel_week.append(dict(self.cancel_by - before))
            self.drawn_week.append(len(evs))
            self.cancelled_any = len(self.w.survivors) < len(evs)
            self.resolve_events(w, plan)
            self.cards_week.append(dict(Counter(plan)))
            self.run_cards(w, plan)
            self.close_week(w)
            self.wells_week.append({k: int(k in self.wells) for k in ("OBJ", "STRAT", "PROC")})
            self.motivation_step(w)
            Wk = self.w
            self.habitus_week.append({
                "hero": len(Wk.hero_log), "dependable": Wk.take_dep, "take_one": Wk.take_other,
                "recognition_witness": sum(Wk.witness.values()), "recognition_need_met": Wk.rec_met})
            self.pool_week.append(self.pool)
            if self.chars:
                self.mot_week_mean.append(statistics.mean(c.mot for c in self.chars))
                self.mot_week_min.append(min(c.mot for c in self.chars))
            else:
                self.mot_week_mean.append(0)
                self.mot_week_min.append(0)
            self.mot_hist_week.append([sum(1 for c in self.chars if c.mot == v) for v in range(R.mot_cap + 1)])
            self.mot_med_week.append(statistics.median(c.mot for c in self.chars) if self.chars else 0)
            self.trust_week.append(self.trust)
            self.cap_week.append(self.cap)
            self.sp_week.append(self.sp)
            self.standing_week.append(self.standing)
            self.habit_week.append({h: 1 for h in self.habits})
            self.capital_week.append(statistics.mean(c.capital for c in self.chars) if self.chars else 0)
            self.banked_week.append(sum(1 for f in self.feat.values() if f["banked"]))
            if w == 1:
                self.catch_up_trust()
        return self.finish()

    def pad_week(self):
        """A week that never happens (the deadline moved up) still needs a row in every per-week list."""
        self.evidence_week.append({k: 0 for k in self.prev})
        self.cancel_week.append({})
        self.drawn_week.append(0)
        self.cards_week.append({})
        self.wells_week.append(dict(self.wells_week[-1]))
        self.habitus_week.append({"hero": 0, "dependable": 0, "take_one": 0, "recognition_witness": 0, "recognition_need_met": 0})
        for lst in (self.pool_week, self.mot_week_mean, self.mot_week_min, self.mot_hist_week, self.mot_med_week, self.trust_week,
                    self.cap_week, self.sp_week, self.standing_week, self.habit_week, self.capital_week, self.banked_week):
            lst.append(lst[-1])

    def catch_up_trust(self):
        # Week 2 reveal: Trust rises 1 if an Engagement was played in week 1 (there is one Engagement card).
        n = self.m["week1_coordinate"]
        self.trust = min(self.R.ledger_max, self.trust + (1 if n else 0))

    def finish(self) -> dict:
        R = self.R
        banked = sum(1 for f in self.feat.values() if f["banked"])
        flex = sum(1 for c in self.chars if c.flex)
        low_tracks = sum(1 for v in (self.trust, self.cap, self.sp) if v <= R.low_band)
        score = (banked * R.feature_value + self.trust + self.cap + self.sp + self.pool
                 + sum(c.mot for c in self.chars) - R.quit_penalty * self.quits - R.flex_penalty * flex
                 - R.low_track_penalty * low_tracks + R.habit_score * len(self.habits))
        if banked < len(self.feat):
            score = 0                                   # an unfinished project scores nothing
        score = max(0, score)
        threshold = R.threshold_base + R.threshold_per_player * R.players
        threshold_high = R.threshold_high_base + R.threshold_per_player * R.players
        if banked < len(self.feat):
            outcome = "failure"
        elif score >= threshold_high:
            outcome = "thriving"
        elif score >= threshold:
            outcome = "sustainable"
        else:
            outcome = "heroic"
        needed = sum(f["cost"] for f in self.feat.values())
        return {
            "banked": banked, "score": score, "threshold": threshold, "threshold_high": threshold_high, "outcome": outcome,
            "work_out": self.m["work_out"], "work_cards": self.m["work_cards"], "work_needed": needed,
            "work_wasted": self.m["work_cards_wasted"], "rework_lost": self.m["rework_lost"], "plan_extra_work": self.m["plan_extra_work"], "plan_skipped": self.m["plan_skipped"],
            "cost_added": self.m["cost_added"], "last_bank_week": self.last_bank_week, "deadline_moved": self.m["deadline_moved"],
            "work_by_week": list(self.work_by_week) + [0] * (R.weeks - len(self.work_by_week)),
            "tokens_earned": self.m["tokens_earned"], "tokens_spent": self.m["tokens_spent"],
            "tokens_lost": self.m["tokens_lost"], "tokens_wasted_cap": self.m["tokens_wasted_cap"],
            "tokens_banked_tr": self.m["tokens_banked_tr"], "pool_end": self.pool,
            "pool_week": list(self.pool_week), "events_drawn": self.m["events_drawn"],
            "event_cost_faced": self.m["event_cost_faced"], "cancel_by": dict(self.cancel_by),
            "habits": dict(self.habits), "hero_plays": self.m["hero_plays"],
            "wolf_up": self.m["wolf_stepped_up"], "wolf_erased": self.m["wolf_capital_erased"],
            "combos": self.m["combos"], "quits": self.quits, "gifts": self.m["gifts"], "gift_rescues": self.m["gift_rescues"], "own_it": self.m["own_it"],
            "quality_quits": self.m["quality_quits"], "quality_quit_nowork": self.m["quality_quit_nowork"],
            "quality_quit_multiweek": self.m["quality_quit_multiweek"], "no_work_weeks": self.m["no_work_weeks"],
            "max_no_work_streak": self.m["max_no_work_streak"],
            "mot_mean": list(self.mot_week_mean), "mot_min": list(self.mot_week_min),
            "mot_hist": list(self.mot_hist_week), "mot_med": list(self.mot_med_week),
            "quit_causes": {k[len("quit_cause_"):]: v for k, v in self.m.items() if k.startswith("quit_cause_")},
            "quit_who": {k[len("quit_who_"):]: v for k, v in self.m.items() if k.startswith("quit_who_")},
            "event_stats": {k: v for k, v in self.m.items() if k.startswith(("ev_landed|", "ev_quit|", "ev_quit_q|", "quit_q_cause|", "ev_drawn_w", "ev_landed_w"))},
            "event_habitus": {k: v for k, v in self.m.items() if k.startswith(("evq|", "evx|"))},
            "empty_seat_weeks": self.m["empty_seat_weeks"], "onboarding_played": self.m["onboarding_played"], "quit_week": [self.m["quit_week_%d" % i] for i in range(1, R.weeks + 1)],
            "trust_week": list(self.trust_week), "cap_week": list(self.cap_week), "sp_week": list(self.sp_week),
            "standing_week": list(self.standing_week), "capital_week": list(self.capital_week),
            "banked_week": list(self.banked_week), "drawn_week": list(self.drawn_week),
            "cancel_week": list(self.cancel_week), "cards_week": list(self.cards_week),
            "wells_week": list(self.wells_week), "evidence_week": list(self.evidence_week),
            "habitus_week": list(self.habitus_week),
            "habit_week": list(self.habit_week),
            "parts": {"%s|%s|%s" % k: v for k, v in self.ps.items()},
            "quit_pairs": dict(self.pair_ps),
            "mot_flow": dict(self.mot_flow), "celebrates": self.m["celebrates"], "celebrate_capped": self.m["celebrate_capped"],
            "celebrate_empty": self.m["celebrate_empty"],
            "need_met": dict(self.need_met), "need_seen": dict(self.need_seen),
            "trust": self.trust, "cap": self.cap, "sp": self.sp, "flex_unrepaid": flex, "max_flex": self.max_flex, "low_tracks": low_tracks,
            "teach_dead": self.m["teach_dead"], "reflect_dead": self.m["reflect_dead"],
            "reflect_played": self.m["reflect_played"], "reflect_no_evidence": self.m["reflect_no_evidence"],
            "tr_well_skipped": self.m["tr_well_skipped"], "tr_wells_filled": len(self.wells),
            "tr_chances": self.m["tr_chances"], "tr_missed": self.m["tr_missed"],
            "immune_saved": self.m["immune_saved"], "hit_extra": self.m["hit_extra"],
            "immune_by": {t: self.m["immune_saved_" + t] for t in ("Autonomy", "Hierarchy", "Community", "Quality", "Recognition")},
            "tokens_reflect": self.m["tokens_reflect"],
            "lines_filled": self.m["lines_filled"], "stack_flips": self.m["stack_flips"],
            "zone_tiles": len(self.tiles), "squares_learned": self.m["squares_learned"],
        }


# --------------------------------------------------------------------------------------
# Running and reporting
# --------------------------------------------------------------------------------------


def status(msg: str, final: bool = False):
    width = max(20, shutil.get_terminal_size((80, 20)).columns - 1)
    sys.stdout.write("\r" + msg[:width].ljust(width) + ("\n" if final else ""))
    sys.stdout.flush()


def simulate(rules: Rules, strat: Strategy, runs: int, seed: int, label: str = "") -> list:
    out = []
    step = max(1, runs // 100)
    for i in range(runs):
        g = Game(rules, strat, random.Random(seed * 1_000_003 + i))
        out.append(g.run())
        if label and ((i + 1) % step == 0 or i + 1 == runs):
            status("%s games %d/%d (%d%%)" % (label, i + 1, runs, 100 * (i + 1) // runs), final=(i + 1 == runs))
    return out


def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def pct(xs, p):
    xs = sorted(xs)
    if not xs:
        return 0.0
    return xs[min(len(xs) - 1, int(p / 100 * len(xs)))]


def share(res, pred):
    return 100.0 * sum(1 for r in res if pred(r)) / len(res)


def need_hi(t: str) -> float:
    return 100.0 if t in NEED_HABIT else NEED_SOFT_HI


def need_rates(res: list) -> dict:
    """Share of character-weeks (percent) in which each Need was met."""
    met, seen = Counter(), Counter()
    for r in res:
        met.update(r["need_met"])
        seen.update(r["need_seen"])
    return {t: (100.0 * met[t] / seen[t] if seen[t] else 0.0) for t in TORSOS}


def quit_rate(res: list) -> float:
    """Quits per 100 character-weeks."""
    weeks = sum(v for r in res for k, v in r["parts"].items() if k.startswith("torso|") and k.endswith("|weeks"))
    return 100.0 * sum(r["quits"] for r in res) / weeks if weeks else 0.0


def card_shares(res: list) -> dict:
    """Share of games (percent) that play each action card at least once."""
    return {c: share(res, lambda r, c=c: c in cards_played(r)) for c in ACTION_CARDS}


def all_but_one(res: list) -> float:
    """Share of games (percent) that play all but at most CARD_MISSING_MAX action cards."""
    return share(res, lambda r: len(set(ACTION_CARDS) - cards_played(r)) <= CARD_MISSING_MAX)


def pair_quit_table(res: list, min_weeks: int = 300) -> list:
    """(quits per 100 character-weeks, ratio to the overall rate, quits, character-weeks, name) for every pair of
    habitus parts from two different rows (values, instinct, upbringing), worst first."""
    agg = Counter()
    for r in res:
        agg.update(r["quit_pairs"])
    overall = quit_rate(res) or 1.0
    out = []
    for key in {k.rsplit("|", 1)[0] for k in agg}:
        wks = agg.get(key + "|weeks", 0)
        if wks >= min_weeks:
            q = agg.get(key + "|quits", 0)
            rate = 100.0 * q / wks
            out.append((rate, rate / overall, q, wks, key))
    return sorted(out, reverse=True)


def part_quit_rates(res: list) -> dict:
    """Quits per 100 character-weeks for every habitus card (values, instinct, upbringing), by human name."""
    agg = Counter()
    for r in res:
        agg.update(r["parts"])
    out = {}
    for key in {k.rsplit("|", 1)[0] for k in agg}:
        kind, val = key.split("|")
        if kind in HUMAN_KIND and agg.get(key + "|weeks", 0):
            out["%s %s" % (HUMAN_KIND[kind], val)] = 100.0 * agg.get(key + "|quits", 0) / agg[key + "|weeks"]
    return out


def report(name: str, res: list, rules: Rules):
    n = len(res)
    print("=" * 78)
    print(f"STRATEGY {name}   ({n} games, {rules.players} players, thresholds {res[0]['threshold']} / {res[0]['threshold_high']})")
    print("=" * 78)
    out = Counter(r["outcome"] for r in res)
    print("Outcome:  failure %.0f%%   heroic %.0f%%   sustainable %.0f%%   high performance %.0f%%   mean score %.1f (p10 %d, p90 %d)" % (
        100 * out["failure"] / n, 100 * out["heroic"] / n, 100 * out["sustainable"] / n, 100 * out["thriving"] / n,
        mean(r["score"] for r in res), pct([r["score"] for r in res], 10), pct([r["score"] for r in res], 90)))

    print("\n1. WORK COST")
    done = [r for r in res if r["banked"] == 6]
    print("   features banked: mean %.2f / 6    all six: %.0f%%" % (mean(r["banked"] for r in res), share(res, lambda r: r["banked"] == 6)))
    print("   Work produced %.1f (needed %.0f + %.1f added), per Work card %.2f, wasted cards %.2f, rework lost %.2f" % (
        mean(r["work_out"] for r in res), res[0]["work_needed"], mean(r["cost_added"] for r in res),
        mean(r["work_out"] / r["work_cards"] if r["work_cards"] else 0 for r in res),
        mean(r["work_wasted"] for r in res), mean(r["rework_lost"] for r in res)))
    print("   Work cards per game %.1f of %d days" % (mean(r["work_cards"] for r in res), rules.weeks * rules.days))
    print("   PLAN: each Work card on the planned feature delivers double; extra Work from Plan %.1f a game, Plan laid %.2f times a game" % (
        mean(r["plan_extra_work"] for r in res), mean(sum(d.get("Plan", 0) for d in r["cards_week"]) for r in res)))
    if done:
        print("   last feature banked in week: mean %.1f  (p10 %d, p90 %d)  over the games that finish" % (
            mean(r["last_bank_week"] for r in done), pct([r["last_bank_week"] for r in done], 10), pct([r["last_bank_week"] for r in done], 90)))
    print("   Work output by week: " + "  ".join("w%d %.1f" % (i + 1, mean(r["work_by_week"][i] for r in res)) for i in range(rules.weeks)))
    print("   Ledger at end: Trust %.1f  Capability %.1f  Shared Practice %.1f   lines filled %.1f  stacks %.1f" % (
        mean(r["trust"] for r in res), mean(r["cap"] for r in res), mean(r["sp"] for r in res),
        mean(r["lines_filled"] for r in res), mean(r["stack_flips"] for r in res)))

    print("\n2. ADAPTABILITY")
    print("   tokens earned %.1f   spent %.1f   lost to events %.2f   wasted at the cap %.2f   banked in TR wells %.2f   pool at end %.1f" % (
        mean(r["tokens_earned"] for r in res), mean(r["tokens_spent"] for r in res), mean(r["tokens_lost"] for r in res),
        mean(r["tokens_wasted_cap"] for r in res), mean(r["tokens_banked_tr"] for r in res), mean(r["pool_end"] for r in res)))
    print("   pool at close of week: " + "  ".join("w%d %.1f" % (i + 1, mean(r["pool_week"][i] for r in res)) for i in range(rules.weeks)))
    ways = Counter()
    for r in res:
        ways.update(r["cancel_by"])
    drawn = sum(r["events_drawn"] for r in res)
    cancelled = sum(ways.values())
    print("   Events drawn %.1f/game, cancelled %.1f (%.0f%%): %s" % (
        drawn / n, cancelled / n, 100 * cancelled / drawn if drawn else 0,
        ", ".join("%s %.2f" % (k, v / n) for k, v in sorted(ways.items()))))
    print("   Hero plays %.2f   Wolf: stepped up %.2f, Capital erased %.2f   combos %.2f" % (
        mean(r["hero_plays"] for r in res), mean(r["wolf_up"] for r in res), mean(r["wolf_erased"] for r in res), mean(r["combos"] for r in res)))
    over_flex = sum(1 for r in res if r["max_flex"] > 1)
    print("   FLEX CHECK: most Flex markers held at once: max %d, games above 1: %d of %d%s" % (
        max(r["max_flex"] for r in res), over_flex, n, "  <<< MORE THAN ONE" if over_flex else "  (ok)"))
    hab = Counter()
    wk = defaultdict(list)
    for r in res:
        for k, v in r["habits"].items():
            hab[k] += 1
            wk[k].append(v)
    habit_txt = "   ".join(
        "%s %.0f%% w%.1f" % (k, 100 * hab[k] / n, mean(wk[k])) for k in ("PS", "WKW", "SR", "TR", "AV") if hab[k])
    print("   Habits (share of games, mean week): " + (habit_txt or "none"))
    print("   Teach cards dead (Trust<=1) %.2f   Reflect dead (Trust<3) %.2f" % (
        mean(r["teach_dead"] for r in res), mean(r["reflect_dead"] for r in res)))
    n_reflect = sum(r["reflect_played"] for r in res)
    print("   TEAM REFLEXIVITY CHECK: needs %d Reflect wells (Objectives, Strategies, Processes), one token each, Trust %d+ to Reflect" % (
        rules.tr_wells, rules.reflect_trust))
    print("      reached %.0f%% of games   wells filled %.2f / %d   Reflect played %.2f   Reflect with no evidence %.0f%%   Reflect dead %.2f" % (
        share(res, lambda r: "TR" in r["habits"]), mean(r["tr_wells_filled"] for r in res), rules.tr_wells,
        mean(r["reflect_played"] for r in res), 100 * sum(r["reflect_no_evidence"] for r in res) / n_reflect if n_reflect else 0,
        mean(r["reflect_dead"] for r in res)))
    print("      tokens banked in wells %.2f   tokens the pool got instead (not banking) %.2f   wells skipped while able %.2f" % (
        mean(r["tokens_banked_tr"] for r in res), mean(r["tokens_reflect"] for r in res), mean(r["tr_well_skipped"] for r in res)))
    for k, label in (("OBJ", "objectives"), ("STRAT", "strategy"), ("PROC", "process")):
        print("      %-10s well filled by week (share of games): " % label + "  ".join(
            "w%d %.2f" % (i + 1, mean(r["wells_week"][i][k] for r in res)) for i in range(rules.weeks)))
    chances = mean(r["tr_chances"] for r in res)
    missed = mean(r["tr_missed"] for r in res)
    print("      weeks with evidence for an empty well %.2f a game (needs %d), Reflect not laid in %.2f of them" % (chances, rules.tr_wells, missed))
    reasons = []
    if chances < rules.tr_wells:
        reasons.append("evidence for an empty well showed up in only %.1f weeks a game, fewer than the %d wells (each week needs a banked feature, 2 Events adapted to, or a Hero / token / track drop, and the Reflect comes the week after)" % (chances, rules.tr_wells))
    if missed > 0.3:
        reasons.append("%.1f of those weeks had no free day for a Reflect" % missed)
    if mean(r["reflect_played"] for r in res) < rules.tr_wells:
        reasons.append("only %.1f Reflects a game against %d wells" % (mean(r["reflect_played"] for r in res), rules.tr_wells))
    if reasons:
        print("      WHY NOT: " + "; ".join(reasons) + ".")
    elif share(res, lambda r: "TR" in r["habits"]) < 50:
        print("      WHY NOT: the cards and evidence are there; the wells fill too late in the game to finish.")

    print("\n3. MOTIVATION")
    print("   mean Motivation by week: " + "  ".join("w%d %.2f" % (i + 1, mean(r["mot_mean"][i] for r in res)) for i in range(rules.weeks)))
    print("   lowest Motivation by week: " + "  ".join("w%d %.2f" % (i + 1, mean(r["mot_min"][i] for r in res)) for i in range(rules.weeks)))
    print("   quits per game %.2f   games with a quit %.0f%%   Celebrates %.1f" % (
        mean(r["quits"] for r in res), share(res, lambda r: r["quits"] > 0), mean(r["celebrates"] for r in res)))
    print("   OWN IT (took the blame, team +1 Trust): %.2f a game" % mean(r["own_it"] for r in res))
    print("   SPEAK UP GIFT: %.2f a game, %.2f of them stopping a quit that week (quits without the rescues: at least %.2f a game)" % (
        mean(r["gifts"] for r in res), mean(r["gift_rescues"] for r in res), mean(r["quits"] + r["gift_rescues"] for r in res)))
    print("   median Motivation by week: " + "  ".join("w%d %.2f" % (i + 1, mean(r["mot_med"][i] for r in res)) for i in range(rules.weeks)))
    print("   QUIT CHECK: quits by week: " + "  ".join("w%d %.2f" % (i + 1, mean(r["quit_week"][i] for r in res)) for i in range(rules.weeks))
          + "   games with 0 quits %.0f%%" % share(res, lambda r: r["quits"] == 0))
    qc = Counter()
    for r in res:
        qc.update(r["quit_causes"])
    print("   ONBOARDING: card played %.2f a game, seats left empty %.2f character-weeks a game" % (
        mean(r["onboarding_played"] for r in res), mean(r["empty_seat_weeks"] for r in res)))
    print("   QUIT CAUSES per game (the biggest Motivation loss in the week the character quit): " + (
        "   ".join("%s %.2f" % (k, v / len(res)) for k, v in qc.most_common()) or "none"))
    print("   EARLY EVENTS (weeks 2 to 4, landed a game, share of draws that landed): " + "   ".join(
        "%s %.2f (%.0f%%)" % (n, l, 100 * s) for l, n, _, s in event_early_rows(res)[:8]))
    print("   EVENT QUITS (quits a game where this Event cost the quitter the most; per 100 times it landed): " + "   ".join(
        "%s %.2f (%.1f)" % (n, q, p) for q, n, _, p in event_quit_rows(res)[:6]))
    print("   EVENT x HABITUS (quits a game blamed on the Events of the quit week and the week before):")
    for kind, val, rows in event_habitus_top(res):
        print("      %-6s %-14s" % (kind, val) + "   ".join("%s %.3f" % (n, v) for v, n in rows))
    print("   QUIT RATE (hard goal in optimal: %.0f or less per 100 character-weeks): %.2f  %s" % (
        QUIT_RATE_HARD, quit_rate(res), "ok" if quit_rate(res) <= QUIT_RATE_HARD else "OVER"))
    low = sorted((v, k) for k, v in part_quit_rates(res).items() if v < QUIT_RATE_SOFT_MIN)
    print("   QUIT PAIRS (worst combinations of two habitus parts, quits per 100 character-weeks, vs the overall rate): " + "   ".join(
        "%s %.1f (%.1fx)" % (name, rate, ratio) for rate, ratio, _, _, name in pair_quit_table(res)[:6]))
    print("   QUIT FLOOR (soft goal: every habitus card at least %.2f quit per 100 character-weeks): %s" % (
        QUIT_RATE_SOFT_MIN, "all ok" if not low else "below the floor: " + ", ".join("%s %.2f" % (k, v) for v, k in low)))
    cel_flow = mean(r["mot_flow"].get("celebrate", 0) for r in res)
    print("   CELEBRATE CHECK: played %.1f a game (target 4 or fewer), %.1f of them with nothing to celebrate   more than 4 times in %.0f%% of games   Motivation given %.1f a game   characters skipped by the cap (Motivation above %d) %.1f a game" % (
        mean(r["celebrates"] for r in res), mean(r["celebrate_empty"] for r in res), share(res, lambda r: r["celebrates"] > 4), cel_flow, rules.celebrate_max_mot,
        mean(r["celebrate_capped"] for r in res)))
    print("   QUALITY CHECK: Quality quits per game %.3f, of which after a week without Work %.3f, after 2+ weeks in a row %.3f" % (
        mean(r["quality_quits"] for r in res), mean(r["quality_quit_nowork"] for r in res),
        mean(r["quality_quit_multiweek"] for r in res)))
    print("   weeks without Work per game %.2f, longest run %.2f   (the design goal is 0 Quality quits from this)" % (
        mean(r["no_work_weeks"] for r in res), mean(r["max_no_work_streak"] for r in res)))
    print("   DEADLINE CHECK: THE DATE MOVES UP cost the team a week in %.0f%% of games; of those, the project still finished in %.0f%%" % (
        share(res, lambda r: r["deadline_moved"] > 0),
        100.0 * sum(1 for r in res if r["deadline_moved"] > 0 and r["banked"] == 6) / max(1, sum(1 for r in res if r["deadline_moved"] > 0))))
    agg_dm = Counter()
    for r in res:
        agg_dm.update(r.get("event_stats", {}))
    print("   THE DATE MOVES UP by week (drawn / landed a game): " + "  ".join(
        "w%d %.2f/%.2f" % (i, agg_dm["ev_drawn_w%d|THE DATE MOVES UP" % i] / len(res), agg_dm["ev_landed_w%d|THE DATE MOVES UP" % i] / len(res))
        for i in range(rules.events_from_week, rules.weeks + 1)))
    flow = Counter()
    for r in res:
        flow.update(r["mot_flow"])
    print("   IMMUNITY CHECK: Events spared immune Torsos %.1f Motivation a game (%s); the hit Torso lost %.1f extra" % (
        mean(r["immune_saved"] for r in res),
        ", ".join("%s %.1f" % (t, mean(r["immune_by"][t] for r in res)) for t in ("Autonomy", "Hierarchy", "Community", "Quality")),
        mean(r["hit_extra"] for r in res)))
    print("   Motivation flow per game (all characters): " + ", ".join("%s %+.1f" % (k, v / n) for k, v in sorted(flow.items())))
    need_m, need_s = Counter(), Counter()
    for r in res:
        need_m.update(r["need_met"])
        need_s.update(r["need_seen"])
    print("   Need met rate: " + "  ".join("%s %.0f%%" % (t, 100 * need_m[t] / need_s[t]) for t in TORSOS if need_s[t]))
    print("   NEED CHECK (soft goal: each Need met %d%% to %d%%, %d%% for Needs a Habit meets): " % (NEED_SOFT_LO, NEED_SOFT_HI, 100) + "  ".join(
        "%s %.0f%% %s" % (t, v, "no goal" if t in NEED_NO_GOAL else "ok" if NEED_SOFT_LO <= v <= need_hi(t) else ("TOO EASY" if v > need_hi(t) else "TOO HARD"))
        for t, v in need_rates(res).items()))

    print("\n4. EVENTS AND DAYS (average count per week)")
    W = rules.weeks
    print("   %-17s" % "Events drawn" + "  ".join("w%d %.2f" % (i + 1, mean(r["drawn_week"][i] for r in res)) for i in range(W)))
    print("   %-17s" % "Events cancelled" + "  ".join(
        "w%d %.2f" % (i + 1, mean(sum(r["cancel_week"][i].values()) for r in res)) for i in range(W)))
    for how in names_in(res, "cancel_week", CANCEL_ORDER):
        print("     by %-12s" % how + "  ".join("w%d %.2f" % (i + 1, mean(r["cancel_week"][i].get(how, 0) for r in res)) for i in range(W)))
    for card in shown_days(res):
        label = "Flex marker days" if card == "Flex" else card + " days"
        print("   %-17s" % label + "  ".join("w%d %.2f" % (i + 1, mean(r["cards_week"][i].get(card, 0) for r in res)) for i in range(W)))
    print("   CARD USE CHECK a (goal: %.0f%% of games play all but %d action cards): %.0f%% of games" % (CARD_MISSING_SHARE, CARD_MISSING_MAX, all_but_one(res)))
    print("   CARD USE CHECK b (goal: every action card is played in more than %.0f%% of games): " % CARD_SHARE_MIN + "  ".join(
        "%s %.0f%%%s" % (c, v, "" if v > CARD_SHARE_MIN else " LOW") for c, v in card_shares(res).items()))
    print("   PLAN AND WORKSHOP CHECK (goal: Plan %.1f to %.1f, Workshop %.1f to %.1f times a game): " % (
        PLAY_RANGES["Plan"] + PLAY_RANGES["Workshop"]) + "   ".join(
        "%s %.1f a game, in range in %.0f%% of games" % (c, mean(times_played(r, c) for r in res), share(res, lambda r, c=c: PLAY_RANGES[c][0] <= times_played(r, c) <= PLAY_RANGES[c][1]))
        for c in ("Plan", "Workshop")))
    print("   PLAN RULE CHECK: weeks with 3 or more Work cards on a non-Low feature and no Plan, %.2f a game (should be 0; only Shared Practice 0 allows it)" % mean(r["plan_skipped"] for r in res))
    for key, label in (("hero", "Hero played"), ("dependable", "Dependable Take 1"), ("take_one", "Other Take One"),
                       ("recognition_witness", "Recog. witness"), ("recognition_need_met", "Recog. Need met")):
        print("   %-17s" % label + "  ".join("w%d %.2f" % (i + 1, mean(r["habitus_week"][i][key] for r in res)) for i in range(W)))

    print("\n5. HABITUS PARTS (a character-week = one character at the table for one week)")
    rows = habitus_table(res)
    for kind in ("torso", "legs", "base"):
        part = sorted((x for x in rows if x["kind"] == kind), key=lambda x: -x["quits_per_100_char_weeks"])
        print("   %-7s %-12s %9s %8s %8s %8s %8s" % (kind, "", "quits/100", "vs avg", "mean Mot", "mean Cap", "Hero/100"))
        for x in part:
            flag = "  <- vulnerable" if x["vs_average"] >= 1.25 else "  <- safest" if x["vs_average"] <= 0.75 else ""
            print("   %-7s %-12s %9.2f %8.2f %8.2f %8.2f %8.2f%s" % (
                "", x["value"], x["quits_per_100_char_weeks"], x["vs_average"], x["mean_motivation"],
                x["mean_capital"], x["hero_per_100_char_weeks"], flag))
    print()


def habitus_table(res: list) -> list:
    agg: Counter = Counter()
    for r in res:
        agg.update(r["parts"])
    total_w = sum(agg["torso|%s|weeks" % v] for v in TORSOS)
    total_q = sum(agg["torso|%s|quits" % v] for v in TORSOS)
    overall = 100.0 * total_q / total_w if total_w else 0.0
    rows = []
    for kind, values in (("torso", TORSOS), ("legs", LEGS), ("base", BASES)):
        for v in values:
            wk = agg["%s|%s|weeks" % (kind, v)]
            if not wk:
                continue
            rate = 100.0 * agg["%s|%s|quits" % (kind, v)] / wk
            rows.append({
                "kind": kind, "value": v, "char_weeks": wk, "quits": agg["%s|%s|quits" % (kind, v)],
                "quits_per_100_char_weeks": rate, "vs_average": rate / overall if overall else 0.0,
                "mean_motivation": agg["%s|%s|mot" % (kind, v)] / wk,
                "mean_capital": agg["%s|%s|capital" % (kind, v)] / wk,
                "hero_per_100_char_weeks": 100.0 * agg["%s|%s|hero" % (kind, v)] / wk,
            })
    return rows


def write_habitus_csv(path: str, dump: dict):
    cols = ["run", "kind", "value", "char_weeks", "quits", "quits_per_100_char_weeks", "vs_average",
            "mean_motivation", "mean_capital", "hero_per_100_char_weeks"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        for title, (_, res) in dump.items():
            for x in habitus_table(res):
                wr.writerow([title] + [round(x[c], 3) if isinstance(x[c], float) else x[c] for c in cols[1:]])


def parse_value(old, text: str):
    if isinstance(old, bool):
        return text.lower() in ("1", "true", "yes", "on")
    if isinstance(old, int):
        return int(text)
    if isinstance(old, str):
        return text
    return float(text)


def apply_overrides(rules: Rules, pairs: list) -> Rules:
    names = {f.name for f in fields(Rules)}
    kw = {}
    for p in pairs:
        k, _, v = p.partition("=")
        if k not in names:
            sys.exit("unknown rule %r; choose from: %s" % (k, ", ".join(sorted(names))))
        kw[k] = parse_value(getattr(rules, k), v)
    return replace(rules, **kw)


COUNTER_FIELDS = ("cancel_by", "mot_flow", "need_met", "need_seen", "cancel_week", "cards_week", "habitus_week", "habit_week", "parts",
                  "wells_week", "evidence_week", "quit_causes", "quit_who", "quit_pairs", "event_stats")


def flatten(r: dict) -> dict:
    row = {}
    for k, v in r.items():
        if k == "event_habitus":
            continue
        if isinstance(v, list):
            for i, x in enumerate(v):
                if isinstance(x, dict):
                    for kk, y in x.items():
                        row["%s_w%d_%s" % (k, i + 1, kk)] = y
                else:
                    row["%s_w%d" % (k, i + 1)] = x
        elif isinstance(v, dict):
            for kk, x in v.items():
                row["%s_%s" % (k, kk)] = x
        else:
            row[k] = v
    return row


def write_csv(path: str, dump: dict):
    rows = []
    for title, (rules, res) in dump.items():
        for i, r in enumerate(res):
            rows.append({"run": title, "game": i + 1, "players": rules.players, **flatten(r)})
    cols = []
    for row in rows:
        for k in row:
            if k not in cols:
                cols.append(k)

    def blank(col):
        return 0 if col.startswith(tuple(f + "_" for f in COUNTER_FIELDS)) else ""

    with open(path, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        for row in rows:
            wr.writerow([row.get(c, blank(c)) for c in cols])

    base, ext = os.path.splitext(path)
    summary = base + "_summary" + (ext or ".csv")
    nums = [c for c in cols if c not in ("run", "game", "outcome")]
    with open(summary, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["run", "games", "failure_pct", "heroic_pct", "sustainable_pct", "high_performance_pct"] + nums)
        for title in dump:
            mine = [r for r in rows if r["run"] == title]
            n = len(mine)
            line = [title, n] + [round(100 * sum(1 for r in mine if r["outcome"] == o) / n, 1)
                                 for o in ("failure", "heroic", "sustainable", "thriving")]
            for c in nums:
                vals = [r.get(c, blank(c)) for r in mine]
                vals = [v for v in vals if isinstance(v, (int, float))]
                line.append(round(sum(vals) / len(vals), 3) if vals else "")
            wr.writerow(line)
    return summary


# --------------------------------------------------------------------------------------
# Optimal play: coordinate-ascent search over the Strategy parameters
# --------------------------------------------------------------------------------------


def cards_played(r: dict) -> set:
    return {c for week in r["cards_week"] for c, n in week.items() if n}


def shown_cards(res: list) -> list:
    """Every action card, played or not, then Onboarding if it was laid. Flex is a marker, not a card."""
    return ACTION_CARDS + [c for c in names_in(res, "cards_week", CARD_ORDER) if c not in ACTION_CARDS and c != "Flex"]


def shown_days(res: list) -> list:
    """What fills the five days: the cards, then the Flex marker if one was laid."""
    return shown_cards(res) + [c for c in names_in(res, "cards_week", CARD_ORDER) if c == "Flex"]


def day_label(name: str) -> str:
    return "Flex marker (not a card)" if name == "Flex" else name


def times_played(r: dict, card: str) -> int:
    return int(sum(week.get(card, 0) for week in r["cards_week"]))


def objective(res: list) -> float:
    # Priorities: no quits (QUIT_WEIGHT each), then every feature delivered (FINISH_WEIGHT), then points: the share reaching
    # the upper threshold plus 2 per point of mean score (a Habit is 12 points, so worth 24). Also minus 100 for each
    # Quality quit after a week without Work, 60 for each action card a game leaves unplayed beyond the one it may skip,
    # 4 for each percent an action card falls short of being played in half the games,
    # and 30 for each play of Plan or Workshop short of 1.3 or over 2.5.
    missing = mean(max(0, len(set(ACTION_CARDS) - cards_played(r)) - CARD_MISSING_MAX) for r in res)
    off = mean(max(0, PLAY_RANGES[c][0] - times_played(r, c)) + max(0, times_played(r, c) - PLAY_RANGES[c][1]) for r in res for c in PLAY_RANGES) * 2
    need_off = sum(max(0.0, NEED_SOFT_LO - v) + max(0.0, v - need_hi(t)) for t, v in need_rates(res).items() if t not in NEED_NO_GOAL)
    return (share(res, lambda r: r["outcome"] == "thriving") + 2.0 * mean(r["score"] for r in res)
            + FINISH_WEIGHT * share(res, lambda r: r["banked"] == 6) - 100 * mean(r["quality_quit_nowork"] for r in res) - 60 * missing - 30 * off
            - 4.0 * sum(max(0.0, CARD_SHARE_MIN - v) for v in card_shares(res).values())
            - 6.0 * share(res, lambda r: r["score"] == 0)
            - QUIT_WEIGHT * mean(r["quits"] for r in res) - 500 * max(0.0, quit_rate(res) - QUIT_RATE_HARD) - 0.2 * need_off
            - 3 * max(0.0, 50 - share(res, lambda r: "PS" in r["habits"]))
            - 0.5 * sum(max(0.0, QUIT_RATE_SOFT_MIN - v) for v in part_quit_rates(res).values()))


OPT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "balance_sim_optimal.json")


def load_optimal(weeks: int) -> Strategy | None:
    try:
        with open(OPT_FILE, encoding="utf-8") as fh:
            d = json.load(fh)
        d["work_days"] = (tuple(d["work_days"]) + (d["work_days"][-1],) * weeks)[:weeks]
        d["overtime_weeks"] = tuple(d.get("overtime_weeks", ()))
        d["plan_weeks"] = tuple(d.get("plan_weeks", ()))
        d["workshop_weeks"] = tuple(d.get("workshop_weeks", ()))
        names = {f.name for f in fields(Strategy)}
        return Strategy(**{k: v for k, v in d.items() if k in names})
    except (OSError, ValueError, KeyError, TypeError, IndexError):
        return None


def optimise(rules: Rules, runs: int, passes: int, seed: int, label: str = "", log: list | None = None,
             reuse: bool = False) -> Strategy:
    W = rules.weeks
    saved = load_optimal(W)
    if reuse and saved is not None:
        if log is not None:
            log.append("OPTIMAL SEARCH skipped (--reuse-optimal), strategy from %s\n  %s\n" % (os.path.basename(OPT_FILE), saved))
        return saved

    def fit(t):
        return (tuple(t) + (t[-1],) * W)[:W]

    best = Strategy("optimal", work_days=(3,) * W, celebrate_needs_reason=True)
    cache: dict = {}

    def value(st: Strategy) -> float:
        key = repr(st)
        if key not in cache:
            cache[key] = objective(simulate(rules, st, runs, seed))
        return cache[key]

    choices = {
        "trust_goal": [0, 1, 2, 3, 4, 5], "celebrate_min": [0, 1, 2, 3],
        "celebrate_mean": [0.0, 1.5, 2.0, 2.5, 3.0, 3.5], "celebrate_every": [0, 2, 3, 4],
        "pool_goal": [0, 2, 3, 4, 5, 6], "learn": [0, 1, 2, 3],
        "reflect": [True, False], "plan": [True, False], "demo": [True, False],
        "adapt_threshold": [0.3, 0.5, 0.7, 0.8, 1.0, 1.5, 99.0], "hero_min_cost": [1, 2, 3],
        "bank_tokens": [True, False], "wolf": ["always", "never", "if_mot"],
        "take_one": [True, False], "repay_flex": [True, False],
        "use_stand": [True, False], "celebrate_needs_reason": [True, False], "care": [True, False], "care_at": [1, 2, 3], "finish_first": [True, False],
    }
    groups = [lambda b, k=k, vs=vs: [replace(b, **{k: v}) for v in vs] for k, vs in choices.items()]
    groups += [lambda b, i=i: [replace(b, work_days=b.work_days[:i] + (d,) + b.work_days[i + 1:]) for d in range(6)]
               for i in range(W)]
    groups += [lambda b, i=i: [replace(b, overtime_weeks=tuple(sorted(set(b.overtime_weeks) ^ {i + 1})))]
               for i in range(W)]
    groups += [lambda b, i=i: [replace(b, plan_weeks=tuple(sorted(set(b.plan_weeks) ^ {i + 1})))]
               for i in range(W)]
    # One flip at a time cannot reach "Plan twice" or "Workshop twice" (one more play alone does not pay), so try whole sets
    groups += [lambda b, i=i: [replace(b, workshop_weeks=tuple(sorted(set(b.workshop_weeks) ^ {i + 1})))]
               for i in range(W)]
    groups += [lambda b: [replace(b, workshop_weeks=c) for n in (1, 2) for c in combinations(range(rules.workshop_from_week, W + 1), n)]]
    groups += [lambda b: [replace(b, plan_weeks=c) for n in (1, 2) for c in combinations(range(rules.plan_from_week, W + 1), n)]]

    best_v = value(best)
    seeds = [best, replace(best, plan=True),
             replace(STRATEGIES["invested"], name="optimal", work_days=fit(STRATEGIES["invested"].work_days),
                     celebrate_needs_reason=True),
             Strategy("optimal", work_days=fit((5, 5, 0, 0, 0, 4, 3, 4)), trust_goal=4, celebrate_min=2, celebrate_mean=3.5,
                      pool_goal=2, learn=2, plan=False, overtime_weeks=(5,), adapt_threshold=0.5, hero_min_cost=1,
                      bank_tokens=False, wolf="never", celebrate_needs_reason=True)]
    if saved is not None:
        seeds.append(replace(saved, celebrate_needs_reason=True))
        seeds.append(replace(saved, celebrate_needs_reason=True, care=True, care_at=3, finish_first=True))
    best_v, best = max(((value(s), s) for s in seeds), key=lambda t: t[0])
    for p in range(1, passes + 1):
        improved = False
        for gi, g in enumerate(groups, 1):
            for cand in g(best):
                v = value(cand)
                if v > best_v + 1e-9:
                    best, best_v, improved = cand, v, True
            status("%s search %d/%d (%d%%) obj %.1f" % (
                label, (p - 1) * len(groups) + gi, passes * len(groups),
                100 * ((p - 1) * len(groups) + gi) // (passes * len(groups)), best_v))
        if not improved:
            break
    status("%s search done, obj %.1f" % (label, best_v), final=True)
    try:
        with open(OPT_FILE, "w", encoding="utf-8") as fh:
            json.dump(asdict(best), fh)
    except OSError:
        pass
    if log is not None:
        log.append("OPTIMAL SEARCH (%s): %d games per candidate, objective %.1f\n  %s\n" % (label, runs, best_v, best))
    return best


# --------------------------------------------------------------------------------------
# SVG plots (standard library only): three panels per strategy, weeks on x, average count on y
# --------------------------------------------------------------------------------------

# The game's own colours (board-game-boards canon); pastel, so lines get a dark outline
C_TRUST, C_CAP, C_SP, C_ADAPT, C_MOT, C_HABITUS = "#D3CEDF", "#C7CFB5", "#F7D7A1", "#B5C7CF", "#D3B1B1", "#E8D4B8"
INK = "#2A2620"

CARD_ORDER = ["Work", "Celebrate", "Engagement", "Workshop", "Learn", "Teach", "Reflect", "Plan", "Demo", "Onboarding", "Flex"]
ACTION_CARDS = [c for c in CARD_ORDER if c not in ("Flex", "Onboarding")]
CARD_COLOUR = {"Work": "#6B7A8F", "Onboarding": "#A39A8B", "Celebrate": "#E3A72F", "Engagement": "#4C9F70", "Refine": "#2F80ED",
               "Workshop": "#7AB8F5", "Learn": "#9B51E0", "Teach": "#C9A0F0", "Reflect": "#F2994A",
               "Plan": "#56CCF2", "Demo": "#EB5757", "Flex": "#333333"}
CANCEL_ORDER = ["free", "habit", "token", "hero", "stand", "trust", "av"]
CANCEL_COLOUR = {"free": "#9AD1A8", "habit": "#63E6BE", "token": C_ADAPT, "hero": "#E3A72F", "stand": "#E8590C",
                 "trust": C_TRUST, "av": "#9B51E0"}
FALLBACK_COLOURS = ["#888888", "#BB6BD9", "#219653", "#F2C94C"]


def names_in(res: list, key: str, order: list) -> list:
    seen = {k for r in res for d in r[key] for k in d}
    return [k for k in order if k in seen] + sorted(seen - set(order))


def week_mean(res: list, key: str, weeks: int) -> list:
    return [mean(r[key][i] for r in res) for i in range(weeks)]


def week_mean_of(res: list, key: str, name: str, weeks: int) -> list:
    return [mean(r[key][i].get(name, 0) for r in res) for i in range(weeks)]


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;")


def _nice_max(v: float) -> float:
    for m in (2, 3, 4, 5, 6, 8, 10, 12, 15, 20):
        if v <= m:
            return m
    return math.ceil(v / 5) * 5


def _pastel(col: str) -> bool:
    try:
        r, g, b = int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16)
    except ValueError:
        return False
    return 0.299 * r + 0.587 * g + 0.114 * b > 170


class _Panel:
    def __init__(self, x, y, w, h, ymax, weeks):
        self.x, self.y, self.w, self.h, self.ymax, self.weeks = x, y, w, h, ymax, weeks

    def px(self, i):
        return self.x + (i + 0.5) * self.w / self.weeks

    def py(self, v):
        return self.y + self.h - v / self.ymax * self.h


def _frame(out: list, p: _Panel, title: str, ylabel: str):
    out.append('<text x="%g" y="%g" class="t">%s</text>' % (p.x, p.y - 14, _esc(title)))
    step = 0.25 if p.ymax <= 1 else 1 if p.ymax <= 8 else 2 if p.ymax <= 16 else 5
    v = 0
    while v <= p.ymax + 1e-9:
        y = p.py(v)
        out.append('<line x1="%g" y1="%.1f" x2="%g" y2="%.1f" class="g"/>' % (p.x, y, p.x + p.w, y))
        out.append('<text x="%g" y="%.1f" class="a" text-anchor="end">%g</text>' % (p.x - 6, y + 3.5, v))
        v += step
    for i in range(p.weeks):
        out.append('<text x="%.1f" y="%g" class="a" text-anchor="middle">%d</text>' % (p.px(i), p.y + p.h + 14, i + 1))
    out.append('<text x="%g" y="%g" class="a" text-anchor="middle">week</text>' % (p.x + p.w / 2, p.y + p.h + 30))
    out.append('<text transform="translate(%g,%g) rotate(-90)" class="a" text-anchor="middle">%s</text>' % (
        p.x - 34, p.y + p.h / 2, _esc(ylabel)))


def _legend(out: list, p: _Panel, items: list):
    x = p.x + p.w + 16
    for j, (label, col, kind) in enumerate(items):
        y = p.y + 10 + j * 17
        if kind == "bar":
            out.append('<rect x="%g" y="%g" width="12" height="10" fill="%s"/>' % (x, y - 8, col))
        else:
            dash = ' stroke-dasharray="4 3"' if kind == "dash" else ""
            if _pastel(col):
                out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="4.6"%s/>' % (x, y - 3, x + 12, y - 3, INK, dash))
            out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2.2"%s/>' % (x, y - 3, x + 12, y - 3, col, dash))
        out.append('<text x="%g" y="%g" class="a">%s</text>' % (x + 18, y, _esc(label)))


def _lines(out: list, p: _Panel, series: list):
    for _, col, vals, dash in series:
        pts = " ".join("%.1f,%.1f" % (p.px(i), p.py(v)) for i, v in enumerate(vals))
        pale = _pastel(col)
        if pale:
            out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="4.6"%s/>' % (
                pts, INK, ' stroke-dasharray="4 3"' if dash else ""))
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2"%s/>' % (
            pts, col, ' stroke-dasharray="4 3"' if dash else ""))
        for i, v in enumerate(vals):
            out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"%s/>' % (
                p.px(i), p.py(v), col, ' stroke="%s" stroke-width="1"' % INK if pale else ""))


def _stack(out: list, p: _Panel, layers: list):
    bw = p.w / p.weeks * 0.6
    base = [0.0] * p.weeks
    for _, col, vals in layers:
        for i, v in enumerate(vals):
            if v <= 0.005:
                continue
            y1, y0 = p.py(base[i] + v), p.py(base[i])
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (p.px(i) - bw / 2, y1, bw, y0 - y1, col))
            base[i] += v
    return base


def plot_strategy(path: str, title: str, res: list, rules: Rules):
    W = rules.weeks
    X0, PW, PH, GAP, TOP = 64, 620, 200, 86, 56
    out = []

    # 1. currencies
    lines = [
        ("Motivation (mean per character)", C_MOT, week_mean(res, "mot_mean", W), False),
        ("Capital (mean per character)", C_HABITUS, week_mean(res, "capital_week", W), False),
        ("Adaptability pool (tokens)", C_ADAPT, week_mean(res, "pool_week", W), False),
        ("Features banked", "#212529", week_mean(res, "banked_week", W), False),
    ]
    p1 = _Panel(X0, TOP, PW, PH, _nice_max(max(max(s[2]) for s in lines)), W)
    _frame(out, p1, "1. Currencies at the close of each week", "average count")
    _lines(out, p1, lines)
    _legend(out, p1, [(s[0], s[1], "dash" if s[3] else "line") for s in lines])

    # 1b. the Ledger and Habits held
    held = [mean(len(r["habit_week"][i]) for r in res) for i in range(W)]
    ledger = [
        ("Trust", C_TRUST, week_mean(res, "trust_week", W), False),
        ("Capability", C_CAP, week_mean(res, "cap_week", W), False),
        ("Shared Practice", C_SP, week_mean(res, "sp_week", W), False),
        ("Standing (highest Capital)", "#868E96", week_mean(res, "standing_week", W), False),
        ("Habits held (0-5)", "#B03A2E", held, True),
        ("Habit threshold (%d)" % rules.habit_at, "#AAAAAA", [float(rules.habit_at)] * W, True),
    ]
    yl = TOP + PH + GAP
    pl = _Panel(X0, yl, PW, PH, 5, W)
    _frame(out, pl, "2. The Ledger and Habits held, at the close of each week", "track value / count")
    _lines(out, pl, ledger)
    _legend(out, pl, [(s[0], s[1], "dash" if s[3] else "line") for s in ledger])

    # 1c. which Habits, share of games
    names = [("PS", "Psychological Safety", C_TRUST), ("WKW", "Who Knows What", C_CAP),
             ("SR", "Shared Repertoire", C_SP), ("TR", "Team Reflexivity", C_ADAPT),
             ("AV", "Authorized Voice", "#868E96")]
    habit_share = [(label, col, [mean(r["habit_week"][i].get(k, 0) for r in res) for i in range(W)], False)
             for k, label, col in names]
    yh = yl + PH + GAP
    ph = _Panel(X0, yh, PW, PH, 1, W)
    _frame(out, ph, "3. Habits formed: share of games holding each, per week", "share of games")
    _lines(out, ph, habit_share)
    _legend(out, ph, [(s[0], s[1], "line") for s in habit_share])

    # 2. Events cancelled, by how
    base_ways = ["free", "token", "hero", "av"]
    hows = base_ways + [h for h in names_in(res, "cancel_week", CANCEL_ORDER) if h not in base_ways]
    labels = {"free": "Habit discount (cost 0)", "token": "Adaptability tokens", "hero": "Hero (Legs, 3+ Motivation)",
              "trust": "Trust 4+ (one a week)", "av": "AV = Authorized Voice (one a week)",
              "stand": "Torso Stand (optional)", "habit": "Habit cancel (optional)"}
    layers = [(labels.get(h, h), CANCEL_COLOUR.get(h, FALLBACK_COLOURS[j % 4]), week_mean_of(res, "cancel_week", h, W)) for j, h in enumerate(hows)]
    y2 = yh + PH + GAP
    tot = [sum(l[2][i] for l in layers) for i in range(W)]
    p2 = _Panel(X0, y2, PW, PH, _nice_max(max(tot + [2])), W)
    _frame(out, p2, "4. Events cancelled per week, by how (two are drawn each week from week 2)", "average count")
    _stack(out, p2, layers)
    _legend(out, p2, [(l[0], l[1], "bar") for l in layers])

    # 3. The five days
    cards = shown_days(res)
    layers = [(day_label(c), CARD_COLOUR.get(c, "#999999"), week_mean_of(res, "cards_week", c, W)) for c in cards]
    y3 = y2 + PH + GAP
    tot = [sum(l[2][i] for l in layers) for i in range(W)]
    p3 = _Panel(X0, y3, PW, PH, _nice_max(max(tot + [rules.days])), W)
    _frame(out, p3, "5. How the five days are played, per week", "average days")
    _stack(out, p3, layers)
    _legend(out, p3, [(l[0], l[1], "bar") for l in reversed(layers)])

    # 4. Habitus moves: Hero, Dependable (Take One), Recognition
    hab = [
        ("Hero played", "#E3A72F", week_mean_of(res, "habitus_week", "hero", W), False),
        ("Dependable: Take One For The Team", "#2B8A3E", week_mean_of(res, "habitus_week", "dependable", W), False),
        ("Recognition: witness gets +1 Motivation", "#D6336C", week_mean_of(res, "habitus_week", "recognition_witness", W), False),
        ("Recognition: Need met (characters)", "#F783AC", week_mean_of(res, "habitus_week", "recognition_need_met", W), True),
    ]
    y4 = y3 + PH + GAP
    p4 = _Panel(X0, y4, PW, PH, _nice_max(max(max(s[2]) for s in hab) or 1), W)
    _frame(out, p4, "6. Habitus moves per week: Hero, Dependable and Recognition", "average count")
    _lines(out, p4, hab)
    _legend(out, p4, [(s[0], s[1], "dash" if s[3] else "line") for s in hab])

    # 7. Team Score histogram with the threshold
    y5 = y4 + PH + GAP
    scores = [r["score"] for r in res]
    thr = res[0]["threshold"]
    thr2 = res[0]["threshold_high"]
    bin_w = 5
    lo = int(min(min(scores), thr) // bin_w * bin_w - bin_w)
    hi = int((max(max(scores), thr2) // bin_w + 2) * bin_w)
    nb = (hi - lo) // bin_w
    counts = [0] * nb
    for s in scores:
        counts[min(nb - 1, int((s - lo) // bin_w))] += 1
    hmax = _nice_max(max(counts))
    hx = lambda v: X0 + (v - lo) / (hi - lo) * PW
    hy = lambda c: y5 + PH - c / hmax * PH
    out.append('<text x="%g" y="%g" class="t">7. Team Score distribution: number of games per score</text>' % (X0, y5 - 14))
    ystep = 1 if hmax <= 8 else 2 if hmax <= 16 else 5 if hmax <= 40 else 10 if hmax <= 100 else 20 if hmax <= 200 else 50 if hmax <= 500 else 100
    v = 0
    while v <= hmax:
        out.append('<line x1="%g" y1="%.1f" x2="%g" y2="%.1f" class="g"/>' % (X0, hy(v), X0 + PW, hy(v)))
        out.append('<text x="%g" y="%.1f" class="a" text-anchor="end">%g</text>' % (X0 - 6, hy(v) + 3.5, v))
        v += ystep
    xstep = 10 if hi - lo <= 160 else 20
    t = (lo // xstep + 1) * xstep
    while t < hi:
        out.append('<text x="%.1f" y="%g" class="a" text-anchor="middle">%d</text>' % (hx(t), y5 + PH + 14, t))
        t += xstep
    out.append('<text x="%g" y="%g" class="a" text-anchor="middle">Team Score (points)</text>' % (X0 + PW / 2, y5 + PH + 30))
    out.append('<text transform="translate(%g,%g) rotate(-90)" class="a" text-anchor="middle">number of games</text>' % (X0 - 40, y5 + PH / 2))
    for i, c in enumerate(counts):
        if c:
            below = lo + (i + 1) * bin_w <= thr
            high = lo + i * bin_w >= thr2
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (
                hx(lo + i * bin_w) + .5, hy(c), PW / nb - 1, y5 + PH - hy(c), "#6B7A8F" if below else "#1F7A4D" if high else "#4C9F70"))
    avg = statistics.mean(scores)
    out.append('<line x1="%.1f" y1="%g" x2="%.1f" y2="%g" stroke="#212529" stroke-width="1.4" stroke-dasharray="1.5 2.5"/>' % (hx(avg), y5, hx(avg), y5 + PH))
    out.append('<line x1="%.1f" y1="%g" x2="%.1f" y2="%g" stroke="#C92A2A" stroke-width="1.8" stroke-dasharray="6 3"/>' % (hx(thr), y5, hx(thr), y5 + PH))
    out.append('<line x1="%.1f" y1="%g" x2="%.1f" y2="%g" stroke="#C92A2A" stroke-width="1.8" stroke-dasharray="6 3"/>' % (hx(thr2), y5, hx(thr2), y5 + PH))
    lx = X0 + PW + 16
    out.append('<rect x="%g" y="%g" width="12" height="10" fill="#6B7A8F"/><text x="%g" y="%g" class="a">below the lower threshold</text>' % (lx, y5 + 2, lx + 18, y5 + 10))
    out.append('<rect x="%g" y="%g" width="12" height="10" fill="#4C9F70"/><text x="%g" y="%g" class="a">between the two thresholds</text>' % (lx, y5 + 19, lx + 18, y5 + 27))
    out.append('<rect x="%g" y="%g" width="12" height="10" fill="#1F7A4D"/><text x="%g" y="%g" class="a">at or above the high threshold</text>' % (lx, y5 + 36, lx + 18, y5 + 44))
    out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#C92A2A" stroke-width="1.8" stroke-dasharray="6 3"/><text x="%g" y="%g" class="a">thresholds (%d and %d)</text>' % (lx, y5 + 58, lx + 12, y5 + 58, lx + 18, y5 + 61, thr, thr2))
    out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#212529" stroke-width="1.4" stroke-dasharray="1.5 2.5"/><text x="%g" y="%g" class="a">mean score (%.1f)</text>' % (lx, y5 + 75, lx + 12, y5 + 75, lx + 18, y5 + 78, avg))
    out.append('<text x="%g" y="%g" class="a">%d%% reach %d, %d%% reach %d</text>' % (lx, y5 + 97, round(100 * sum(1 for s in scores if s >= thr) / len(scores)), thr, round(100 * sum(1 for s in scores if s >= thr2) / len(scores)), thr2))

    # 8. Team Reflexivity progress: wells filled, evidence on offer, Reflect cards played
    yt = y5 + PH + GAP
    wl = [("OBJ", "Objectives", "#2B8A3E"), ("STRAT", "Strategy", "#7048E8"), ("PROC", "Process", "#F2994A")]
    tr_lines = []
    for k, label, col in wl:
        tr_lines.append(("%s well filled" % label, col, [mean(r["wells_week"][i][k] for r in res) for i in range(W)], False))
    for k, label, col in wl:
        ev_key = {"OBJ": "banked", "STRAT": "adapted2", "PROC": "process"}[k]
        tr_lines.append(("%s evidence on offer" % label, col, [mean(r["evidence_week"][i][ev_key] for r in res) for i in range(W)], True))
    tr_lines.append(("Team Reflexivity held", C_ADAPT, [mean(1 if "TR" in r["habit_week"][i] else 0 for r in res) for i in range(W)], False))
    ptr = _Panel(X0, yt, PW, PH, 1, W)
    _frame(out, ptr, "8. Team Reflexivity: share of games with each well filled, evidence on offer, and the Habit held", "share of games")
    _lines(out, ptr, tr_lines)
    _legend(out, ptr, [(s[0], s[1], "dash" if s[3] else "line") for s in tr_lines])

    # 8b. Motivation spread: characters at each level at the close of each week, and quits
    ym = yt + PH + GAP
    lv_cols = ["#C92A2A", "#E8590C", "#F59F00", "#C0D24A", "#69B578", "#1F7A4D"]
    pm = _Panel(X0, ym, PW, PH, rules.players, W)
    _frame(out, pm, "9. Motivation: characters at each level at the close of each week, and quits that week", "characters (average)")
    layers = [("Motivation %d" % v, lv_cols[min(v, 5)], [mean(r["mot_hist"][i][v] if v < len(r["mot_hist"][i]) else 0 for r in res) for i in range(W)])
              for v in range(rules.mot_cap + 1)]
    _stack(out, pm, layers)
    quit_line = [("Quits that week", INK, [mean(r["quit_week"][i] for r in res) for i in range(W)], True)]
    _lines(out, pm, quit_line)
    _legend(out, pm, [(l[0], l[1], "bar") for l in layers] + [(quit_line[0][0], INK, "dash")])

    # 9b. Motivation: lowest, mean and median per week, and quits
    yq = ym + PH + GAP
    mq = [("Lowest Motivation", "#C92A2A", week_mean(res, "mot_min", W), False),
          ("Mean Motivation", "#1F7A4D", week_mean(res, "mot_mean", W), False),
          ("Median Motivation", "#1971C2", week_mean(res, "mot_med", W), True),
          ("Quits that week", INK, [mean(r["quit_week"][i] for r in res) for i in range(W)], True)]
    pq = _Panel(X0, yq, PW, PH, rules.mot_cap, W)
    _frame(out, pq, "10. Motivation per week: lowest, mean, median, and quits (goal in optimal play: 0 quits)", "Motivation / quits")
    _lines(out, pq, mq)
    _legend(out, pq, [(s[0], s[1], "dash" if s[3] else "line") for s in mq])

    # 11. Who quits when
    yw = yq + PH + GAP
    yw_end = _heat(out, X0, yw, PW, "11. Who quits when: average quits a game, by habitus card and week", quit_who_rows(res, W), W)

    # 12. Table: cards played, average per game, by week
    y6 = yw_end + GAP
    rows = shown_cards(res)
    rh, cw = 20, 64
    out.append('<text x="%g" y="%g" class="t">12. Cards played: average per game, by week</text>' % (X0, y6 - 14))
    cols = ["card"] + ["w%d" % (i + 1) for i in range(W)] + ["per game", "% of games"]
    xs = [X0] + [X0 + 130 + i * cw for i in range(W)] + [X0 + 130 + W * cw + 10, X0 + 130 + W * cw + 110]
    out.append('<rect x="%g" y="%g" width="%g" height="%g" fill="#f1f3f5"/>' % (X0 - 6, y6 - 2, xs[-1] + 140 - X0, rh))
    for x, c in zip(xs, cols):
        out.append('<text x="%g" y="%g" class="t" text-anchor="%s">%s</text>' % (x if c == "card" else x + (cw - 14 if c.startswith("w") else 60), y6 + 13, "start" if c == "card" else "end", c))
    tot_w = [0.0] * W
    for ri, card in enumerate(rows):
        y = y6 + (ri + 1) * rh
        per_week = week_mean_of(res, "cards_week", card, W)
        per_game = sum(per_week)
        played = share(res, lambda r, c=card: sum(d.get(c, 0) for d in r["cards_week"]) > 0)
        if ri % 2:
            out.append('<rect x="%g" y="%g" width="%g" height="%g" fill="#f8f9fa"/>' % (X0 - 6, y - 2, xs[-1] + 140 - X0, rh))
        out.append('<rect x="%g" y="%g" width="10" height="10" fill="%s"/>' % (X0, y + 3, CARD_COLOUR.get(card, "#999999")))
        out.append('<text x="%g" y="%g" class="a">%s</text>' % (X0 + 16, y + 13, card))
        for i, v in enumerate(per_week):
            tot_w[i] += v
            out.append('<text x="%g" y="%g" class="a" text-anchor="end">%s</text>' % (xs[i + 1] + cw - 14, y + 13, "%.2f" % v if v else "-"))
        out.append('<text x="%g" y="%g" class="t" text-anchor="end">%.1f</text>' % (xs[W + 1] + 60, y + 13, per_game))
        out.append('<text x="%g" y="%g" class="a" text-anchor="end">%.0f%%</text>' % (xs[W + 2] + 60, y + 13, played))
    y = y6 + (len(rows) + 1) * rh
    out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" class="g"/>' % (X0 - 6, y - 2, xs[-1] + 134, y - 2))
    out.append('<text x="%g" y="%g" class="t">all cards</text>' % (X0 + 16, y + 13))
    for i, v in enumerate(tot_w):
        out.append('<text x="%g" y="%g" class="t" text-anchor="end">%.2f</text>' % (xs[i + 1] + cw - 14, y + 13, v))
    out.append('<text x="%g" y="%g" class="t" text-anchor="end">%.1f</text>' % (xs[W + 1] + 60, y + 13, sum(tot_w)))

    width, height = max(X0 + PW + 260, int(xs[-1]) + 150), y + 50
    head = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
            '<style>.t{font:bold 13px sans-serif;fill:#111}.a{font:11px sans-serif;fill:#444}.g{stroke:#ddd;stroke-width:1}</style>'
            '<rect width="100%%" height="100%%" fill="#fff"/>'
            '<text x="%d" y="26" style="font:bold 16px sans-serif">%s  (%d games, %d players, %d weeks)</text>') % (
        width, height, width, height, X0, _esc(title), len(res), rules.players, W)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(head + "".join(out) + "</svg>\n")


def calibrate(dump: dict):
    """Upper threshold: UPPER_GOAL percent of optimal play reach it. Lower threshold: balanced/invested reach it in half of their games."""
    series = {t: res for t, (_, res) in dump.items()}
    rnd = [n for n in ("random", "hero") if n in series]
    reasonable = [n for n in ("balanced", "invested") if n in series]
    if "optimal" not in series or not (rnd or reasonable):
        return "", [], ""
    rules = dump["optimal"][0]
    names = list(series)

    def reach(res, t):
        return sum(1 for r in res if r["banked"] == 6 and r["score"] >= t) / len(res)

    lo = min(r["score"] for res in series.values() for r in res) - 1
    hi = max(r["score"] for res in series.values() for r in res) + 1
    rows = [[t] + [round(100 * reach(series[n], t), 1) for n in names] for t in range(lo, hi + 1)]
    opt = series["optimal"]
    all_six = 100 * sum(1 for r in opt if r["banked"] == 6) / len(opt)
    ok = [t for t in range(lo, hi + 1) if reach(opt, t) >= UPPER_GOAL / 100]
    top = max(ok) if ok else None
    # lowest score where every 'almost never' strategy is at 2% or less
    # random never banks all six features, so its 'reach' is always 0: judge it on the score alone
    never = [min([t for t in range(lo, hi + 1) if sum(1 for r in series[n] if r["score"] >= t) / len(series[n]) <= 0.02] or [hi]) for n in rnd]
    low = max(never) if never else lo
    often_ok = [t for t in range(lo, hi + 1) if reasonable and all(reach(series[n], t) >= 0.5 for n in reasonable)]
    often = max(often_ok) if often_ok else None
    cur = rules.threshold_base + rules.threshold_per_player * rules.players
    cur2 = rules.threshold_high_base + rules.threshold_per_player * rules.players
    if not rnd:
        low = cur
    per = rules.threshold_per_player * rules.players
    lines = ["THRESHOLD CALIBRATION (goals: optimal play reaches the UPPER threshold in %.0f%% of games; balanced/invested play reaches the LOWER threshold in 50%% or more)." % UPPER_GOAL,
             "'reach' = all six features banked AND Team Score at or above the threshold).",
             "Current thresholds: %d (%d + %d x %d players) and %d (%d + %d x %d)."
             % (cur, rules.threshold_base, rules.threshold_per_player, rules.players,
                cur2, rules.threshold_high_base, rules.threshold_per_player, rules.players)]
    for n in names:
        sc = sorted(r["score"] for r in series[n])
        lines.append("  %-9s all six features %3.0f%%   score p10 %4d  p50 %4d  p90 %4d   reach %3.0f%% at %d, %3.0f%% at %d" % (
            n, 100 * sum(1 for r in series[n] if r["banked"] == 6) / len(series[n]),
            sc[len(sc) // 10], sc[len(sc) // 2], sc[min(len(sc) - 1, len(sc) * 9 // 10)],
            100 * reach(series[n], cur), cur, 100 * reach(series[n], cur2), cur2))
    lines.append("  Quits in optimal play: %.2f a game, games with 0 quits %.0f%% (goal: 0 quits, 100%%)" % (
        sum(r["quits"] for r in opt) / len(opt), 100 * sum(1 for r in opt if r["quits"] == 0) / len(opt)))
    lines.append("  Celebrate in optimal play: %.1f a game, %.1f of them with nothing to celebrate, more than 4 times in %.0f%% of games (goal: 4 or fewer)" % (
        sum(r["celebrates"] for r in opt) / len(opt), sum(r["celebrate_empty"] for r in opt) / len(opt),
        100 * sum(1 for r in opt if r["celebrates"] > 4) / len(opt)))
    shares = card_shares(opt)
    lines.append("  Card use in optimal play: all but %d action cards in %.0f%% of games (goal %.0f%%); every card in more than %.0f%% of games (goal): %s" % (
        CARD_MISSING_MAX, all_but_one(opt), CARD_MISSING_SHARE, CARD_SHARE_MIN, ", ".join("%s %.0f%%%s" % (c, v, "" if v > CARD_SHARE_MIN else " LOW") for c, v in shares.items())))
    lines.append("  Plan and Workshop in optimal play (goal: Plan %.1f to %.1f, Workshop %.1f to %.1f times a game): " % (
        PLAY_RANGES["Plan"] + PLAY_RANGES["Workshop"]) + "; ".join(
        "%s %.1f a game, in range in %.0f%% of games" % (c, sum(times_played(r, c) for r in opt) / len(opt),
                                                         100 * sum(1 for r in opt if PLAY_RANGES[c][0] <= times_played(r, c) <= PLAY_RANGES[c][1]) / len(opt))
        for c in ("Plan", "Workshop")))
    if top is None:
        best = max(reach(opt, t) for t in range(lo, hi + 1))
        fin = [r for r in opt if r["banked"] == 6]
        near = max([t for t in range(lo, hi + 1) if fin and sum(1 for r in fin if r["score"] >= t) / len(fin) >= UPPER_GOAL / 100] or [lo])
        lines.append("  Upper threshold: no score lets %.0f%% of optimal play reach it. Only %.0f%% of optimal games bank all six features (best reach %.0f%%)." % (UPPER_GOAL, all_six, 100 * best))
        lines.append("  Closest: %d (base %d) is the highest score that %.0f%% of the optimal games that finish reach (%.0f%% of all optimal games)." % (near, near - per, UPPER_GOAL, 100 * reach(opt, near)))
        lines.append("  Make optimal play finish first (every unfinished game scores 0); only then can the upper threshold hit %.0f%%." % UPPER_GOAL)
        up_txt = "upper: none (optimal banks all six in only %.0f%%), closest %d" % (all_six, near)
        up_set = near
    else:
        lines.append("  Upper threshold: %d (base %d) is the highest score that %.0f%% of optimal games reach.   [now %d: %.0f%%]" % (top, top - per, UPPER_GOAL, cur2, 100 * reach(opt, cur2)))
        up_txt = "upper %d" % top
        up_set = top
    lines.append("  Lower threshold: %d (base %d) is the lowest score that %s reach%s 2%% or less." % (
        low, low - per, " and ".join(rnd), "" if len(rnd) != 1 else "es") if rnd else "  Lower threshold: %d (base %d), set by hand (random play is not run)." % (low, low - per))
    for n in reasonable:
        lines.append("    at %d: %s reaches it in %.0f%% of games (all six features in %.0f%%)" % (
            low, n, 100 * reach(series[n], low), 100 * sum(1 for r in series[n] if r["banked"] == 6) / len(series[n])))
    if reasonable:
        if often is None:
            lines.append("  No score is reached by %s in 50%% or more of games. Their ceiling is the share that bank all six features: the rules, not the threshold, hold them back." % " and ".join(reasonable))
            low_txt = "lower %d (random at 2%% or less; %s stay under 50%%)" % (low, " and ".join(reasonable))
        elif often >= low:
            lines.append("  A window exists: pick the lower threshold from %d to %d (random 2%% or less, %s 50%% or more)." % (low, often, " and ".join(reasonable)))
            low_txt = "lower window %d to %d" % (low, often)
        else:
            lines.append("  No window: %s reach 50%% only up to %d, but random is above 2%% until %d." % (" and ".join(reasonable), often, low))
            low_txt = "lower: no window (%d vs %d)" % (low, often)
    else:
        low_txt = "lower %d" % low
    short = "%s; %s (now %d and %d)" % (up_txt, low_txt, cur, cur2)
    lines.append("  SET THESE: --set threshold_base=%d --set threshold_high_base=%d   (lower %d, upper %d at %d players)" % (
        low - per, up_set - per, low, up_set, rules.players))
    return "\n".join(lines) + "\n", [["threshold"] + names] + rows, short


def _flat(title: str) -> str:
    return title.split(" ")[0]


def _target_rows(title: str, res: list) -> list:
    """(target, value text, PASS/MISS or '') for one mode; the mark is only given where the goal applies to that mode."""
    ok_mark = lambda ok: "PASS" if ok else "MISS"
    k = _flat(title)
    up = share(res, lambda r: r["outcome"] == "thriving")
    lo = share(res, lambda r: r["outcome"] in ("sustainable", "thriving"))
    every = all_but_one(res)
    shares = card_shares(res)
    plan = mean(times_played(r, "Plan") for r in res)
    align = mean(times_played(r, "Workshop") for r in res)
    cel = mean(r["celebrates"] for r in res)
    tr = share(res, lambda r: "TR" in r["habits"])
    ps = share(res, lambda r: "PS" in r["habits"])
    quits = mean(r["quits"] for r in res)
    zero = share(res, lambda r: r["quits"] == 0)
    flex = max(r["max_flex"] for r in res)
    qnw = mean(r["quality_quit_nowork"] for r in res)
    onb = mean(r["onboarding_played"] for r in res)
    scored0 = share(res, lambda r: r["score"] == 0)
    return [
        ("Reach UPPER threshold (goal: optimal %.0f%% or more)" % UPPER_GOAL, "%.0f%%" % up, ok_mark(up >= UPPER_GOAL) if k == "optimal" else ""),
        ("Reach LOWER threshold (goal: balanced and invested 50% or more)", "%.0f%%" % lo,
         ok_mark(lo >= 50) if k in ("balanced", "invested") else ""),
        ("All but %d action cards played in every game (goal: %.0f%% of games)" % (CARD_MISSING_MAX, CARD_MISSING_SHARE), "%.0f%%" % every, ok_mark(every >= CARD_MISSING_SHARE)),
        ("Every action card played in more than %.0f%% of games (goal in optimal)" % CARD_SHARE_MIN,
         "fewest: %s %.0f%%" % min(shares.items(), key=lambda kv: kv[1]),
         ok_mark(min(shares.values()) > CARD_SHARE_MIN) if k == "optimal" else ""),
        ("Plan plays a game (goal: %.1f to %.1f)" % PLAY_RANGES["Plan"], "%.1f" % plan, ok_mark(PLAY_RANGES["Plan"][0] <= plan <= PLAY_RANGES["Plan"][1])),
        ("Workshop plays a game (goal: %.1f to %.1f)" % PLAY_RANGES["Workshop"], "%.1f" % align, ok_mark(PLAY_RANGES["Workshop"][0] <= align <= PLAY_RANGES["Workshop"][1])),
        ("Celebrate plays a game (goal: 4 or fewer)", "%.1f" % cel, ok_mark(cel <= 4)),
        ("Team Reflexivity held at the end (goal: reachable in optimal, 50% or more)", "%.0f%%" % tr, ok_mark(tr >= 50) if k == "optimal" else ""),
        ("Psychological Safety held at the end (goal: reachable in optimal, 50% or more)", "%.0f%%" % ps, ok_mark(ps >= 50) if k == "optimal" else ""),
        ("Quits per 100 character-weeks (HARD goal in optimal: 5 or less)", "%.2f (%.2f a game, 0 quits in %.0f%% of games)" % (quit_rate(res), quits, zero),
         ok_mark(quit_rate(res) <= QUIT_RATE_HARD) if k == "optimal" else ""),
        ("Habitus cards under %.2f quit per 100 character-weeks (soft goal: none)" % QUIT_RATE_SOFT_MIN,
         "%d of %d" % (sum(1 for v in part_quit_rates(res).values() if v < QUIT_RATE_SOFT_MIN), len(part_quit_rates(res))),
         ok_mark(all(v >= QUIT_RATE_SOFT_MIN for v in part_quit_rates(res).values())) if k == "optimal" else ""),
        ("Most Flex markers held at once (goal: 1 or fewer)", "%d" % flex, ok_mark(flex <= 1)),
        ("Quality quits after a week without Work (goal in optimal: 0.05 or less)", "%.3f" % qnw, ok_mark(qnw <= 0.05) if k == "optimal" else ""),
        ("Onboarding plays a game (goal in optimal: %.2f or less, follows the quits; not an action card)" % ONBOARDING_MAX, "%.2f" % onb, ok_mark(onb <= ONBOARDING_MAX) if k == "optimal" else ""),
        ("Games that end on 0 points (goal: optimal %.0f%% or less, balanced and invested more than %.0f%%)" % (OPT_ZERO_MAX, HAND_ZERO_MIN), "%.1f%%" % scored0,
         ok_mark(scored0 <= OPT_ZERO_MAX) if k == "optimal" else ok_mark(scored0 > HAND_ZERO_MIN) if k in ("balanced", "invested") else ""),
    ] + [("%s Need met (no goal)" % t if t in NEED_NO_GOAL else "%s Need met (soft goal: %d%% to %d%%)" % (t, NEED_SOFT_LO, need_hi(t)), "%.0f%%" % v,
          "" if t in NEED_NO_GOAL else ok_mark(NEED_SOFT_LO <= v <= need_hi(t)) if k == "optimal" else "") for t, v in need_rates(res).items()]


def write_postsim(path: str, dump: dict):
    """Markdown scoreboard: every target per mode, a summary per mode, then a section for optimal play only."""
    modes = list(dump)
    flat = lambda title: title.split(" ")[0]
    ok_mark = lambda ok: "PASS" if ok else "MISS"
    L = ["# Post-sim report", "",
         "Games per mode: %s. Players: %d. Thresholds: lower %d, upper %d." % (
             ", ".join("%s %d" % (m, len(dump[m][1])) for m in modes), dump[modes[0]][0].players,
             dump[modes[0]][1][0]["threshold"], dump[modes[0]][1][0]["threshold_high"]), ""]

    def per_game(res, card):
        return mean(times_played(r, card) for r in res)

    targets = _target_rows

    tt = {m: targets(m, dump[m][1]) for m in modes}
    L += ["## 1. Targets by mode", "", "| Target | " + " | ".join(modes) + " |", "|---|" + "---|" * len(modes)]
    for i, row in enumerate(tt[modes[0]]):
        L.append("| %s | %s |" % (row[0], " | ".join((tt[m][i][1] + (" **%s**" % tt[m][i][2] if tt[m][i][2] else "")) for m in modes)))
    L += ["", "PASS/MISS is only shown where the goal applies to that mode.", ""]

    L += ["## 2. Summary by mode", "", "| Measure | " + " | ".join(modes) + " |", "|---|" + "---|" * len(modes)]
    summ = [
        ("Failure / heroic / sustainable / high performance", lambda res: "%.0f / %.0f / %.0f / %.0f %%" % tuple(
            share(res, lambda r, o=o: r["outcome"] == o) for o in ("failure", "heroic", "sustainable", "thriving"))),
        ("Mean score (p10 / p90)", lambda res: "%.1f (%d / %d)" % (mean(r["score"] for r in res), pct([r["score"] for r in res], 10), pct([r["score"] for r in res], 90))),
        ("Features banked, all six", lambda res: "%.2f, %.0f%%" % (mean(r["banked"] for r in res), share(res, lambda r: r["banked"] == 6))),
        ("Habits held at the end", lambda res: "%.1f" % mean(len(r["habits"]) for r in res)),
        ("Events cancelled", lambda res: "%.1f of %.1f" % (mean(sum(r["cancel_by"].values()) for r in res), mean(r["events_drawn"] for r in res))),
        ("Mean Motivation at week 8 (lowest)", lambda res: "%.2f (%.2f)" % (mean(r["mot_mean"][-1] for r in res), mean(r["mot_min"][-1] for r in res))),
        ("Quits a game, games with a quit", lambda res: "%.2f, %.0f%%" % (mean(r["quits"] for r in res), share(res, lambda r: r["quits"] > 0))),
        ("Capability / Trust / Shared Practice at the end", lambda res: "%.1f / %.1f / %.1f" % (
            mean(r["cap"] for r in res), mean(r["trust"] for r in res), mean(r["sp"] for r in res))),
    ]
    for label, fn in summ:
        L.append("| %s | %s |" % (label, " | ".join(fn(dump[m][1]) for m in modes)))

    opt = [m for m in modes if flat(m) == "optimal"]
    for m in opt:
        rules, res = dump[m]
        W = rules.weeks
        L += ["", "## 3. Optimal play only: %s" % m, "", "### Targets", ""]
        L += ["- %s: %s%s" % (t, v, " **%s**" % ok if ok else "") for t, v, ok in tt[m]]
        L += ["", "### Motivation and quits by week", "", "| Week | " + " | ".join(str(i + 1) for i in range(W)) + " |", "|---|" + "---|" * W]
        for label, key in (("Lowest", "mot_min"), ("Mean", "mot_mean"), ("Median", "mot_med"), ("Quits", "quit_week")):
            L.append("| %s | %s |" % (label, " | ".join("%.2f" % mean(r[key][i] for r in res) for i in range(W))))
        qc = Counter()
        for r in res:
            qc.update(r["quit_causes"])
        L += ["", "Quit causes per game (biggest Motivation loss in the week): " + (
            ", ".join("%s %.2f" % (k, v / len(res)) for k, v in qc.most_common()) or "none") + "."]
        L += ["", "### Event cards in weeks 2 to 4 (every card is drawn equally often; the difference is which ones land)", "",
              "| Event | cost to cancel | drawn a game | landed a game | share that landed |", "|---|---|---|---|---|"]
        cost_of = {e.name: ("cannot" if e.cost is None else "say no" if e.say_no else e.cost) for e in EVENTS}
        for landed, n, drawn, s in event_early_rows(res):
            L.append("| %s | %s | %.3f | %.3f | %.0f%% |" % (n, cost_of[n], drawn, landed, 100 * s))
        L += ["", "### Event cards behind quits", "", "| Event | quits a game | lands a game | quits per 100 landings |", "|---|---|---|---|"]
        for q, n, landed, p in event_quit_rows(res)[:8]:
            L.append("| %s | %.3f | %.2f | %.1f |" % (n, q, landed, p))
        L += ["", "### Event cards behind each habitus card's quits (the quit week and the week before)", "",
              "| Habitus card | Event cards (quits a game) |", "|---|---|"]
        for kind, val, rows in event_habitus_top(res):
            L.append("| %s %s | %s |" % (kind, val, ", ".join("%s %.3f" % (n, v) for v, n in rows)))
        L += ["", "### Cards (share of games playing each, plays a game)", "", "| Card | share | per game |", "|---|---|---|"]
        for c in ACTION_CARDS:
            L.append("| %s | %.0f%% | %.2f |" % (c, share(res, lambda r, c=c: c in cards_played(r)), per_game(res, c)))
        agg = Counter()
        for r in res:
            agg.update(r["parts"])
        L += ["", "### Habitus parts by quits (per 100 character-weeks)", "", "| Part | quits/100 | mean Motivation |", "|---|---|---|"]
        rows = []
        for key in {k.rsplit("|", 1)[0] for k in agg}:
            wks = agg.get(key + "|weeks", 0)
            if wks:
                rows.append((100 * agg.get(key + "|quits", 0) / wks, agg.get(key + "|mot", 0) / wks, key.replace("|", " ")))
        for q, mo, name in sorted(rows, reverse=True)[:8]:
            L.append("| %s | %.1f | %.2f |" % (name, q, mo))
        L += ["", "Lowest mean Motivation: " + ", ".join("%s %.2f" % (n, mo) for _, mo, n in sorted(rows, key=lambda x: x[1])[:4]) + "."]
        pairs = pair_quit_table(res)
        L += ["", "### Pairs of habitus parts that quit most (per 100 character-weeks, pairs with 300+ character-weeks)", "",
              "| Pair | quits/100 | vs all | quits | character-weeks |", "|---|---|---|---|---|"]
        for rate, ratio, q, wks, name in pairs[:12]:
            L.append("| %s | %.1f | %.1fx | %d | %d |" % (name, rate, ratio, q, wks))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


def event_early_rows(res: list, first: int = 2, last: int = 4) -> list:
    """(landed a game, Event, drawn a game, share that landed) for weeks first..last, most-landed first."""
    agg = Counter()
    for r in res:
        agg.update(r.get("event_stats", {}))
    out = []
    for e in EVENTS:
        drawn = sum(agg["ev_drawn_w%d|%s" % (w, e.name)] for w in range(first, last + 1)) / len(res)
        landed = sum(agg["ev_landed_w%d|%s" % (w, e.name)] for w in range(first, last + 1)) / len(res)
        out.append((landed, e.name, drawn, landed / drawn if drawn else 0.0))
    return sorted(out, reverse=True)


def event_quit_rows(res: list) -> list:
    """(quits a game, Event, times landed a game, quits per 100 landings), worst first: quits where that Event cost the quitter the most."""
    agg = Counter()
    for r in res:
        agg.update(r.get("event_stats", {}))
    names = {k.split("|", 1)[1] for k in agg if k.startswith(("ev_landed|", "ev_quit|"))}
    rows = [(agg["ev_quit|" + n] / len(res), n, agg["ev_landed|" + n] / len(res),
             100 * agg["ev_quit|" + n] / max(1, agg["ev_landed|" + n])) for n in names]
    return sorted(rows, reverse=True)


def quit_who_rows(res: list, weeks: int) -> list:
    """(habitus card, average quits a game in each week), values then instinct then upbringing."""
    agg = Counter()
    for r in res:
        agg.update(r["quit_who"])
    rows = []
    for kind, vals in (("torso", TORSOS), ("legs", LEGS), ("base", BASES)):
        for val in vals:
            rows.append(("%s %s" % (HUMAN_KIND[kind], val),
                         [agg.get("%d|%s|%s" % (w, kind, val), 0) / len(res) for w in range(1, weeks + 1)]))
    return rows


def _heat(out: list, x: float, y: float, w: float, title: str, rows: list, weeks: int) -> float:
    """Heatmap: one row per habitus card, one column per week, darker red = more quits a game. Returns the bottom y."""
    out.append('<text x="%g" y="%g" class="t">%s</text>' % (x, y - 14, _esc(title)))
    lab, rh, tot = 150, 18, 60
    cw = (w - lab - tot) / weeks
    vmax = max([v for _, vals in rows for v in vals] + [0.01])
    for i in range(weeks):
        out.append('<text x="%.1f" y="%g" class="a" text-anchor="middle">w%d</text>' % (x + lab + (i + 0.5) * cw, y + 8, i + 1))
    out.append('<text x="%.1f" y="%g" class="a" text-anchor="middle">all</text>' % (x + lab + weeks * cw + tot / 2, y + 8))
    for j, (name, vals) in enumerate(rows):
        yy = y + 14 + j * rh + (6 if j >= 5 else 0) + (6 if j >= 10 else 0)
        out.append('<text x="%g" y="%g" class="a" text-anchor="end">%s</text>' % (x + lab - 6, yy + 12, _esc(name)))
        for i, v in enumerate(vals):
            t = min(1.0, v / vmax)
            col = "#%02X%02X%02X" % (round(255 - 54 * t), round(255 - 213 * t), round(255 - 213 * t))
            out.append('<rect x="%.1f" y="%g" width="%.1f" height="%d" fill="%s" stroke="#fff"/>' % (x + lab + i * cw, yy, cw, rh - 1, col))
            if v >= 0.005:
                out.append('<text x="%.1f" y="%g" class="a" text-anchor="middle" style="fill:%s">%.2f</text>' % (
                    x + lab + (i + 0.5) * cw, yy + 12, "#fff" if t > 0.6 else "#222", v))
        out.append('<text x="%.1f" y="%g" class="t" text-anchor="middle">%.2f</text>' % (x + lab + weeks * cw + tot / 2, yy + 12, sum(vals)))
    return y + 14 + len(rows) * rh + 12


def _hbars(out: list, x: float, y: float, w: float, title: str, rows: list, maxv: float, fmt: str, bands: dict | None = None):
    """Horizontal bars; rows are (label, value, colour); bands shade the goal range for a label."""
    out.append('<text x="%g" y="%g" class="t">%s</text>' % (x, y - 14, _esc(title)))
    lab, bw = 150, w - 150 - 70
    for i, (label, val, col) in enumerate(rows):
        yy = y + i * 20
        if bands and label in bands:
            lo, hi = bands[label]
            out.append('<rect x="%.1f" y="%g" width="%.1f" height="18" fill="#D8F0DC"/>' % (x + lab + lo / maxv * bw, yy - 1, (hi - lo) / maxv * bw))
        out.append('<text x="%g" y="%g" class="a" text-anchor="end">%s</text>' % (x + lab - 6, yy + 12, _esc(label)))
        out.append('<rect x="%g" y="%g" width="%.1f" height="12" fill="%s" stroke="%s" stroke-width=".5"/>' % (
            x + lab, yy + 2, max(0.0, min(val, maxv)) / maxv * bw, col, INK))
        out.append('<text x="%.1f" y="%g" class="a">%s</text>' % (x + lab + min(val, maxv) / maxv * bw + 4, yy + 12, fmt % val))
    return y + len(rows) * 20


def event_habitus_top(res: list, top: int = 3) -> list:
    """Per habitus part: the Event cards with the most quits attributed to them (the Motivation they cost in the quit week
    and the week before, shared out by size), in quits a game."""
    q = Counter()
    for r in res:
        for k, v in r.get("event_habitus", {}).items():
            if k.startswith("evq|"):
                q[k.split("|", 1)[1]] += v
    out = []
    for kind, val in [("torso", t) for t in TORSOS] + [("legs", l) for l in LEGS] + [("base", b) for b in BASES]:
        rows = sorted(((q["%s|%s|%s" % (kind, val, e.name)] / len(res), e.name) for e in EVENTS), reverse=True)[:top]
        out.append((kind, val, rows))
    return out


def plot_event_habitus(path: str, dump: dict):
    """Heatmap: which Event cards sit behind the quits of each habitus part (2-week look-back), per 100 games."""
    modes = [m for m in dump if _flat(m) in ("balanced", "optimal")]
    parts = [("torso", t) for t in TORSOS] + [("legs", l) for l in LEGS] + [("base", b) for b in BASES]
    CW, CH, X0, LAB = 46, 16, 200, 210
    out, y = [], 30
    for m in modes:
        res = dump[m][1]
        n = len(res)
        q = Counter()
        for r in res:
            for k, v in r.get("event_habitus", {}).items():
                if k.startswith("evq|"):
                    q[k.split("|", 1)[1]] += v
        grid = {(e.name, p): 100 * q["%s|%s|%s" % (p[0], p[1], e.name)] / n for e in EVENTS for p in parts}
        order = sorted(EVENTS, key=lambda e: -sum(grid[(e.name, p)] for p in parts))
        hi = max(grid.values()) or 1
        out.append('<text x="20" y="%d" font-size="15" font-weight="bold">%s: Event cards behind quits, per habitus card (quits per 100 games, Events of the quit week and the week before)</text>' % (y, _esc(_flat(m))))
        y += 14
        for j, (kind, val) in enumerate(parts):
            out.append('<text x="%d" y="%d" font-size="10" transform="rotate(-45 %d %d)">%s %s</text>' % (
                X0 + j * CW + CW / 2, y + 72, X0 + j * CW + CW / 2, y + 72, kind, _esc(val)))
        y += 80
        for e in order:
            out.append('<text x="%d" y="%d" font-size="10" text-anchor="end">%s</text>' % (X0 - 6, y + 12, _esc(e.name)))
            for j, p in enumerate(parts):
                v = grid[(e.name, p)]
                shade = int(255 - 190 * min(1.0, v / hi))
                out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="rgb(255,%d,%d)" stroke="#fff"/>' % (X0 + j * CW, y, CW, CH, shade, shade))
                if v >= 0.5:
                    out.append('<text x="%d" y="%d" font-size="9" text-anchor="middle">%.0f</text>' % (X0 + j * CW + CW / 2, y + 12, v))
            y += CH
        y += 50
    W = X0 + len(parts) * CW + 40
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="Arial, sans-serif">' % (W, y, W, y),
           '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, y)] + out + ["</svg>"]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(svg))


def plot_quit_triggers(path: str, dump: dict):
    """What triggers quitting: the biggest Motivation loss behind each quit, and the Event cards behind the Event quits."""
    modes = [m for m in dump if _flat(m) in ("balanced", "invested", "optimal")]
    W, PH = 1180, 340
    out = []

    def bars(x, y, labels, series, colours, scale, w, row=17):
        for i, (lab, vals) in enumerate(zip(labels, series)):
            yy = y + i * row
            out.append('<text x="%d" y="%d" font-size="11" text-anchor="end">%s</text>' % (x - 6, yy + 12, _esc(lab)))
            xx = x
            for v, col in zip(vals, colours):
                bw = v * scale
                if bw > 0:
                    out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s"/>' % (xx, yy, bw, row - 4, col))
                xx += bw
            out.append('<text x="%.1f" y="%d" font-size="10" fill="#444">%.2f</text>' % (xx + 4, yy + 12, sum(vals)))

    for i, m in enumerate(modes):
        res = dump[m][1]
        n = len(res)
        y0 = 30 + i * PH
        out.append('<text x="20" y="%d" font-size="15" font-weight="bold">%s: what triggers quitting (quits a game, %d games)</text>' % (y0, _esc(_flat(m)), n))
        qc, qq, agg = Counter(), Counter(), Counter()
        for r in res:
            qc.update(r["quit_causes"])
            agg.update(r.get("event_stats", {}))
            for k, v in r.get("event_stats", {}).items():
                if k.startswith("quit_q_cause|"):
                    qq[k.split("|", 1)[1]] += v
        out.append('<text x="20" y="%d" font-size="12" fill="#555">Biggest Motivation loss behind the quit (dark: a Quality character)</text>' % (y0 + 22))
        causes = qc.most_common(7)
        labels = [c for c, _ in causes]
        series = [((v - qq[c]) / n, qq[c] / n) for c, v in causes]
        top = max([sum(s) for s in series] or [1])
        bars(300, y0 + 32, labels, series, ("#74A9CF", "#08519C"), 200 / top, 200)
        out.append('<text x="640" y="%d" font-size="12" fill="#555">Event cards behind the Event quits (dark: a Quality character)</text>' % (y0 + 22))
        names = {k.split("|", 1)[1] for k in agg if k.startswith("ev_quit|")}
        rows = sorted(((agg["ev_quit|" + e] / n, agg["ev_quit_q|" + e] / n, e) for e in names), reverse=True)[:12]
        labels = [e for _, _, e in rows]
        series = [(t - q, q) for t, q, _ in rows]
        top = max([t for t, _, _ in rows] or [1])
        bars(900, y0 + 32, labels, series, ("#F4A582", "#B2182B"), 220 / top, 220)
    H = 30 + len(modes) * PH
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="Arial, sans-serif">' % (W, H, W, H),
           '<rect width="%d" height="%d" fill="#ffffff"/>' % (W, H)] + out + ["</svg>"]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(svg))


SCORE_COL = {"balanced": "#1971C2", "invested": "#E8590C", "optimal": "#1F7A4D", "random": "#868E96", "hero": "#9B51E0"}


def _score_chart(out: list, x: float, y: float, w: float, h: float, dump: dict) -> float:
    """Share of games that reach at least each Team Score, one line per mode, with both thresholds and the goals. Returns the bottom edge."""
    from bisect import bisect_left
    modes = list(dump)
    R = dump[modes[0]][0]
    lo_t = R.threshold_base + R.threshold_per_player * R.players
    hi_t = R.threshold_high_base + R.threshold_per_player * R.players
    mx = max(20, math.ceil((max(max(r["score"] for r in dump[m][1]) for m in modes) + 1) / 20) * 20)
    px = lambda s: x + w * s / mx
    py = lambda p: y + h - h * p / 100
    out.append('<text x="%g" y="%g" class="h">TEAM SCORE BY MODE</text>' % (x, y - 34))
    out.append('<text x="%g" y="%g" class="a">share of games that reach at least this Team Score (the drop at 1 is the games that end on 0)</text>' % (x, y - 16))
    out.append('<rect x="%g" y="%g" width="%g" height="%g" fill="#fafafa" stroke="#ccc"/>' % (x, y, w, h))
    for p in (0, 25, 50, 75, 100):
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" class="g"/><text x="%g" y="%g" class="a" text-anchor="end">%d%%</text>' % (x, py(p), x + w, py(p), x - 6, py(p) + 4, p))
    for s in range(0, mx + 1, 20):
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" class="g"/><text x="%g" y="%g" class="a" text-anchor="middle">%d</text>' % (px(s), y, px(s), y + h, px(s), y + h + 16, s))
    for t, label in ((lo_t, "lower threshold %d" % lo_t), (hi_t, "upper threshold %d" % hi_t)):
        out.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#C92A2A" stroke-width="1.4" stroke-dasharray="6 3"/>' % (px(t), y, px(t), y + h))
        out.append('<text x="%g" y="%g" class="a" text-anchor="middle">%s</text>' % (px(t), y - 3, _esc(label)))
    for i, m in enumerate(modes):
        sc = sorted(r["score"] for r in dump[m][1])
        n = len(sc)
        col = SCORE_COL.get(_flat(m), "#444444")
        pts = " ".join("%g,%g" % (px(s), py(100 * (n - bisect_left(sc, s)) / n)) for s in range(0, mx + 1))
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>' % (pts, col))
        out.append('<rect x="%g" y="%g" width="14" height="4" fill="%s"/><text x="%g" y="%g" class="a">%s</text>' % (
            x + w - 150, y + 14 + i * 18, col, x + w - 130, y + 19 + i * 18, _esc(_flat(m))))
    out.append('<circle cx="%g" cy="%g" r="6" fill="none" stroke="#1F7A4D" stroke-width="2"/>' % (px(hi_t), py(UPPER_GOAL)))
    out.append('<text x="%g" y="%g" class="a">goal: optimal %.0f%% at the upper threshold</text>' % (px(hi_t) + 10, py(UPPER_GOAL) - 8, UPPER_GOAL))
    out.append('<circle cx="%g" cy="%g" r="6" fill="none" stroke="#1971C2" stroke-width="2"/>' % (px(lo_t), py(50)))
    out.append('<text x="%g" y="%g" class="a">goal: balanced and invested 50%% at the lower threshold</text>' % (px(lo_t) + 10, py(50) - 8))
    out.append('<text x="%g" y="%g" class="a" text-anchor="middle">Team Score</text>' % (x + w / 2, y + h + 34))
    return y + h + 40


def plot_summary(path: str, dump: dict):
    """One page: every target by mode, then a focus on optimal play."""
    modes = list(dump)
    X0, LAB, COL, RH = 40, 560, 175, 22
    out = []
    rows0 = _target_rows(modes[0], dump[modes[0]][1])
    tt = {m: _target_rows(m, dump[m][1]) for m in modes}
    y0 = 84
    out.append('<text x="%d" y="%d" class="h">TARGETS BY MODE</text>' % (X0, y0 - 22))
    out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#f1f3f5"/>' % (X0, y0, LAB + COL * len(modes), RH))
    out.append('<text x="%d" y="%d" class="t">target</text>' % (X0 + 6, y0 + 15))
    for j, m in enumerate(modes):
        out.append('<text x="%d" y="%d" class="t" text-anchor="middle">%s</text>' % (X0 + LAB + j * COL + COL / 2, y0 + 15, _esc(_flat(m))))
    for i, row in enumerate(rows0):
        yy = y0 + (i + 1) * RH
        out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" class="g"/>' % (X0, yy, X0 + LAB + COL * len(modes), yy))
        out.append('<text x="%d" y="%d" class="a">%s</text>' % (X0 + 6, yy + 15, _esc(row[0])))
        for j, m in enumerate(modes):
            _, val, mark = tt[m][i]
            fill = "#CDEBD3" if mark == "PASS" else "#F5C6C6" if mark == "MISS" else "#ffffff"
            cx = X0 + LAB + j * COL
            out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s"/>' % (cx + 2, yy + 1, COL - 4, RH - 2, fill))
            out.append('<text x="%d" y="%d" class="a" text-anchor="middle">%s%s</text>' % (
                cx + COL / 2, yy + 15, _esc(val if len(val) < 22 else val.split(" (")[0]), (" " + mark) if mark else ""))
    tab_end = y0 + (len(rows0) + 1) * RH
    tab_end = _score_chart(out, X0 + 40, tab_end + 70, 1000, 300, dump) + 10
    width = X0 + LAB + COL * len(modes) + 40
    width = max(width, 1120)
    height = tab_end + 40
    opt = next((m for m in modes if _flat(m) == "optimal"), None)
    if opt:
        rules, res = dump[opt]
        W = rules.weeks
        out.append('<text x="%d" y="%d" class="h">OPTIMAL PLAY</text>' % (X0, tab_end + 52))
        ys = tab_end + 100
        # Motivation, quits
        p1 = _Panel(X0 + 34, ys, 560, 220, rules.mot_cap, W)
        series = [("Lowest Motivation", "#C92A2A", week_mean(res, "mot_min", W), False),
                  ("Mean Motivation", "#1F7A4D", week_mean(res, "mot_mean", W), False),
                  ("Median Motivation", "#1971C2", week_mean(res, "mot_med", W), True),
                  ("Quits that week", INK, [mean(r["quit_week"][i] for r in res) for i in range(W)], True)]
        _frame(out, p1, "Motivation per week and quits (goal: 0 quits)", "Motivation / quits")
        _lines(out, p1, series)
        _legend(out, p1, [(s[0], s[1], "dash" if s[3] else "line") for s in series])
        # cards per game
        card_rows = [(c, mean(times_played(r, c) for r in res), CARD_COLOUR.get(c, "#999999")) for c in ACTION_CARDS]
        _hbars(out, 880, ys, 480, "Cards played per game (green band = goal)", card_rows,
               _nice_max(max(v for _, v, _ in card_rows)), "%.1f", {**PLAY_RANGES, "Celebrate": (0, 4)})
        ys2 = ys + 220 + 90
        # needs met
        need_rows = []
        for t, col in (("Autonomy", "#F7D7A1"), ("Hierarchy", "#C7CFB5"), ("Community", "#D3CEDF"), ("Quality", "#B5C7CF"), ("Recognition", "#D9D3C4")):
            seen = sum(r["need_seen"].get(t, 0) for r in res)
            need_rows.append((t, 100 * sum(r["need_met"].get(t, 0) for r in res) / seen if seen else 0.0, col))
        end1 = _hbars(out, X0 + 34, ys2, 560, "Need met, share of character-weeks (green band = soft goal)", need_rows, 100, "%.0f%%", {t: (NEED_SOFT_LO, need_hi(t)) for t, _, _ in need_rows if t not in NEED_NO_GOAL})
        # quits by habitus part, human names
        human = {"torso": "values", "legs": "instinct", "base": "upbringing"}
        agg = Counter()
        for r in res:
            agg.update(r["parts"])
        parts = []
        for key in {k.rsplit("|", 1)[0] for k in agg}:
            wks = agg.get(key + "|weeks", 0)
            if wks:
                kind, val = key.split("|")
                parts.append((100 * agg.get(key + "|quits", 0) / wks, "%s %s" % (human.get(kind, kind), val)))
        parts.sort(reverse=True)
        part_rows = [(n, q, "#D3B1B1") for q, n in parts[:8]]
        _hbars(out, 880, ys2, 480, "Quits per 100 character-weeks, worst 8 habitus cards", part_rows, _nice_max(max([q for _, q, _ in part_rows] + [1])), "%.1f")
        # key numbers
        sc = sorted(r["score"] for r in res)
        yh = max(end1, ys2 + 8 * 20) + 60
        yh_end = _heat(out, X0 + 34, yh, 1280, "Who quits when (optimal): average quits a game, by habitus card and week", quit_who_rows(res, W), W)
        yk = yh_end + 50
        facts = ["Mean score %.1f (p10 %d, p90 %d)" % (mean(sc), pct(sc, 10), pct(sc, 90)),
                 "Features banked %.2f of 6, all six in %.0f%% of games" % (mean(r["banked"] for r in res), share(res, lambda r: r["banked"] == 6)),
                 "Habits held at the end %.1f" % mean(len(r["habits"]) for r in res),
                 "Quits %.2f a game, 0 quits in %.0f%% of games" % (mean(r["quits"] for r in res), share(res, lambda r: r["quits"] == 0)),
                 "Events cancelled %.1f of %.1f" % (mean(sum(r["cancel_by"].values()) for r in res), mean(r["events_drawn"] for r in res))]
        out.append('<text x="%d" y="%d" class="t">Optimal in numbers</text>' % (X0 + 34, yk - 14))
        for i, f in enumerate(facts):
            out.append('<text x="%d" y="%d" class="a">%s</text>' % (X0 + 34, yk + i * 18, _esc(f)))
        height = yk + len(facts) * 18 + 30
        width = max(width, 1400)
    head = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
            '<style>.t{font:bold 13px sans-serif;fill:#111}.a{font:11px sans-serif;fill:#444}.g{stroke:#ddd;stroke-width:1}'
            '.h{font:bold 18px sans-serif;fill:#111}</style><rect width="100%%" height="100%%" fill="#fff"/>'
            '<text x="%d" y="30" style="font:bold 20px sans-serif">Balance summary: targets and optimal play  (%d games per mode, %d players)</text>') % (
        width, height, width, height, X0, len(dump[modes[0]][1]), dump[modes[0]][0].players)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(head + "".join(out) + "</svg>\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", type=int, default=2000)
    ap.add_argument("--players", type=int, default=5)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--strategies", default="hero,balanced,invested,random,optimal",
                    help="comma list from: %s, optimal (optimal = searched best policy)" % ", ".join(STRATEGIES))
    ap.add_argument("--opt-runs", type=int, default=150, help="games per candidate while searching for optimal play")
    ap.add_argument("--opt-passes", type=int, default=3, help="max search passes for optimal play")
    ap.add_argument("--reuse-optimal", action="store_true",
                    help="skip the optimal search and use the strategy saved by the last search (balance_sim_optimal.json)")
    ap.add_argument("--plots", metavar="DIR", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots"),
                    help="write one SVG per strategy here (default: plots beside this script)")
    ap.add_argument("--no-plots", action="store_true")
    ap.add_argument("--verbose", action="store_true", help="also print the full report to the terminal")
    ap.add_argument("--report", metavar="FILE", default=None,
                    help="full text report (default: the --csv name with _report.txt)")
    ap.add_argument("--set", action="append", default=[], metavar="RULE=VALUE")
    ap.add_argument("--sweep", metavar="RULE=V1,V2,...", help="rerun every strategy for each value of one rule")
    ap.add_argument("--json", metavar="FILE", help="write raw per-game results")
    ap.add_argument("--csv", metavar="FILE", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "balance_sim_results.csv"),
                    help="per-game results, one row per game (default: balance_sim_results.csv beside this script)")
    a = ap.parse_args()
    if not a.report:
        a.report = os.path.splitext(a.csv)[0] + "_report.txt"

    base = apply_overrides(Rules(players=a.players), a.set)
    names = a.strategies.split(",")
    for s in names:
        if s != "optimal" and s not in STRATEGIES:
            sys.exit("unknown strategy %r; choose from: %s, optimal" % (s, ", ".join(STRATEGIES)))

    variants = [("", base)]
    if a.sweep:
        k, _, vs = a.sweep.partition("=")
        variants = [("%s=%s" % (k, v), apply_overrides(base, ["%s=%s" % (k, v)])) for v in vs.split(",")]

    dump = {}
    log, reports = [], []
    steps, step, t0 = len(variants) * len(names), 0, time.time()
    for label, rules in variants:
        for name in names:
            step += 1
            tag = "[%d/%d] %s" % (step, steps, name + ((" " + label) if label else ""))
            st = optimise(rules, a.opt_runs, a.opt_passes, a.seed + 777, tag, log, a.reuse_optimal) if name == "optimal" else STRATEGIES[name]
            res = simulate(rules, st, a.runs, a.seed, tag)
            title = name + ((" [" + label + "]") if label else "")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                report(title, res, rules)
            reports.append(buf.getvalue())
            if a.verbose:
                print(buf.getvalue())
            dump[title] = (rules, res)
    status("writing files...")
    cal_text, cal_rows, cal_short = calibrate(dump) if not a.sweep else ("", [], "")
    if cal_text:
        reports.append(cal_text)
    with open(a.report, "w", encoding="utf-8") as fh:
        fh.write("\n".join(log + reports))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump({t: r for t, (_, r) in dump.items()}, fh)
    if a.csv:
        write_csv(a.csv, dump)
        write_postsim(os.path.splitext(a.csv)[0] + "_postsim.md", dump)
        write_habitus_csv(os.path.splitext(a.csv)[0] + "_habitus.csv", dump)
        if cal_rows:
            with open(os.path.splitext(a.csv)[0] + "_threshold.csv", "w", newline="", encoding="utf-8") as fh:
                csv.writer(fh).writerows(cal_rows)
    if not a.no_plots:
        os.makedirs(a.plots, exist_ok=True)
        for title, (rules, res) in dump.items():
            fname = "plot_" + "".join(ch if ch.isalnum() else "_" for ch in title).strip("_") + ".svg"
            plot_strategy(os.path.join(a.plots, fname), title, res, rules)
        plot_summary(os.path.join(a.plots, "summary_targets_optimal.svg"), dump)
        plot_quit_triggers(os.path.join(a.plots, "quit_triggers.svg"), dump)
        plot_event_habitus(os.path.join(a.plots, "quit_event_habitus.svg"), dump)
    status("done in %.0fs" % (time.time() - t0), final=True)
    print("  report  %s" % a.report)
    if cal_short:
        print("  calibration: %s" % cal_short)
    if a.csv:
        print("  csv     %s (+ _summary, _habitus)" % a.csv)
    if not a.no_plots:
        print("  plots   %s (%d files)" % (a.plots, len(dump)))


if __name__ == "__main__":
    main()
