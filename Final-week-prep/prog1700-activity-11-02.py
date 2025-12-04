import os
import time

#opens a text file and returns its content as a string
def read_file_to_string(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    files = [
        filename,
        os.path.join(script_dir, filename)
    ]

    for path in files:
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                return fh.read()
        except FileNotFoundError:
            continue

    print(f"File not found or is empty: {filename}")
    return ""

def main():
    print("Simple TXT File Reader\n") 

    while True:
        filename = input("Enter a .txt file to open (or 0 to exit): ").strip()

        if filename == "0":
            print("Exiting program", end="", flush=True)
            for _ in range(3):
                time.sleep(1)
                print(".", end="", flush=True)
            print()
            break
          #little . fun

        if not filename.lower().endswith(".txt"):
            print("Error: You must provide a .txt file.\n")
            continue

        content = read_file_to_string(filename)

        print("\n--- FILE CONTENT ---")
        print(content)
        print("--------------------\n")

if __name__ == "__main__":
    main()
