import sys

print("Simple ATM Withdrawal Program")
print("-----------------------------")

# Read current balance (repeat until a valid non-negative number is entered)
while True:
    bal_input = input("Enter current balance: ").strip()
    try:
        balance = float(bal_input)
        if balance < 0:
            print("Balance cannot be negative. Please try again.")
            continue
        break
    except Exception:
        print("Invalid input. Please enter a number like 100 or 100.50.")

# Read withdrawal amount (repeat until a valid positive number is entered)
while True:
    wd_input = input("Enter withdrawal amount: ").strip()
    try:
        withdrawal = float(wd_input)
        if withdrawal <= 0:
            print("Withdrawal must be greater than 0. Please try again.")
            continue
        break
    except Exception:
        print("Invalid input. Please enter a number like 25 or 25.00.")

# Validate and show result
if withdrawal > balance:
    print(f"Error: Insufficient funds. Your balance is ${balance:.2f}.")
    sys.exit(1)

new_balance = balance - withdrawal
print(f"Withdrawal successful. New balance: ${new_balance:.2f}")
sys.exit(0)