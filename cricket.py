#!/usr/bin/env python3
"""
cricket_game.py
A simple terminal cricket game (player vs CPU).
Run: python cricket_game.py
"""

import random
import time

# ---------------------------
# Configuration / Utilities
# ---------------------------
def slowprint(s, delay=0.02):
    # small helper to show commentary
    for ch in s:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def choose(prompt, options):
    # prompt until user picks a valid option (string options)
    options_str = "/".join(options)
    while True:
        val = input(f"{prompt} ({options_str}): ").strip().lower()
        if val in options:
            return val
        print("Invalid choice — try again.")

# ---------------------------
# Game logic
# ---------------------------

class Innings:
    def __init__(self, overs, batting_is_human=True, target=None):
        self.overs = overs
        self.batting_is_human = batting_is_human
        self.target = target  # if chasing, None otherwise
        self.runs = 0
        self.wickets = 0
        self.balls = 0
        self.comments = []

    def balls_remaining(self):
        return self.overs * 6 - self.balls

    def is_finished(self):
        if self.balls >= self.overs * 6:
            return True
        if self.wickets >= 10:
            return True
        if self.target is not None and self.runs > self.target:
            # If runs > target, chasing side has won already (we use > so target=100 means need 101 to win)
            return True
        return False

    def over_and_ball(self):
        o = self.balls // 6
        b = self.balls % 6
        return o, b

    def summary(self):
        o, b = self.over_and_ball()
        return f"{self.runs}/{self.wickets} in {o}.{b} overs"

# Probabilities matrix: given batting choice and bowling choice, produce outcome distribution
# Outcomes: -1 => wicket, 0,1,2,3,4,6 runs, "WIDE", "NOBALL"
# We'll model as weighted list
def outcome_distribution(bat_choice, bowl_choice):
    # base probabilities differ by choice
    # bat_choice: 'def' (defensive), 'norm' (normal), 'agg' (aggressive)
    # bowl_choice: 'fast', 'spin', 'line' (accurate)
    # We'll return a weighted list of outcomes to random.choices from
    # Weights tuned to feel reasonable
    base = []

    if bat_choice == 'def':
        base = [
            (0, 30), (1, 25), (2, 10), (3, 2), (4, 8), (6, 1), (-1, 8),
            ("WIDE", 8), ("NOBALL", 8)
        ]
    elif bat_choice == 'norm':
        base = [
            (0, 20), (1, 30), (2, 15), (3, 3), (4, 12), (6, 4), (-1, 8),
            ("WIDE", 4), ("NOBALL", 4)
        ]
    else:  # agg
        base = [
            (0, 12), (1, 25), (2, 12), (3, 4), (4, 18), (6, 12), (-1, 12),
            ("WIDE", 3), ("NOBALL", 2)
        ]

    # adjust by bowl_choice
    # fast: slightly more wickets but more boundaries too
    # spin: induces more single/2 and occasional wicket
    # line: fewer wickets, fewer wides
    modified = []
    for outcome, weight in base:
        w = weight
        if bowl_choice == 'fast':
            if outcome == -1:
                w = int(w * 1.3)
            if outcome in (4,6):
                w = int(w * 1.1)
            if outcome in ("WIDE","NOBALL"):
                w = int(w * 1.1)
        elif bowl_choice == 'spin':
            if outcome in (1,2,3):
                w = int(w * 1.2)
            if outcome == -1:
                w = int(w * 1.1)
            if outcome in (4,6):
                w = int(w * 0.9)
        else:  # line
            if outcome == -1:
                w = int(w * 0.7)
            if outcome in ("WIDE","NOBALL"):
                w = int(w * 0.4)
            if outcome in (4,6):
                w = int(w * 0.8)
        if w <= 0:
            w = 1
        modified.append((outcome, w))
    return modified

def sample_outcome(dist):
    outcomes = [o for o,_ in dist]
    weights = [w for _,w in dist]
    out = random.choices(outcomes, weights=weights, k=1)[0]
    return out

