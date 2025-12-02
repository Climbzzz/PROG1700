import os

target_folder = r"C:\Users\W0526797\PROG1700\Final-week-prep"
print("Using folder:", target_folder)

while True:
    filename = input("Enter a .txt file name (0 to exit): ").strip()

    if filename == "0":
        break

    if not filename.lower().endswith(".txt"):
        print("Filename must end with .txt")
        continue

    full_path = os.path.join(target_folder, filename)
    print("Full path:", full_path)

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            print("\n--- File content ---")
            print(f.read())
            print("--------------------\n")
    except FileNotFoundError:
        print("File not found in", target_folder)