import os
import csv
import string
from datetime import datetime

def demo_alphabet_index_method():
    alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    text = input("Enter text (lowercase only, spaces allowed): ").strip().lower()
    try:
        key = int(input("Enter key (1–26): "))
    except ValueError:
        print("Invalid key")
        return

    keyword = []

    if 0 < key <= 26:
        for letter in text:
            try:
                get_letter = alphabet.index(letter) + key
                keyword.append(alphabet[get_letter])
            except ValueError:
                keyword.append(letter)
        print("Encrypted (alphabet/index method):", "".join(keyword))
    else:
        print("Key must be between 1 and 26.")


def encrypt_char(ch: str, step: int) -> str:
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + step) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + step) % 26 + base)
    return ch


def encrypt_text(plaintext: str, step: int) -> str:
    return ''.join(encrypt_char(ch, step) for ch in plaintext)


def decrypt_char(ch: str, step: int) -> str:
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base - step) % 26 + base)
    if 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base - step) % 26 + base)
    return ch


def decrypt_text(ciphertext: str, step: int) -> str:
    return ''.join(decrypt_char(ch, step) for ch in ciphertext)


def read_file_to_string(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [filename, os.path.join(script_dir, filename)]

    for path in candidates:
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                return fh.read()
        except FileNotFoundError:
            continue

    print(f"File not found (tried): {candidates}")
    return ""


def write_string_to_file(filename: str, content: str) -> None:
    if os.path.isabs(filename) or os.path.dirname(filename):
        path = filename
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, filename)

    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(content)

    print(f"Wrote file: {path}")


def load_dictionary(filename: str) -> set:
    words = set()
    try:
        with open(filename, 'r', encoding='utf-8') as fh:
            for line in fh:
                w = line.strip().lower()
                if w:
                    words.add(w)
    except FileNotFoundError:
        print(f"Dictionary file not found: {filename}")
    return words


def main():
    print("PROG1700 – Workshop 10 Activity 01: Caesar Cipher\n")

    print("\n=== PART 1: ENCRYPTION ===")
    try:
        step = int(input("Enter shift value (1–26): "))
    except ValueError:
        print("Invalid step; defaulting to 3")
        step = 3

    plaintext = read_file_to_string("plaintext.txt")
    if not plaintext:
        print("plaintext.txt is empty or missing. You can still enter text manually.")
        plaintext = input("Enter plaintext to encrypt: \n")

    # Encrypt
    ciphertext = encrypt_text(plaintext, step)
    write_string_to_file("ciphertext.txt", ciphertext)

    print("Encryption complete. Output written to ciphertext.txt")

    # Summary
    print("\n--- PART 1: SUMMARY ---")
    print(f"Used shift value: {step}")
    preview_len = 400
    plain_preview = plaintext.replace('\n', ' \n ')[:preview_len]
    cipher_preview = ciphertext.replace('\n', ' \n ')[:preview_len]
    print("Plaintext preview:")
    print(plain_preview)
    print("\n=== PART 2: DECRYPTION ===")

    cipher_in = read_file_to_string("ciphertext.txt")
    if not cipher_in:
        cipher_in = ciphertext

    # Decrypt
    decrypted = decrypt_text(cipher_in, step)
    write_string_to_file("decrypted.txt", decrypted)

    print("Decryption complete. Output written to decrypted.txt")

    print("\nDecrypted preview:")
    print(cipher_preview)



if __name__ == "__main__":
    main()

print("\n")