def play_ball(inning: Innings, bat_choice=None, bowl_choice=None, human_batting=True):
    # if batting is human, bat_choice is provided by human; else CPU
    # CPU chooses bat_choice randomly based on game state
    if bat_choice is None:
        # CPU batting strategy: if chasing and close to target be aggressive
        if inning.target is not None:
            need = inning.target - inning.runs + 1
            balls_left = inning.balls_remaining()
            run_rate_needed = need / max(1, balls_left/6)
            if need <= 6 and balls_left <= 6:
                bat_choice = 'agg'
            elif run_rate_needed > 6:
                bat_choice = 'agg'
            elif run_rate_needed > 3:
                bat_choice = 'norm'
            else:
                bat_choice = 'def'
        else:
            # first innings: mix based on wickets
            if inning.wickets >= 6:
                bat_choice = 'def'
            else:
                bat_choice = random.choices(['def','norm','agg'], weights=[2,5,3])[0]

    if bowl_choice is None:
        # if human is bowling, they might choose; else CPU chooses bowl_choice
        bowl_choice = random.choice(['fast','spin','line'])

    dist = outcome_distribution(bat_choice, bowl_choice)
    outcome = sample_outcome(dist)

    # Handle wides/noballs (they don't count as legal ball, add run and not increment ball)
    if outcome == "WIDE":
        inning.runs += 1
        inning.comments.append("Wide ball! +1 run (ball repeated).")
        return False  # ball not counted as legal
    if outcome == "NOBALL":
        # treat noball as 1 extra + a free-hit (we'll allow next ball to not cause wicket)
        inning.runs += 1
        inning.comments.append("No-ball! +1 run and free-hit.")
        # On free-hit, we simulate again but wicket cannot occur (convert wicket -> 0)
        dist2 = []
        for o,w in outcome_distribution(bat_choice, bowl_choice):
            if o == -1:
                # replace wicket chance into dot ball chance
                o2 = 0
                w2 = w
                dist2.append((o2,w2))
            else:
                dist2.append((o,w))
        outcome2 = sample_outcome(dist2)
        # If it's still "WIDE" or "NOBALL" keep treating specially (rare)
        if outcome2 == "WIDE":
            inning.runs += 1
            inning.comments.append("Extra wide on free-hit! +1 (ball repeated).")
            return False
        if outcome2 == "NOBALL":
            inning.runs += 1
            inning.comments.append("Another no-ball on free-hit! +1 (ball repeated).")
            return False
        # otherwise count the result but do not allow wicket
        if isinstance(outcome2, int):
            # run outcome (0,1,2,3,4,6)
            inning.runs += outcome2
            inning.balls += 1
            inning.comments.append(f"Free-hit: {outcome2} runs.")
            return True
        else:
            # fallback
            inning.balls += 1
            inning.comments.append("Strange free-hit outcome.")
            return True

    # Normal legal outcome
    if outcome == -1:
        # wicket falls
        inning.wickets += 1
        inning.balls += 1
        inning.comments.append("WICKET! Batsman is out.")
    elif isinstance(outcome, int):
        inning.runs += outcome
        inning.balls += 1
        if outcome == 0:
            inning.comments.append("Dot ball.")
        else:
            inning.comments.append(f"{outcome} run{'s' if outcome>1 else ''}.")
    else:
        # should not reach
        inning.balls += 1
        inning.comments.append("Unknown outcome.")
    return True

# ---------------------------
# High level game
# ---------------------------

