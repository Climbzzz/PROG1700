## ![alt text](image.png)

---

## **1) Assignment Details**

* **Course:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Assignment Title:** MP3 – Data Processing & Persistence Challenge
* **Type:** Mini-Project (Individual)
* **Estimated Time:** 6 hours (over Weeks 9 – 10)
* **Due Date:** *(see Brightspace)*
* **Weight:** 15 % of final grade
* **File Naming:**
  `studentnumber_PROG1700_mp3_dataprocessor.py`
  *Example:* `A00123456_PROG1700_mp3_dataprocessor.py`

---

## **2) Overview / Purpose / Objectives**

This project challenges you to design and build a **data-processing utility** that reads structured text (CSV or TXT), performs meaningful analysis using loops and collections, and persists results to a file.

You will demonstrate the ability to:

* Work with Python collections (lists, tuples, sets, dictionaries).
* Implement modular functions for processing, validation, and reporting.
* Perform loop-based computation and data aggregation.
* Read and write text/CSV files using file I/O.
* Produce and analyze summary reports (saved to disk).

The result should be a **procedural, modular** program that automates a small, real-world task such as tracking, counting, filtering, or summarizing data.

---

## **3) Learning Outcomes Addressed**

| Outcome Code | Description                                                  |
| -----------: | ------------------------------------------------------------ |
|       **O1** | Translate logical rules into program code.                   |
|       **O2** | Apply input/output handling and file processing techniques.  |
|       **O3** | Use Python collections to store and manipulate data.         |
|       **O5** | Build modular, reusable functions to organize program logic. |
|       **O6** | Employ loops and control structures for data processing.     |
|       **O7** | Demonstrate debugging, testing, and reflection skills.       |

---

## **4) Assignment Description / Use Case**

You will choose **one of the following three use cases** (or propose your own with instructor approval):

### **Option A – Student Grades Analyzer**

* Read a `grades.csv` file containing student names and scores.
* Compute average, highest, lowest grades.
* Identify students above/below thresholds.
* Write a summary report to `grades_summary.txt`.

### **Option B – Inventory Tracker**

* Read an `inventory.csv` with items, quantities, and costs.
* Compute inventory value, reorder alerts, and sorted lists.
* Save summary report to `inventory_report.txt`.

### **Option C – Text Analytics (Term Frequency)**

* Read a `text_input.txt`.
* Count word frequency using a dictionary.
* Sort results by frequency.
* Save `word_frequency.csv` to disk.

---

## **5) Tasks / Instructions (Step-by-Step)**

### **Step 1 – Prepare Your Data**

* Create a small sample dataset for testing (e.g., 5–10 records).
* Ensure it is clean and well-formatted (CSV or TXT).
* Store it in the same directory as your Python file.

### **Step 2 – Plan Your Program**

Sketch the logic (flowchart or pseudocode):

* Read file
* Parse lines into collections
* Process (loop through data)
* Summarize (results dictionary or list)
* Write output to file
* Display key results to console

### **Step 3 – Implement File Reading**

```python
with open("grades.csv", "r") as f:
    for line in f:
        print(line.strip())
```

Use `split(",")` to break lines into fields.

### **Step 4 – Store Data in Collections**

Example:

```python
records = []
for line in f:
    name, score = line.strip().split(",")
    records.append((name, float(score)))
```

### **Step 5 – Process Data Using Loops and Conditions**

Compute totals, averages, counts, and apply filters.
Demonstrate both `for` and `while` loops at least once.

### **Step 6 – Use Functions for Modularity**

Define at least **three** functions:

```python
def read_file(filename): ...
def process_data(records): ...
def write_report(filename, summary): ...
```

Each should handle a distinct task.

### **Step 7 – Write Results to File**

Write summary output to a new file (`summary.txt`, `report.csv`, etc.).

### **Step 8 – Reflection**

At the bottom of your file (add as comments):

```python
# Reflection:
# 1) What collection type(s) did you use and why?
# 2) What was the hardest bug you fixed?
# 3) How does saving to a file make your program more useful?
# 4) If you expanded this project, what feature would you add?
```

---

## **6) Deliverables**

Submit the following:

1. **Python file** `studentnumber_PROG1700_mp3_dataprocessor.py`
2. **Input data file** (`grades.csv`, `inventory.csv`, or `text_input.txt`)
3. **Output file** (`summary.txt` or `report.csv`)

---

## **7) Assessment & Rubric (100 pts)**

| Category                        | Criteria                                                  |     Pts |
| ------------------------------- | --------------------------------------------------------- | ------: |
| **File I/O & Persistence**      | Reads and writes files correctly using `with open()`      |      15 |
| **Data Structures**             | Uses appropriate collections (lists, tuples, sets, dicts) |      15 |
| **Loops & Logic**               | Correct use of loops and conditional expressions          |      15 |
| **Functions & Modularity**      | Code organized into clear, reusable functions             |      15 |
| **Processing Accuracy**         | Correct summaries, calculations, and output format        |      15 |
| **Error Handling & Robustness** | Handles missing files or invalid input gracefully         |      10 |
| **Reflection & Style**          | Comments, answers, and professional presentation          |      15 |
| **Total**                       |                                                           | **100** |

---

## **8) Submission Guidelines**

* Submit via **Brightspace > Assignments > MP3 – Data Processor**.
* Ensure your Python file runs without errors in VS Code (Python 3.x).
* Verify your output files exist and contain readable data.
* Include name and student number in file header.

---

## **9) Resources / Equipment**

* Python 3.x installed
* VS Code with Python extension
* Course notes: Loops, Collections, Functions, File I/O
* Example files from Workshop 09 and 10

---

## **10) Academic Integrity**

All work must be your own.
Discuss ideas, not code. Cite any reference you used for logic or syntax.

---

## **11) Copyright Notice**

© 2025 Davis Boudreau – Educational use only (NSCC PROG1700).
