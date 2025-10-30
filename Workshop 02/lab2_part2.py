age_text = input("Enter your age: ")

if age_text.isdigit():
    age = int(age_text)
    if age >= 21:
        print("You are an adult.")
    else:
        print("You are a minor.")
        print(f"In 5 years you will be {age + 5}.")
else:
    print("That doesn't look like a number.")