def play_match():
    slowprint("Welcome to Terminal Cricket! 🎮🏏", 0.03)
    # Choose overs
    try:
        overs = int(input("Enter number of overs per innings (default 2 for quick game): ").strip() or "2")
        if overs <= 0:
            overs = 2
    except Exception:
        overs = 2

    # Toss
    slowprint("Toss time...")
    toss_call = choose("Call toss: heads or tails?", ["heads", "tails"])
    toss = random.choice(["heads", "tails"])
    player_won_toss = (toss_call == toss)
    slowprint(f"Toss result: {toss}.", 0.02)
    if player_won_toss:
        slowprint("You won the toss!")
        decision = choose("Choose to bat or bowl?", ["bat","bowl"])
        player_bats_first = (decision == "bat")
    else:
        slowprint("CPU won the toss.")
        # CPU decides: simple heuristic choose to chase when overs small else bat
        cpu_decision = random.choices(["bat","bowl"], weights=[6,4])[0]
        slowprint(f"CPU chooses to {cpu_decision}.")
        player_bats_first = (cpu_decision == "bowl")  # if CPU bats, player bowls so player_bats_first=False

    # First innings
    slowprint("\n--- First Innings ---\n")
    first_innings = Innings(overs, batting_is_human=player_bats_first, target=None)
    play_innings(first_innings, human_batting=player_bats_first)

    slowprint(f"End of first innings: {first_innings.summary()}\n", 0.01)

    # Second innings (chase)
    target = first_innings.runs
    slowprint(f"Target for second innings: {target+1} runs.\n")
    second_innings = Innings(overs, batting_is_human=not player_bats_first, target=target)
    play_innings(second_innings, human_batting=not player_bats_first)

    slowprint(f"End of match: First {first_innings.summary()} | Second {second_innings.summary()}\n")
    # Determine result
    if second_innings.runs > target:
        # chasing side won
        winner = "You" if second_innings.batting_is_human else "CPU"
        slowprint(f"{winner} won the match!", 0.03)
        # margin
        if second_innings.batting_is_human:
            # player chased
            balls_left = second_innings.balls_remaining()
            slowprint(f"You won by {10 - second_innings.wickets} wickets with {balls_left} balls remaining.")
        else:
            runs_margin = second_innings.runs - target
            slowprint(f"CPU won by {runs_margin} runs.")
    elif second_innings.runs == target:
        slowprint("Match tied!")
    else:
        # defending side won
        winner = "You" if first_innings.batting_is_human else "CPU"
        slowprint(f"{winner} won the match!", 0.03)
        if first_innings.batting_is_human:
            # player defended
            runs_margin = first_innings.runs - second_innings.runs
            slowprint(f"You won by {runs_margin} runs.")
        else:
            runs_margin = first_innings.runs - second_innings.runs
            slowprint(f"CPU won by {runs_margin} runs.")

def play_innings(inning: Innings, human_batting=True):
    slowprint(f"{'You' if human_batting else 'CPU'} batting. Overs: {inning.overs}")
    while not inning.is_finished():
        o,b = inning.over_and_ball()
        # New over prompt (if human batting and start of over)
        if b == 0:
            slowprint(f"\nOver {o+1} begins. Score: {inning.runs}/{inning.wickets} ({inning.balls} balls)", 0.01)
        # Choose batting or bowling choices depending on who is human
        if human_batting:
            bat_choice = choose("Choose shot: defensive (def), normal (norm), aggressive (agg)", ["def","norm","agg"])
            # CPU bowls: choose bowl type
            bowl_choice = random.choice(['fast','spin','line'])
            # Show CPU bowl choice occasionally to make it interesting
            slowprint(f"CPU bowls: {bowl_choice}")
            legal = play_ball(inning, bat_choice=bat_choice, bowl_choice=bowl_choice, human_batting=True)
        else:
            # CPU batting, human bowling
            # human chooses bowl type
            bowl_choice = choose("Choose your bowl: fast, spin, line", ["fast","spin","line"])
            # CPU chooses shot automatically inside play_ball
            legal = play_ball(inning, bat_choice=None, bowl_choice=bowl_choice, human_batting=False)

        # print last comment
        if inning.comments:
            slowprint(inning.comments[-1], 0.01)

        # If chasing, show target and remaining
        if inning.target is not None:
            need = inning.target - inning.runs + 1
            if need <= 0:
                break
            balls_left = inning.balls_remaining()
            slowprint(f"Need {need} off {balls_left} balls. Score: {inning.runs}/{inning.wickets}", 0.01)
        else:
            slowprint(f"Score: {inning.runs}/{inning.wickets} in {inning.balls//6}.{inning.balls%6} overs", 0.01)

        # If ball was illegal (wide/noball), we did not increment legal ball - loop continues without counting
        # But if inning ended because of target, break
        if inning.is_finished():
            break

# ---------------------------
# Run the game
# ---------------------------
if __name__ == "__main__":
    random.seed()  # system seed
    play_match()
