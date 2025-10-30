## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** Tuples in Action – Immutable Data Adventures
* **Activity Type:** Guided Workshop / Lab
* **Duration:** 1.5 hours
* **Due:** End of class
* **Submission Format:**
  Submit through **Brightspace** or **GitHub**
* **File Naming Format:**
  `studentnumber_PROG1700_ws06-01.py`
  *Example:* `123456_PROG1700_ws06-01.py`

---

## **1. Activity Overview**

In this workshop, you’ll explore **tuples**, one of Python’s most useful immutable data structures.
You’ll learn how to:

* Represent grouped data using tuples
* Access and unpack tuple values
* Use loops to process tuples
* Simulate simple CRUD (Create, Read, Update, Delete) logic when data is immutable

By the end, you’ll understand *why* immutability matters and how tuples help make your code more predictable.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Create tuples and access their elements
* Use loops to process tuple data
* Simulate updates and replacements using new tuples
* Recognize when tuples are preferable to lists

---

## **3. Concept Review / Lesson Content**

A **tuple** is an ordered, immutable collection — you can’t change it directly after creation.

```python
# Tuple example
student = ("Alex", "A00123", "IT", 1)
print(student[0])  # Access by index
```

Tuples are perfect for representing **records** or **coordinates**.

You can **unpack** them for readability:

```python
name, id, program, year = student
print(f"{name} is in year {year} of {program}.")
```

They can also hold mixed data types (numbers, strings, lists, etc.).

---

## **4. Integrated Tutorial / Guided Activity**

### **Step 1 – Tuple Basics: Airline Ticket**

Create and print a simple travel record.

```python
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")
```

💡 **Challenge:**

* Unpack the tuple into variables and print a personalized message.
* Add an emoji flair: ✈️, 🧳, 🌎

---

### **Step 2 – Tuple Collections: Travel Itinerary**

Now create a **list of tuples**, each representing a flight.

```python
flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")
```

💡 **Challenge:**

* Use a **for loop** to print only flights cheaper than $150.
* Use a **while loop** to total up prices.
* Add a counter and print the **average ticket cost**.

---

### **Step 3 – Simulating Updates (Immutability in Action)**

Tuples can’t be changed — but you can *replace* them.

```python
flight = ("Halifax", "Toronto", 349.99)
print("Before:", flight)

# “Update” destination
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)
```

💡 **Challenge:**

* Write a function `update_flight(f, new_dest, new_price)` that returns a new tuple.
* Use loops to let a user “update” multiple records interactively.

---

### **Step 4 – Real-World Mini Challenge: Pizza Orders**

Represent pizza orders as tuples and store them in a list.

```python
orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]
```

💡 **Tasks:**

* Loop through all orders and print a neat summary:
  `"Alex ordered a Large pizza with Pepperoni & Mushroom."`
* Count how many Large pizzas were ordered.
* Use a **set** to find all **unique toppings** ordered.

---

## **5. Reflection**

Add the following reflection as comments at the end of your file:

```python
# Reflection:
# 1. Why are tuples useful if you can’t modify them?
# 2. In which step did immutability cause you to think differently?
# 3. Which exercise did you enjoy most, and why?
# 4. Give one example in real life where tuples make sense (e.g., coordinates, database records).
```

---

## **6. Deliverables**

Submit one `.py` file named:
`studentnumber_PROG1700_ws06-01.py`

Your file must include:

* All completed steps (1–4)
* Your improvements or added features
* Reflection answers as comments

---

## **7. Submission**

* Submit via **Brightspace** (or GitHub if instructed).
* **Due:** End of class.
* Ensure the file runs without syntax errors and includes your name and student number.

---

## **8. Evaluation Criteria**

| Criteria   | Description                                 | Marks        |
| ---------- | ------------------------------------------- | ------------ |
| Completion | All tuple examples and challenges completed | 3            |
| Accuracy   | Code executes correctly and logically       | 3            |
| Creativity | Student adds custom touches or extensions   | 2            |
| Reflection | Insightful, thoughtful answers              | 2            |
| **Total**  |                                             | **10 marks** |

---

## **9. Resources**

* [W3Schools: Python Tuples](https://www.w3schools.com/python/python_tuples.asp)
* [Real Python: Tuple Basics](https://realpython.com/python-tuples/)
* [Programiz: Python Data Structures](https://www.programiz.com/python-programming/tuple)
* VSCode with Python extension

---

## **10. Academic Integrity**

All work must be original.
Discussion with classmates is encouraged, but **code sharing is not allowed**.
Use comments to explain your thinking.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.