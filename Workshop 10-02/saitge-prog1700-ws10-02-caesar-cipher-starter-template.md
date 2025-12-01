Here’s a **student starter template** you can hand out for **Workshop 10 – Activity 01**.

* It’s **one file**: `studentnumber_PROG1700_ws10-01_caesar.py`
* Includes:

  * Header + placeholder for student info
  * Simple demo of **Method A** (alphabet + index) with a **WARNING** comment
  * Function stubs + TODOs for **Method B (ord/chr)** encryption & decryption
  * Function stub + TODOs for **brute-force** using `dictionary.txt`
  * A simple `main()` flow with clear TODO steps
  * Reflection block at the bottom

Students can fill in each TODO during the workshop.

---

```python
"""
PROG1700 – Logic & Programming
Workshop 10 – Activity 01: Caesar Cipher Encryption, Decryption & File I/O

File: studentnumber_PROG1700_ws10-01_caesar.py
Student Name: __________________________
Student Number: ________________________

Instructions:
- Complete the TODO sections.
- Use this file to:
    1. Encrypt plaintext.txt → ciphertext.txt
    2. Decrypt ciphertext.txt using the known step
    3. Experiment with brute-force decryption using dictionary.txt
    4. Answer the reflection questions at the bottom (in comments)
"""

import os
import csv   # may or may not be used – safe to leave
from datetime import datetime

# ============================================================
# SECTION 1 – (Demo) Method A: Alphabet String + index()
#           (FOR LEARNING ONLY – NOT THE MAIN SOLUTION)
# ============================================================

def demo_alphabet_index_method():
    """
    DEMO ONLY: This shows the basic idea behind using an alphabet string
    and index() to shift characters.

    IMPORTANT:
    - This method only supports: space + lowercase a–z
    - It breaks on punctuation, digits, and uppercase letters.
    - It is LESS flexible than the ord()/chr() method.
    - We will NOT use this as our primary solution.

    You DO NOT need to modify this function unless you want to experiment.
    """

    alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    text = input("[DEMO] Enter text (lowercase only, spaces allowed): ").strip().lower()
    key = int(input("[DEMO] Enter key (1–26): "))

    keyword = []

    if 0 < key <= 26:
        for letter in text:
            # WARNING: If letter not in alphabet, this will crash with ValueError.
            get_letter = alphabet.index(letter) + key
            keyword.append(alphabet[get_letter])
        print("[DEMO] Encrypted (alphabet/index method):", "".join(keyword))
    else:
        print("[DEMO] Key must be between 1 and 26.")


# ============================================================
# SECTION 2 – Method B: ord() and chr() (Preferred, Main Approach)
# ============================================================

def encrypt_char(ch: str, step: int) -> str:
    """
    Encrypt a single character using a Caesar shift.

    Rules:
    - If ch is in 'a'..'z': shift within lowercase range.
    - If ch is in 'A'..'Z': shift within uppercase range.
    - Otherwise: return ch unchanged (punctuation, digits, etc.)

    TODO:
      1. Detect lowercase letters and shift using base = ord('a').
      2. Detect uppercase letters and shift using base = ord('A').
      3. Leave other characters unchanged.
    """
    # TODO: Implement lowercase logic using ord()/chr()
    # TODO: Implement uppercase logic using ord()/chr()
    # TODO: Return shifted or unchanged character

    # Placeholder (for now, return the original character)
    return ch


def encrypt_text(plaintext: str, step: int) -> str:
    """
    Encrypt an entire string using encrypt_char() for each character.
    """
    ciphertext = ""
    for ch in plaintext:
        ciphertext += encrypt_char(ch, step)
    return ciphertext


def decrypt_char(ch: str, step: int) -> str:
    """
    Decrypt a single character using a Caesar shift.

    Rules:
    - Reverse the encryption (subtract the step instead of adding).
    - Use the same logic (lowercase, uppercase, others unchanged).

    TODO:
      1. Similar structure as encrypt_char, but subtract step instead.
    """
    # TODO: Implement lowercase logic for decryption
    # TODO: Implement uppercase logic for decryption
    # TODO: Return shifted or unchanged character

    # Placeholder
    return ch


def decrypt_text(ciphertext: str, step: int) -> str:
    """
    Decrypt an entire string using decrypt_char() for each character.
    """
    decrypted = ""
    for ch in ciphertext:
        decrypted += decrypt_char(ch, step)
    return decrypted


# ============================================================
# SECTION 3 – File I/O Helpers
# ============================================================

def read_file_to_string(filename: str) -> str:
    """
    Safely read a text file into a single string.

    TODO:
      1. Use a with-open block, mode 'r', encoding 'utf-8'.
      2. Return the file contents.
      3. Optionally handle FileNotFoundError and print a helpful message.
    """
    # TODO: Implement reading logic

    # Placeholder
    return ""


def write_string_to_file(filename: str, content: str) -> None:
    """
    Safely write a string to a text file (overwrite).

    TODO:
      1. Use a with-open block, mode 'w', encoding 'utf-8'.
      2. Write the content string to the file.
    """
    # TODO: Implement writing logic
    pass


# ============================================================
# SECTION 4 – Brute-Force Decryption (Preview / Exploration)
# ============================================================

def load_dictionary(filename: str) -> set:
    """
    Load dictionary.txt into a set of lowercase words.

    TODO:
      1. Read each line, strip whitespace, convert to lowercase.
      2. Add non-empty words to a set.
      3. Return the set.
    """
    words = set()
    # TODO: Implement dictionary loading
    return words


def brute_force_decrypt(ciphertext: str, dictionary_words: set) -> None:
    """
    Try all possible steps (1–25) and see which decrypted text
    contains the most matches with dictionary_words.

    This can help guess the key if we don't know it.

    TODO:
      1. Loop s from 1 to 25.
      2. For each s, decrypt the ciphertext using decrypt_text(ciphertext, s).
      3. Split the candidate text into words and clean punctuation.
      4. Count how many words appear in dictionary_words.
      5. Track and print the best match (step + sample text).
    """

    # TODO: Implement brute-force logic here
    # Hint: start with best_match_count = 0, best_step = None, best_text = ""
    pass


# ============================================================
# SECTION 5 – Main Flow
# ============================================================

def main():
    print("PROG1700 – Workshop 10 Activity 01: Caesar Cipher\n")

    # OPTIONAL: Uncomment to see the demo of Method A (alphabet/index approach)
    # demo_alphabet_index_method()

    # -----------------------------
    # Part 1 – Encryption
    # -----------------------------
    print("\n=== PART 1: ENCRYPTION (KNOWN STEP) ===")
    step = int(input("Enter shift value (1–26): "))

    # TODO:
    # 1. Read plaintext.txt into a string using read_file_to_string().
    plaintext = read_file_to_string("plaintext.txt")

    # 2. Encrypt using encrypt_text().
    ciphertext = encrypt_text(plaintext, step)

    # 3. Write ciphertext to ciphertext.txt using write_string_to_file().
    write_string_to_file("ciphertext.txt", ciphertext)

    print("Encryption complete. Output written to ciphertext.txt")

    # -----------------------------
    # Part 2 – Decryption (Known Step)
    # -----------------------------
    print("\n=== PART 2: DECRYPTION (KNOWN STEP) ===")

    # TODO:
    # 4. Read ciphertext.txt back in (or reuse ciphertext variable).
    cipher_in = read_file_to_string("ciphertext.txt")

    # 5. Decrypt using decrypt_text().
    decrypted = decrypt_text(cipher_in, step)

    # 6. Write decrypted text to decrypted_known_step.txt
    write_string_to_file("decrypted_known_step.txt", decrypted)

    print("Decryption complete. Output written to decrypted_known_step.txt")

    # -----------------------------
    # Part 3 – Brute-Force (Preview)
    # -----------------------------
    print("\n=== PART 3: BRUTE-FORCE PREVIEW (OPTIONAL / EXPLORATION) ===")
    choice = input("Try brute-force decryption using dictionary.txt? (y/n): ").lower()

    if choice == "y":
        # TODO:
        # 7. Load dictionary.txt using load_dictionary().
        dictionary_words = load_dictionary("dictionary.txt")

        # 8. Call brute_force_decrypt() with ciphertext and the dictionary set.
        brute_force_decrypt(cipher_in, dictionary_words)

    print("\nWorkshop 10 Activity 01 complete.\n")
    print("Remember to answer the reflection questions at the bottom of this file in comments.")


if __name__ == "__main__":
    main()

# ============================================================
# SECTION 6 – Reflection (ANSWER IN COMMENTS)
# ============================================================

# Reflection:
# 1. In plain language, what is the difference between encryption and decryption?
# 2. Why is Method B (ord/chr) generally superior to the alphabet-index approach?
# 3. What kinds of characters does your script preserve correctly?
# 4. How might a brute-force attack break a Caesar cipher easily?
# 5. What part of this activity helped you understand text processing the most?

