![alt text](image.png)

---

## **1. Activity Details**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Activity Title:** The Loop Lab – Practicing *while* Loops through Fun Challenges
* **Type:** Guided Tutorial / Class Activity
* **Duration:** 1.5 hours
* **Due Date:** See Brightspace
* **Submission Format:**

  * Submit via **Brightspace** or **GitHub**
  * **File Naming Format:** `studentnumber_PROG1700_ws09-01.py`
    *Example:* `123456_PROG1700_ws09-01.py`

---

## **2. Overview / Purpose / Objectives**

Loops make your programs dynamic and alive. Instead of writing the same code repeatedly, you can automate repetition until something changes.
This session will help you **master the `while` loop** through creative, simple, and fun examples that get progressively harder.

By the end, you’ll be able to:

* Build and control loops using conditions
* Avoid infinite loops through careful design
* Apply `break` and `continue` effectively
* Reflect on how repetition creates real-world functionality (games, counters, simulations)

---

## **3. Learning Outcomes Addressed**

* **O1:** Translate logic principles into programming code
* **O6:** Design and implement loops for repetition and control
* **O7:** Debug and test loops using IDE tools

---

## **4. Assignment Description / Use Case**

You will complete three creative mini-projects inside one Python file.
Each project introduces a basic loop pattern, and your task is to **improve it** with your own creative twist.

---

## **5. Tasks / Instructions**

### 🧮 **Step 1 – The Counting Machine**

Start with this base program:

```python
# Simple counting machine
count = 1
while count <= 5:
    print("Counting:", count)
    count += 1

print("Done counting!")
```

✅ **Run it:** See how it counts from 1 to 5.
💡 **Now improve it:**

* Make it count **down** from 10 to 1.
* Print a cool message for each step (e.g., “Launching in... 10 🚀”).
* Add `"Liftoff!"` at the end.

**Bonus:** Add a small `time.sleep(1)` delay between counts for dramatic effect.

---

### 🎯 **Step 2 – The Guessing Game 2.0**

Here’s your starter code:

```python
import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("Too low! 📉")
    elif guess > secret:
        print("Too high! 📈")
    else:
        print("You got it! 🎉")
```

💡 **Challenge Upgrades:**

* Add a **guess counter** and stop after **5 tries**.
* Print `"Game Over 😢"` if the player runs out of attempts.
* Award **points** (e.g., `score = 10 - attempts`) for guessing quickly.
* Add a **play again? (Y/N)** loop so players can restart.

**Hint:** Nesting loops is allowed—but watch your indentation!

---

### 🕹️ **Step 3 – Creative Challenge: “Loop Your Own Adventure”**

Design your own fun simulation using a `while` loop.
Choose *one idea* below or invent your own.

**Ideas:**

1. **🥤 Bubble Tea Simulator** – Keep drinking sips until the cup is empty.

   ```python
   sips = 5
   while sips > 0:
       print("You take a sip... 🧋")
       sips -= 1
   print("Cup empty. Refill time!")
   ```

   💡 Add: random “boba pearl” encounters or “brain freeze” warnings.

2. **🐍 Snake Growth Game** – Print a growing line of snakes until size 10.

   ```python
   snake = ""
   while len(snake) < 10:
       snake += "🐍"
       print(snake)
   print("The snake is full size!")
   ```

3. **🎲 Dice Battle** – Simulate dice rolls between two players until one wins 3 rounds.

   ```python
   import random
   player1_score = 0
   player2_score = 0

   while player1_score < 3 and player2_score < 3:
       roll1 = random.randint(1,6)
       roll2 = random.randint(1,6)
       print(f"Player1:{roll1} | Player2:{roll2}")
       if roll1 > roll2:
           player1_score += 1
       elif roll2 > roll1:
           player2_score += 1
   print("Winner:", "Player 1" if player1_score > player2_score else "Player 2")
   ```

💡 **Customize:** Add emojis, power-ups, or sound effects (`print("\a")`).

---

## **6. Deliverables**

Submit **one** Python file named:
`studentnumber_PROG1700_ws09-01.py`
It must include:

1. All three exercises (Counting Machine, Guessing Game, Creative Challenge)
2. Your customized improvements and creative changes
3. Reflection answers in comments

---

## **7. Reflection Questions**

At the bottom of your file, answer in comments:

```python
# Reflection:
# 1. What bug or mistake caused your first infinite loop today?
# 2. How did you fix it?
# 3. Which loop activity did you enjoy most, and why?
# 4. How might while loops be useful in a game or app you’d build someday?
```

---

## **8. Assessment & Rubric**

| Criteria   | Description                                     | Marks        |
| ---------- | ----------------------------------------------- | ------------ |
| Completion | All examples completed and improved             | 3            |
| Accuracy   | Code executes correctly without infinite loops  | 3            |
| Creativity | Unique or fun enhancements added                | 2            |
| Reflection | Answers demonstrate understanding and curiosity | 2            |
| **Total**  |                                                 | **10 marks** |

---

## **9. Submission Guidelines**

* Submit through **Brightspace** or **GitHub** before leaving class.
* Ensure your code runs without syntax errors.
* Include your name and student number at the top.

---

## **10. Resources / Equipment**

* Python 3.x
* VSCode (with Python extension)
* [W3Schools: Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
* [Real Python: Loop Patterns](https://realpython.com/python-while-loop/)
* Optional: `time` and `random` modules for extra fun

---

## **11. Academic Policies**

All code must be your own.
You may discuss ideas with classmates but **do not copy code**.
Comment your logic to show understanding.

---

## **12. Copyright Notice**

© 2025, Davis Boudreau – for educational use only.

