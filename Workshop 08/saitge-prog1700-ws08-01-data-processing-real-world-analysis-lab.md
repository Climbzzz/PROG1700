## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** Data Processing & Real-World Analysis Lab
* **Activity Type:** Integrated Workshop / Lab
* **Duration:** 1.5–2.0 hours
* **Due:** See Brightspace
* **Submission Format:** Submit through **Brightspace**
* **File Naming Format:** `studentnumber_PROG1700_ws08-01.py`
  *Example:* `123456_PROG1700_ws08-01.py`

---

## **1. Activity Overview**

In this workshop, you’ll work through four practical mini-projects that apply loops and collections to real-world data.
Each scenario uses lists, sets, or dictionaries to **store**, **analyze**, and **report** data — just like beginner data automation tasks in workplaces.

All code will be written **procedurally** (no functions or methods) to strengthen logical thinking and flow control.

---

## **2. Learning Objectives**

By completing this workshop, you will be able to:

* Combine `for` and `while` loops with collection data types to manage and summarize data.
* Build simple data analysis scripts for real-world scenarios.
* Apply counting, filtering, and aggregation techniques using basic Python structures.
* Create readable, formatted console output.

---

## **3. Concept Review / Lesson Content**

Common patterns for analyzing data:

```python
# Loop through list
for item in my_list:
    ...

# Process dictionary
for key, value in my_dict.items():
    ...

# Validate input
while user_input != "done":
    ...
```

These patterns are the backbone of procedural programming — every task today will apply one or more of them.

---

## **4. Integrated Tutorial / Guided Activities**

You will complete **four short data-driven scenarios**, each reinforcing loops + data processing.

---

### 🌦️ **A) Weather Reporter**

Analyze and summarize a week of temperature data.

```python
temperatures = [14, 16, 18, 17, 20, 19, 15]

total = 0
for temp in temperatures:
    total += temp

avg = total / len(temperatures)
print("Average temperature:", avg)
```

💡 **Try This:**

* Add a `while` loop to allow entering new temperatures.
* Find and print the **highest** and **lowest** temperatures.
* Count how many days were above 18°C.
* Use a set to remove duplicate temperature readings.

---

### 📚 **B) Library Checkout Log**

Track books checked out using a dictionary.

```python
books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

for title, qty in books.items():
    print(f"{title:25} copies: {qty}")
```

💡 **Try This:**

* Use a `while` loop to check out or return books.
* Prevent negative quantities with a warning.
* Display the book with the fewest remaining copies.
* Print a summary showing total books in circulation.

---

### ☕ **C) Campus Café Sales**

Use lists to store sales and compute totals.

```python
items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]
```

💡 **Try This:**

* Print a formatted sales report.
* Calculate total and average sales per item.
* Add new items interactively in a `while` loop.
* Create a set of all **unique** menu items sold.
* Identify the **best-selling** item.

---

### 🐾 **D) Pet Adoption Tracker**

Keep a record of animal adoptions using dictionaries and sets.

```python
adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}

for species, count in adoptions.items():
    print(f"{species:10} adopted: {count}")
```

💡 **Try This:**

* Allow users to log more adoptions until “done.”
* Prevent negative totals or invalid entries.
* Store all animal types seen in a **set** (unique species).
* Print a report: total adoptions and most popular pet.

---

## **5. Reflection**

Add the following to the bottom of your `.py` file:

```python
# Reflection:
# 1. Which dataset (weather, library, café, or pets) was easiest to work with, and why?
# 2. How do loops make repetitive tasks faster in programming?
# 3. Which collection type (list, set, or dict) felt most useful today?
# 4. Describe one improvement you would make if this lab continued next week.
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws08-01.py`

Include:

* All four completed tasks (A–D)
* Clear comments labeling each section
* Reflection answers as comments at the end

---

## **7. Submission**

* Submit through **Brightspace** (or GitHub if instructed).
* **Due:** End of class.
* Ensure your file runs correctly with no syntax errors.
* Include your name and student number in file header.

---

## **8. Evaluation Criteria**

| Criteria   | Description                                       | Marks        |
| ---------- | ------------------------------------------------- | ------------ |
| Completion | All 4 tasks completed                             | 3            |
| Accuracy   | Code runs correctly and logic is valid            | 3            |
| Creativity | Personalized enhancements or realistic extensions | 2            |
| Reflection | Insightful, specific answers                      | 2            |
| **Total**  |                                                   | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python Lists, Sets, Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
* [Programiz – Python For Loop Examples](https://www.programiz.com/python-programming/for-loop)
* [Real Python – Data Structures in Python](https://realpython.com/python-data-structures/)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All code must be written individually.
You may discuss ideas, but do **not copy or share code**.
Use comments to explain your reasoning.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.