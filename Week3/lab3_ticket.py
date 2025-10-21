def main():
    while True:
        age_input = input("Enter your age: ").strip()
        if not age_input:
            print("Please enter a value.")
            continue
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for age.")

    if age < 5:
        price = 0
    elif 5 <= age <= 12:
        price = 8
    elif 13 <= age <= 64:
        price = 12
    else:  # age >= 65
        price = 6

    if age >= 13:
        student = input("Are you a student? (yes/no): ").strip().lower()
        if student in ("yes", "y"):
            price = max(0, price - 2)

    print(f"Ticket price: ${price:.2f}")

if __name__ == "__main__":
    main()
