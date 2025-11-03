## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** Function Builder Lab
* **Activity Type:** Guided Workshop / Lab
* **Duration:** 1.5–2.0 hours
* **Due:** See Brightspace
* **Submission Format:** Submit through **Brightspace**
* **File Naming Format:**
  `studentnumber_PROG1700_ws09-01.py`
  *Example:* `123456_PROG1700_ws09-01.py`

---

## **1. Activity Overview**

In this lab, you’ll transform repetitive code into reusable, modular components using **functions**.
This is your first step toward **structured programming**, where code becomes organized, readable, and easy to maintain.

You’ll create a small **function library** that performs everyday tasks like calculations, conversions, and input validation — preparing you for modular, persistent applications later in the course.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Write Python functions with and without parameters.
* Return results from functions using the `return` keyword.
* Reuse functions in a procedural program.
* Pass user input as function arguments.
* Apply modular programming concepts to real-world mini-tasks.

---

## **3. Concept Review / Lesson Content**

A **function** groups code that performs a specific task.

```python
def greet(name):
    print("Hello", name)

greet("Davis")
```

### Why Functions?

* Reusable — write once, use many times.
* Maintainable — easier to debug and expand.
* Organized — helps structure larger programs.

### Anatomy of a Function

```python
def add(a, b):          # definition
    result = a + b
    return result       # return value

print(add(3, 4))        # call
```

---

## **4. Integrated Tutorial / Guided Activities**

You’ll build three main functional mini-projects today.
Keep your code modular — each task in its own section with labeled comments.

---

### ➕ **A) Modular Calculator**

Create a simple four-operation calculator using **functions**.

**Steps:**

1. Write four functions:

   ```python
   def add(a, b): return a + b
   def subtract(a, b): return a - b
   def multiply(a, b): return a * b
   def divide(a, b): return a / b
   ```
2. Ask the user for two numbers and an operation symbol (`+, -, *, /`).
3. Use conditionals to call the correct function.
4. Print the result.

💡 **Try This:**

* Handle division by zero using an `if` check or `try/except`.
* Round results to 2 decimal places.
* Allow continuous calculations in a `while` loop until “exit”.

---

### 🔁 **B) Unit Converter**

Apply functions to convert between real-world units.

**Example conversions:**

* Kilometres ↔ Miles
* Celsius ↔ Fahrenheit
* Pounds ↔ Kilograms

**Example:**

```python
def c_to_f(c):
    return (c * 9/5) + 32
```

**Steps:**

1. Create a menu with 2–3 conversions.
2. Prompt for a value and direction.
3. Call the appropriate conversion function.
4. Print formatted results.

💡 **Try This:**

* Add input validation to reject non-numeric values.
* Format with 1 decimal precision.
* Allow multiple conversions in one session.

---

### ✅ **C) Validation Functions**

Create functions to check that input is valid before using it.

**Examples:**

```python
def is_positive(num):
    return num > 0

def is_integer(value):
    return value.isdigit()
```

**Steps:**

1. Use `input()` to get a user number or string.
2. Call validation functions before continuing.
3. Print feedback if the data is invalid.
4. Use a `while` loop to re-prompt until valid input is given.

💡 **Try This:**

* Use a counter to track how many invalid attempts were made.
* Combine with your calculator — validate inputs before calling math functions.

---

## **5. Reflection**

At the bottom of your `.py` file, add:

```python
# Reflection:
# 1. How did using functions change the structure of your code?
# 2. Which task (calculator, converter, validation) felt most useful?
# 3. How might modular code help on larger projects?
# 4. One real-world example where you would use functions in the future.
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws09-01.py`

Include:

* All three main sections (A–C)
* Comment headers for each part
* Reflection answers at the bottom

---

## **7. Submission**

* Submit via **Brightspace** (or GitHub).
* **Due:** End of class.
* Ensure code runs without syntax errors.
* Include your name and student number in the header.

---

## **8. Evaluation Criteria**

| Criteria   | Description                                             | Marks        |
| ---------- | ------------------------------------------------------- | ------------ |
| Completion | All three function challenges completed                 | 3            |
| Accuracy   | Functions perform correctly and return expected results | 3            |
| Modularity | Code is clean, reusable, and well-commented             | 2            |
| Reflection | Thoughtful responses provided                           | 2            |
| **Total**  |                                                         | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python Functions](https://www.w3schools.com/python/python_functions.asp)
* [Programiz – Defining and Calling Functions](https://www.programiz.com/python-programming/function)
* [Real Python – Defining Your Own Functions](https://realpython.com/defining-your-own-python-function/)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All code must be written individually.
You may discuss the logic, but do not share or copy code.
Include comments showing your reasoning.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.
