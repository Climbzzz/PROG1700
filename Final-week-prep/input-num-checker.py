def input_num_checker(num1, num2, exitcode):
    while True:
        try:
            selection = int(input(f"\nEnter a valid number ({num1}-{num2}). {exitcode} to exit: "))

            if selection == exitcode:
                print("Exiting program.")
                break

            if selection and num1 <= int(selection) <= num2:
                print("Valid number:", selection)

            if selection < num1 or selection > num2:
                print("Invalid number, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

input_num_checker(1, 26, 0)