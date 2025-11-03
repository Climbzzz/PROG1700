## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** File I/O & Persistence Lab (v1)
* **Activity Type:** Guided Workshop / Lab
* **Duration:** 1.5 – 2.0 hours
* **Due:** See Brightspace
* **Submission Format:** Submit through **Brightspace**
* **File Naming Format:** `studentnumber_PROG1700_ws10-00.py`
  *Example:* `123456_PROG1700_ws10-00.py`

---

## **1. Activity Overview**

This workshop builds directly on **Workshop 09 – Function Builder**, where you created modular calculators and converters.
Now you’ll extend those tools to **store and retrieve data** using **text** and **CSV files**.

By completing this activity, you’ll learn how to:

* Save user results for later reference,
* Load data from previous sessions, and
* Export summaries in a structured format.

Persistence is the next step toward full applications — it turns your short-lived programs into ones that *remember*.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Read and write to text and CSV files in Python.
* Integrate file I/O within modular programs.
* Append data safely without overwriting files.
* Produce simple logs and exports for reuse or analysis.

---

## **3. Concept Review / Lesson Content**

### Text Files

```python
with open("log.txt", "a") as file:
    file.write("Calculation: 3 + 4 = 7\n")
```

### CSV Files

```python
import csv
with open("results.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Operation", "Result"])
```

Use `"w"` to overwrite and `"a"` to append.
Always close files (or use `with`) to avoid corruption.

---

## **4. Integrated Tutorial / Guided Activities**

### 🧮 A) Modular Calculator with Text Logging

Extend your Workshop 09 calculator.

**Steps**

1. Copy or rewrite your arithmetic functions (`add`, `subtract`, `multiply`, `divide`).
2. Each time a calculation runs, append a line to `calc_log.txt` like:
   `5 * 3 = 15`
3. Add an option to view the entire log by reading and printing the file.

💡 *Try This:*

* Add a timestamp to each entry (`datetime.now()`).
* Use a `while` loop for multiple calculations.
* Add error handling for invalid numbers or division by zero.

---

### 🔁 B) Unit Converter with CSV Persistence

Re-use your converter functions from Workshop 09.

**Steps**

1. Ask the user to select a conversion (e.g., C↔F, km↔mi).
2. Perform the conversion and display the result.
3. Save the details to a CSV file called `conversions.csv` with columns:
   `Type,Input,Output`
4. At the end, read and display all previous conversions.

💡 *Try This:*

* Append to the file each time a conversion runs.
* Add a header row only if the file does not exist.
* Use `round(result, 2)` for clean formatting.

---

### 🧾 C) Combined Session Report

After running both programs, generate a simple summary text file (`session_summary.txt`) containing:

* Total calculations performed.
* Total conversions performed.
* Timestamp of session end.

💡 *Try This:*

* Use a counter to track calculations and conversions.
* Format the report using `f-strings` for clarity.

---

## **5. Reflection**

At the bottom of your `.py` file, add:

```python
# Reflection:
# 1. Why is file persistence important in real-world applications?
# 2. Which file type (text or CSV) felt more suitable for storing data? Why?
# 3. How did combining functions and file I/O change your code’s organization?
# 4. If you expanded this program, what would you store next?
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws10-00.py`

Include:

* Calculator + Converter modules
* File I/O integration (Text + CSV)
* Session summary and reflection

---

## **7. Submission**

* Submit through **Brightspace** or GitHub.
* **Due:** End of class.
* Ensure all files (`.txt`, `.csv`) are in the same folder for testing.
* Include your name and student number in the file header.

---

## **8. Evaluation Criteria**

| Criteria   | Description                            |     Marks    |
| :--------- | :------------------------------------- | :----------: |
| Completion | Both modules and I/O features complete |       3      |
| Accuracy   | Files read / write correctly           |       3      |
| Modularity | Functions and logic organized cleanly  |       2      |
| Reflection | Thoughtful answers included            |       2      |
| **Total**  |                                        | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
* [Programiz – Python CSV](https://www.programiz.com/python-programming/csv)
* [Real Python – Read/Write Files](https://realpython.com/read-write-files-python/)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All code must be your own. Discuss ideas but do not share solutions.
Comment each section to explain your approach.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.
