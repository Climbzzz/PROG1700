groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}

total = 0
for item, price in groceries.items():
    print(f"{item:10} ${price:5.2f}")
    total += price
print(f"\nTotal cost: ${total:.2f}")