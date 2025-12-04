def validatefilename(filename):
    import re
    # Regular expression to match valid filenames (letters, numbers, underscores, hyphens) ending with .txt
    pattern = r'^[\w\-]+\.txt$'
    return re.match(pattern, filename) is not None
 
while True:
    userinput = input("Enter a filename (filename.txt) or 0 to exit: ").strip()
    # print(userinput)
 
    if userinput == "0":
        print("Exiting the program. Goodbye!")
        break
 
    if validatefilename(userinput):
        # print(f"Valid filename: {userinput}")
        try:
            with open(userinput, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"File not found: {userinput}. Please check the filename and try again.")
    else:
        print(f"Invalid filename: {userinput}. Ensure formate is 'filename.txt' with only letters, numbers, underscores, or hyphens.")