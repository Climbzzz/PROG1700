import sys


def parse_amount(val: str, name: str) -> float:
	try:
		return float(val)
	except Exception:
		raise ValueError(f"Invalid {name}: must be a numeric value.")


def run_withdrawal(balance: float, withdrawal: float) -> int:
	"""Validate and perform withdrawal. Returns 0 on success, 1 on error."""
	if withdrawal <= 0:
		print("Error: Withdrawal amount must be greater than 0.")
		return 1
	if withdrawal > balance:
		print("Error: Insufficient funds.")
		return 1

	new_balance = balance - withdrawal
	print(f"New balance: ${new_balance:.2f}")
	return 0


def main(argv) -> int:
	if len(argv) == 3:
		try:
			balance = parse_amount(argv[1], "current balance")
			withdrawal = parse_amount(argv[2], "withdrawal amount")
		except ValueError as e:
			print(e)
			return 1
		return run_withdrawal(balance, withdrawal)
	try:
		bal_input = input("Enter current balance: ").strip()
		balance = parse_amount(bal_input, "current balance")
	except ValueError as e:
		print(e)
		return 1

	try:
		wd_input = input("Enter withdrawal amount: ").strip()
		withdrawal = parse_amount(wd_input, "withdrawal amount")
	except ValueError as e:
		print(e)
		return 1

	return run_withdrawal(balance, withdrawal)


if __name__ == "__main__":
	raise SystemExit(main(sys.argv))

