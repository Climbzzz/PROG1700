orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]

for name, size, toppings in orders:
    toppings_str = ""
    for i in toppings:
        toppings_str += i + " "
    print(f"{name} ordered a {size} pizza with {toppings_str}")