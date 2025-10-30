## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** Data Processing & Integration Labs
* **Activity Type:** Integrated Workshop / Lab
* **Duration:** 1.5 - 3 hours
* **Due:** See Brightspace
* **Submission Format:** Submit through **Brightspace**
* **File Naming Format:** `studentnumber_PROG1700_ws07-02.py`
  *Example:* `123456_PROG1700_ws07-02.py`

---

## **1. Activity Overview**

In this two-part workshop, you’ll combine everything you’ve learned about **lists**, **sets**, and **dictionaries** with **loops** to analyze and process data in simple but realistic scenarios.

You’ll build **four small programs**, each reinforcing different loop and data-handling patterns.
All programs should use **procedural code only** — no functions or classes — to strengthen your foundational understanding of program flow and iteration.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Process and summarize collections using loops.
* Filter, count, and organize information in Python lists, sets, and dictionaries.
* Use `for` and `while` loops for aggregation and control flow.
* Apply procedural problem-solving techniques to small datasets.

---

## **3. Concept Review / Lesson Content**

Remember:
A **loop** + a **collection** = *the foundation of data processing.*

Common structures:

```python
# for over a list
for item in my_list: ...

# for over a dictionary
for key, value in my_dict.items(): ...

# while for control
while condition:
    ...
```

---

## **4. Integrated Tutorial / Guided Activities**

You will complete **four integrated mini-labs** below.
Each demonstrates a key real-world use of loops and collections.

---

### 🛒 **A) Grocery Analyzer**

Analyze store items using a dictionary and loop.

```python
groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}

total = 0
for item, price in groceries.items():
    print(f"{item:10} ${price:5.2f}")
    total += price
print(f"\nTotal cost: ${total:.2f}")
```

💡 **Try This:**

* Add a `while` loop to let users add more items and prices.
* Track number of items and find the **most expensive** one.
* Apply a **10% discount** to any item above $4.00.

---

### 🎓 **B) Student Tracker**

Manage a small grade tracker using lists and loops.

```python
students = ["Ava", "Noah", "Liam"]
grades = [88, 92, 79]

for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}")
```

💡 **Try This:**

* Add new students and grades in a `while` loop (until “done”).
* Calculate **average**, **highest**, and **lowest** grade.
* Create a set of “honour roll” students (grades ≥ 90).
* Add print formatting for clean, readable output.

---

### 🏀 **C) Game Scoreboard**

Use a dictionary to record scores during a simple tournament.

```python
scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

for name, points in scores.items():
    print(f"{name:10} {points} pts")
```

💡 **Try This:**

* Let the user update or add players in a loop.
* Keep looping until “done” is entered.
* Print the **top player** (max score).
* If any player exceeds 20 points, print a “Level Up!” message.

---

### 🎶 **D) Playlist Analyzer**

Work with a list of song titles and play counts.

```python
songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]
```

💡 **Try This:**

* Loop to print all songs with play counts.
* Find the **most played** and **least played** songs.
* Store unique songs in a set to remove duplicates.
* Calculate total plays and average per song.
* Bonus: allow user to add new songs interactively.

---

## **5. Reflection**

At the bottom of your `.py` file, include the following comments:

```python
# Reflection:
# 1. Which mini-project felt most realistic, and why?
# 2. How do loops make data handling easier?
# 3. What did you find challenging about combining loops with collections?
# 4. One idea for how you could expand any of these mini-projects.
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws07-02.py`

Include:

* All four integrated mini-projects (A–D)
* Comments labeling each section
* Reflection questions answered at the bottom

---

## **7. Submission**

* Submit via **Brightspace** or **GitHub**
* **Due:** End of Week 8
* Ensure the file runs without syntax errors.
* Include your name and student number at the top of the file.

---

## **8. Evaluation Criteria**

| Criteria   | Description                                    | Marks        |
| ---------- | ---------------------------------------------- | ------------ |
| Completion | All four mini-projects completed               | 3            |
| Accuracy   | Loops, collections, and outputs work correctly | 3            |
| Creativity | Personal enhancements or improved logic        | 2            |
| Reflection | Thoughtful answers demonstrating understanding | 2            |
| **Total**  |                                                | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python Loops & Data Structures](https://www.w3schools.com/python/python_for_loops.asp)
* [Programiz – Python Lists, Sets, Dictionaries](https://www.programiz.com/python-programming/dictionary)
* [Real Python – Iterating Over Data](https://realpython.com/python-for-loop/)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All work must be original.
You may discuss logic ideas, but do **not copy code**.
Comment your logic to demonstrate understanding.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.

