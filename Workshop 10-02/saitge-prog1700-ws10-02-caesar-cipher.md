## ![alt text](image.png)

---

## **Course Information**

* **Course Code:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** File I/O + Caesar Cipher Encryption & Decryption
* **Activity Number:** Activity 10-01
* **Duration:** 1.5–2.0 hours
* **Due:** End of class
* **Submission Format:** Brightspace or GitHub
* **File Naming Format:**
  `studentnumber_PROG1700_ws10-01_caesar.py`
  *Example:* `A00123456_PROG1700_ws10-01_caesar.py`

---

# **1. Activity Overview**

In this workshop, you will:

### 1) Learn the fundamentals of **encryption & decryption**

* plaintext vs ciphertext
* what a key (shift value) is
* how the Caesar cipher works

### 2) Implement **two different encryption approaches**

* **Approach A:** Alphabet string + `.index()` shifting *(simple but limited)*
* **Approach B:** Arithmetic shifting using `ord()` and `chr()` *(professional, robust)*

### 3) Create Python scripts that:

* **Encrypt** the contents of `plaintext.txt`
* **Write** the result to `ciphertext.txt`
* **Decrypt** ciphertext back to plaintext
* Explore a **brute-force decryption** approach using a dictionary file

### 4) Demonstrate file-handling skills

* read/write text files
* use `'r'`, `'w'`, `'a'` modes
* handle Unicode safely

This workshop prepares you for more advanced text-processing and cryptographic thinking while reinforcing loops, conditionals, string handling, and file persistence.

---

# **2. Learning Objectives**

After completing this activity, you will be able to:

* Define key encryption terms: plaintext, ciphertext, key, shift.
* Implement Caesar cipher logic using *two* techniques.
* Explain the **strengths and weaknesses** of each method.
* Apply loops, conditionals, functions, and string manipulation.
* Read from and write to text files using Python’s `open()` and `with`.
* Attempt brute-force decryption using a dictionary of English words.

---

# **3. Concept Review / Lesson Content**

---

## **3.1 Key Terms**

* **Plaintext:** The readable message.
* **Ciphertext:** Encrypted (scrambled) version of the message.
* **Encryption:** Plaintext → Ciphertext.
* **Decryption:** Ciphertext → Plaintext.
* **Key (Shift Value):** A number that determines how letters are shifted.
* **Caesar Cipher:** A shift cipher that moves letters by *n* positions in the alphabet.

---

## **3.2 Method A: Alphabet String + `.index()` Approach**

*(A quick-and-easy but limited way to implement a Caesar cipher)*

### Example Code:

```python
alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

get_letter = 0
keyword = []

text = str(input("Enter the text: ")).strip().lower()
key = int(input("Enter the key: "))

if 0 < key <= 26:
        for letter in text:
            get_letter = alphabet.index(letter) + key	
            keyword.append(alphabet[get_letter])
        print("".join(keyword) + " is the keyword!")
else:
    print("Key must be between 1 and 26!")
```

---

## **3.2.1 How This Works (Conceptually)**

* The alphabet string includes:
  `" abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"`
  (a space + two copies of `a–z` so shifting can wrap around easily).
* For each character in the text:

  * `alphabet.index(letter)` finds where the character appears in the alphabet.
  * Adding the key (`+ key`) shifts the index.
  * Appending `alphabet[get_letter]` collects the shifted letters.
* The second copy of the alphabet allows for wrap-around.

---

## **3.2.2 Critical Assessment — Limits & Drawbacks**

This method is a *good beginner insight* but has important limitations:

### **1) Only works for lowercase letters + space**

* Cannot handle:

  * uppercase letters
  * punctuation
  * digits
  * tabs/newlines
* If a character is *not* in the string, `.index()` → **ValueError**.

### **2) Space becomes an encrypted character**

* A space `' '` is part of the “alphabet” and also gets shifted into letters.
* This makes text less readable and harder to decrypt manually.

### **3) Requires duplicated alphabet string**

* The “repeat alphabet twice” technique is clever but not obvious.
* It hides the underlying logic instead of showing it clearly.

### **4) Inefficient for larger text**

* `.index(letter)` does a **linear search** each time → slower on large files.

### **5) Harder to extend**

Supporting uppercase?
Symbols?
Different alphabets?
Internationalization?

→ You must manually rebuild the alphabet string every time.

### **6) Not how professionals implement it**

Modern cryptography and even basic encoding use numeric transformations, not `.index()`-based lookups.

---

### **Bottom Line:**

This method is *okay* to understand conceptually,
but it is **not reusable**, **not robust**, and **not industry-aligned**.

