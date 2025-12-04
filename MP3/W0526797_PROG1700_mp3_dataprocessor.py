import os
import time
import csv

def read_txt(filename: str) -> str:
    """Reads a TXT file and returns its contents as a string."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"TXT file not found: {filename}")
        return ""


def write_txt(filename: str, text: str):
    """Writes text to a TXT file (overwrites)."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"TXT file written: {filename}")
    except Exception as e:
        print(f"Error writing TXT: {e}")


def read_csv_file(filename: str) -> list:
    """Reads a CSV file and returns a list of rows."""
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"CSV file not found: {filename}")
        return []


def write_csv_file(filename: str, data: list):
    """Writes a list of rows to a CSV file (overwrites)."""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"CSV file written: {filename}")
    except Exception as e:
        print(f"Error writing CSV: {e}")


def main():
    print("TXT & CSV Reader/Writer\n")

    while True:
        print("Options:")
        print("1. Read TXT file")
        print("2. Write TXT file")
        print("3. Read CSV file")
        print("4. Write CSV file")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("Exiting...")
            break

        # --- READ TXT ---
        elif choice == "1":
            filename = input("Enter TXT filename: ").strip()
            if not filename.endswith(".txt"):
                print("Must end with .txt\n")
                continue
            content = read_txt(filename)
            print("\n--- TXT CONTENT ---")
            print(content)
            print("\n")

        # --- WRITE TXT ---
        elif choice == "2":
            filename = input("Enter TXT filename to write: ").strip()
            if not filename.endswith(".txt"):
                print("Must end with .txt\n")
                continue

            print("Enter text (type 'done' on its own line to finish):")
            lines = []
            while True:
                line = input()
                if line.lower() == "done":
                    break
                lines.append(line)

            write_txt(filename, "\n".join(lines) + "\n")

        # --- READ CSV ---
        elif choice == "3":
            filename = input("Enter CSV filename: ").strip()
            if not filename.endswith(".csv"):
                print("Must end with .csv\n")
                continue
            rows = read_csv_file(filename)
            print("\n--- CSV CONTENT ---")
            for row in rows:
                print(row)
            print("\n")

        # --- WRITE CSV ---
        elif choice == "4":
            filename = input("Enter CSV filename to write: ").strip()
            if not filename.endswith(".csv"):
                print("Must end with .csv\n")
                continue

            print("Enter CSV rows (comma separated). Type 'done' to finish.")
            data = []
            while True:
                row = input("Row: ")
                if row.lower() == "done":
                    break
                data.append([c.strip() for c in row.split(",")])

            write_csv_file(filename, data)

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()






#  _____       __ _           _   _             
# |  __ \     / _| |         | | (_)            
# | |__) |___| |_| | ___  ___| |_ _  ___  _ __  
# |  _  // _ \  _| |/ _ \/ __| __| |/ _ \| '_ \ 
# | | \ \  __/ | | |  __/ (__| |_| | (_) | | | |
# |_|  \_\___|_| |_|\___|\___|\__|_|\___/|_| |_|
# -------------------------------------------------

# --- 1. ---
# I stored multiple possible file paths inside a list so the program could try more than one location when opening a file.

# --- 2. ---
# The hardest bug I fixed was related to opening text files that weren’t in the same folder as the script.
# At first, the program only checked the filename directly, which caused “file not found” errors even when the file existed.

# --- 3. ---
# Saving data to a file makes the program far more useful because the information can be preserved between runs.

# --- 4. ---
# If I expanded the project, I would add a file browser menu that automatically lists all .txt files in the directory 
# so the user can choose from a numbered list instead of typing filenames manually.


