## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** File I/O & Persistence Lab
* **Activity Type:** Guided Workshop / Lab
* **Duration:** 1.5–2.0 hours
* **Due:** See Brightspace
* **Submission Format:** Submit through **Brightspace**
* **File Naming Format:**
  `studentnumber_PROG1700_ws10-01.py`
  *Example:* `123456_PROG1700_ws10-01.py`

---

## **1. Activity Overview**

In this workshop, you will learn to **store and retrieve data** using Python’s **file input/output (I/O)** features.
By extending the data-processing work from previous weeks (like Grocery Analyzer and Café Sales), you’ll now make your programs **persistent** — saving results to text or CSV files so data isn’t lost when the program ends.

You’ll complete four short tasks:

1. Write data to a text log.
2. Read from a text file.
3. Write data to a CSV file.
4. Read and process data from a CSV file.

These tasks show how modern programs keep track of results, user input, and analytics data in reusable files.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Use Python’s `open()`, `write()`, and `read()` functions to work with files.
* Safely handle files using `with` blocks to prevent errors.
* Write and parse comma-separated data (CSV).
* Combine loops, conditionals, and file I/O for persistence.

---

## **3. Concept Review / Lesson Content**

### Writing to a Text File

```python
with open("notes.txt", "w") as file:
    file.write("This is a text file.\n")
    file.write("It can store logs or messages.")
```

### Reading from a Text File

```python
with open("notes.txt", "r") as file:
    contents = file.read()
    print(contents)
```

### Writing to a CSV File

```python
import csv

with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Quantity", "Price"])
    writer.writerow(["Coffee", 3, 2.50])
```

### Reading from a CSV File

```python
import csv

with open("sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## **4. Integrated Tutorial / Guided Activities**

### 🧾 **A) Text Log – Daily Summary Writer**

Write a program that allows a user to record daily notes in a text file.

**Steps:**

1. Use a `while` loop to let the user enter daily messages (e.g., “Sold 15 coffees today”).
2. Each entry should append to a file called `daily_log.txt`.
3. Stop when the user types “done”.
4. After writing, reopen and print the file contents neatly.

💡 *Try This:*

* Add timestamps using `from datetime import datetime`.
* Count and display the total number of log entries.
* Prevent empty lines from being recorded.

---

### 📖 **B) Text Reader – Read Grocery Inventory**

Create a small text file called `inventory.txt` with lines like:

```
Apples,3.50
Bananas,2.75
Bread,2.99
```

**Steps:**

1. Open and read the file line by line.
2. Use `.split(",")` to separate name and price.
3. Convert prices to floats and calculate the **total inventory value**.
4. Print a neat report.

💡 *Try This:*

* Add an average item price.
* Handle blank or invalid lines with `try/except`.

---

### 💽 **C) CSV Writer – Café Sales Export**

Write a CSV file of café sales data.

```python
import csv

sales = [
    ["Latte", 12, 3.25],
    ["Tea", 10, 2.50],
    ["Muffin", 5, 2.00]
]

with open("cafe_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Quantity", "Price"])
    for row in sales:
        writer.writerow(row)
```

💡 *Try This:*

* Ask the user to enter more rows interactively.
* Calculate total revenue and append it as a final line.
* Ensure consistent formatting.

---

### 📊 **D) CSV Reader – Student Grades Report**

Create a CSV file named `grades.csv`:

```
Name,Grade
Ava,88
Noah,92
Liam,79
```

**Steps:**

1. Read the CSV and print each name + grade.
2. Calculate average grade.
3. Find the highest and lowest scores.
4. Write a new file, `grades_summary.txt`, summarizing your findings.

💡 *Try This:*

* Add a “Pass/Fail” result for each student.
* Include a timestamp in the summary file.

---

## **5. Reflection**

At the bottom of your `.py` file, add:

```python
# Reflection:
# 1. How does file persistence change what your program can do?
# 2. Which was easier to handle — text files or CSV files? Why?
# 3. What kind of program could use both file types together?
# 4. One problem you ran into and how you solved it.
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws10-01.py`

Include:

* All four tasks (A–D)
* Inline comments and reflection answers

---

## **7. Submission**

* Submit via **Brightspace** or GitHub
* **Due:** End of class
* Include your name and student number in the header
* Ensure all files (`.txt`, `.csv`) are saved in the same folder for testing

---

## **8. Evaluation Criteria**

| Criteria   | Description                       | Marks        |
| ---------- | --------------------------------- | ------------ |
| Completion | All four mini-projects complete   | 3            |
| Accuracy   | Code reads/writes files correctly | 3            |
| Creativity | Realistic data or enhancements    | 2            |
| Reflection | Clear and relevant responses      | 2            |
| **Total**  |                                   | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
* [Real Python – Reading & Writing Files](https://realpython.com/read-write-files-python/)
* [Programiz – Python CSV Handling](https://www.programiz.com/python-programming/csv)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All work must be original and created by you.
You may discuss ideas, but **do not share code**.
Use comments to show your thinking and credit external sources.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.