Which is why we now move to…

---

# **3.3 Method B (Preferred): `ord()` and `chr()` Approach**

Using Unicode/ASCII code points gives us:

✔ explicit control
✔ automatic wrap-around
✔ separate handling of uppercase & lowercase
✔ ability to preserve spaces & punctuation
✔ a professional foundation for future topics

We use:

```python
ord('A')  # → 65
chr(65)   # → 'A'
```

Process:

1. Turn character into number: `n = ord(ch)`
2. Normalize to alphabetical index: `offset = n - base`
3. Apply shift (add for encrypt, subtract for decrypt)
4. Wrap with `% 26`
5. Convert back: `chr(base + new_offset)`

---

# **4. Integrated Tutorial / Guided Activities**

You will create **one script**:

`studentnumber_PROG1700_ws10-01_caesar.py`

It will include:

* Encryption using Method B (recommended)
* Decryption using known step
* Brute-force preview (optional but encouraged)

---

## **Step 1 — Encrypting plaintext.txt → ciphertext.txt**

### 1.1 Read the plaintext

```python
with open("plaintext.txt", "r", encoding="utf-8") as f:
    plaintext = f.read()
```

### 1.2 Get the step value from the user

```python
step = int(input("Enter shift value (1–26): "))
```

### 1.3 Encryption loop (ord/chr)

```python
ciphertext = ""

for ch in plaintext:
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        new_offset = (offset + step) % 26
        ciphertext += chr(base + new_offset)
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        new_offset = (offset + step) % 26
        ciphertext += chr(base + new_offset)
    else:
        ciphertext += ch    # leave punctuation/spaces unchanged
```

### 1.4 Write ciphertext

```python
with open("ciphertext.txt", "w", encoding="utf-8") as f:
    f.write(ciphertext)
```

---

## **Step 2 — Decrypting (When You Know the Step)**

Reverse the shift:

```python
decrypted = ""

for ch in ciphertext:
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        new_offset = (offset - step) % 26
        decrypted += chr(base + new_offset)
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        new_offset = (offset - step) % 26
        decrypted += chr(base + new_offset)
    else:
        decrypted += ch
```

Save to:

`decrypted_known_step.txt`

---

# **Step 3 — Brute-Force Decryption (Preview)**

*A quick look at how to decrypt when the key is unknown.*

### Load dictionary

```python
words = set()
with open("dictionary.txt", "r") as f:
    for line in f:
        words.add(line.strip().lower())
```

### Try all possible shifts

```python
best_match = 0
best_text = ""
best_step = None

for s in range(1,26):
    candidate = ""   # perform decryption using shift s
    # (same decryption loop as above but using s)
```

Check dictionary matches, find best candidate, display result.

---

# **5. Reflection**

Append these questions at the bottom of your `.py` file:

```python
# Reflection:
# 1. In plain language, what is the difference between encryption and decryption?
# 2. Why is Method B (ord/chr) generally superior to the alphabet-index approach?
# 3. What kinds of characters does your script preserve correctly?
# 4. How might a brute-force attack break a Caesar cipher easily?
# 5. What part of this activity helped you understand text processing the most?
```

---

# **6. Deliverables**

Submit:

✔ `studentnumber_PROG1700_ws10-01_caesar.py`
— includes encryption, decryption, brute-force attempt, and reflection

---

# **7. Submission**

* Upload to **Brightspace** (or GitHub if instructed)
* Ensure all text files (`plaintext.txt`, `ciphertext.txt`, `dictionary.txt`) are in the same folder
* Must run in VSCode using Python 3.x

---

# **8. Evaluation Criteria (10 marks)**

| Criteria         | Description                                              |  Marks |
| ---------------- | -------------------------------------------------------- | -----: |
| Encryption       | Correct Caesar shift implementation; file output correct |      3 |
| Decryption       | Reverse shift correct; readable output                   |      3 |
| Brute Force      | Reasonable attempt, dictionary usage, loops clear        |      2 |
| Reflection/Style | Answers thoughtful, code clean and commented             |      2 |
| **Total**        |                                                          | **10** |

---

# **9. Resources / Tools**

* `ord()`, `chr()` Python documentation
* W3Schools: File handling (`read()`, `write()`, `with`)
* Programiz: Strings and loops
* VSCode + Python Extension

---

# **10. Academic Integrity**

Work must be individually written.
Discuss ideas, but do not share or copy code.
Credit any external resources used for learning.

---

# **11. Copyright**

© 2025, Davis Boudreau – For educational use in PROG1700.

