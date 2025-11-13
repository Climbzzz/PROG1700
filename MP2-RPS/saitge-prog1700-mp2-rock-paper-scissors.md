##![alt text](image.png)

---

## 1) Assignment Details

* **Course:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Title:** RPS+ – Console Game with Modular Logic & Data Handling
* **Type:** Mini-Project (individual)
* **Estimated Time:** 4–6 hours
* **Due Date:** *(set in Brightspace)*
* **Suggested Weight:** 10–15% (scale to course plan)
* **File Naming:** `studentnumber_PROG1700_rps_plus.py`

  * *Example:* `A00123456_PROG1700_rps_plus.py`

---

## 2) Overview / Purpose / Objectives

Build a **playable, replayable** “Rock–Paper–Scissors” style game that demonstrates:

* **Week 3:** Conditional logic for outcomes
* **Week 5:** Use of **collections** (lists / sets / dictionaries)
* **Week 6:** **While loops** for continuous play and input validation
* **Weeks 7–8:** **Integration** of loops + collections for tracking results/history
* **Week 9:** **Functions** to structure and reuse logic (modular design)

The goal: a small but **well-structured** program that feels like a real mini-app, not a one-off script.

---

## 3) Learning Outcomes Addressed

* **O1:** Translate logic into code (outcome rules)
* **O3:** Use appropriate data structures (lists/sets/dicts)
* **O4:** Implement conditionals for decision-making
* **O5:** Build reusable functions (modularity)
* **O6:** Employ loops for iteration and control flow
* **O7:** Apply basic debugging/testing habits (e.g., trace prints, edge cases)

---

## 4) Assignment Description / Use Case

Create **RPS+**, a console game where a human plays against the computer.

**Minimum feature set**

* Classic **Rock–Paper–Scissors** with **best-of-N** match option (odd N: 3, 5, 7).
* Computer picks moves at random.
* **Valid input** only (reject/reprompt on invalid entries).
* **Scoreboard** that tracks wins/losses/ties per session.
* **Round history** list (or list of dicts) to show what happened each round.
* **Clean, readable output** for a quick demo.

**Design constraints**

* **Procedural Python** with **small functions** (no classes/OOP).
* Use only the **Python standard library** (`random`, `time`, etc.).
* Keep functions focused (e.g., `get_player_move()`, `get_cpu_move()`, `decide_winner()`, `play_round()`, `print_scoreboard()`, `print_history()`).

---

## 5) Tasks / Instructions (Step-by-Step)

### Part A — Game Core (logic + loop)

1. **Data setup (Week 5):**

   * `valid_moves = ["rock", "paper", "scissors"]` *(list)*
   * `valid_set = {"rock", "paper", "scissors"}` *(set for fast validation)*
   * `score = {"player": 0, "cpu": 0, "ties": 0}` *(dict scoreboard)*
   * `history = []` *(list of per-round dicts)*

2. **Functions (Week 9):**

   * `get_player_move(valid_set) -> str` (sanitize to lowercase; loop until valid)
   * `get_cpu_move(valid_moves) -> str` (random choice)
   * `decide_winner(player, cpu) -> str` returns `"player" | "cpu" | "tie"`
   * `print_scoreboard(score: dict) -> None`
   * `print_history(history: list) -> None` (print last N or all)

3. **Outcome rules (Week 3):**
   Conditionally determine who wins. Example rules mapping (choose your style):

   ```python
   wins_over = {("rock","scissors"), ("scissors","paper"), ("paper","rock")}
   ```

   If `(player, cpu)` in `wins_over` → player wins; reverse → cpu; same → tie.

4. **Main while loop (Week 6):**

   * Ask for **best-of-N** (odd only; validate).
   * Play rounds until either side reaches `ceil(N/2)` wins.
   * Update `score` and append a **round record** to `history`, e.g.:
     `{"round": 3, "player":"rock", "cpu":"scissors", "result":"player"}`
   * After match: show scoreboard and optionally **play again**.

### Part B — Integration Enhancements (Weeks 7–8)

Choose **at least two**:

* **Expanded move set:** add **“lizard”** and **“spock”** (update rules set + validation).
* **Streak tracker:** track max consecutive wins (extra counters/logic).
* **Simple analytics:** from `history`, compute most used move by player & CPU.
* **Friendly UX:** small delays (`time.sleep(0.3)`), clear separators, uppercase headings.
* **Accessibility tweak:** accept first letters (`r/p/s`) and expand to full move.

### Part C — Reflection (Week 9 habits)

Add answers as block comments at file end:

```python
# Reflection:
# 1) Which function was most useful to keep your code organized? Why?
# 2) What bug or edge case did you fix (describe inputs + expected vs actual)?
# 3) Which data structure (list/set/dict) felt best for each part (why)?
# 4) If you had one more hour, what improvement would you ship next?
```

---

## 6) Deliverables

* **One Python file**: `studentnumber_PROG1700_rps_plus.py`
* Contains: game core (A), at least **two** enhancements (B), reflection (C).
* Code **runs without errors** and is cleanly commented.

---

## 7) Assessment & Rubric (100 pts)

| Category                         | Criteria                                                       |     Pts |
| -------------------------------- | -------------------------------------------------------------- | ------: |
| **Core Gameplay**                | Valid input loop, random CPU, best-of-N, plays to completion   |      25 |
| **Outcome Logic**                | Correct conditional rules; all cases handled (win/lose/tie)    |      15 |
| **Collections Use**              | Appropriate lists/sets/dicts (validation, scoreboard, history) |      15 |
| **Modularity (Functions)**       | Clear, focused functions; minimal duplication; readable        |      20 |
| **Integration Enhancements**     | At least two from Part B implemented correctly                 |      15 |
| **Reflection & Professionalism** | Reflection quality; naming, comments, formatting               |      10 |
| **Total**                        |                                                                | **100** |

> **Instructor note:** scale to your weighting (e.g., 10–15%). Keep point ratios.

---

## 8) Submission Guidelines

* Submit to **Brightspace** (or GitHub Classroom, if specified).
* Include name & student number in a **header comment**.
* Only standard library modules.
* If you added non-obvious rules, include a **README note** in comments.

---

## 9) Resources / Equipment

* Python 3.x, VSCode (Python extension)
* Prior course labs (Weeks 3, 5, 6, 7–8, 9)
* Random module: `import random`
* (Optional) Time module: `import time`

---

## 10) Academic Policies

Work must be your own. Discussion is encouraged; **code sharing is not**.
Cite any snippets you looked up and explain them in comments.

---

## 11) Copyright Notice

© 2025, Davis Boudreau. Educational use only.

---