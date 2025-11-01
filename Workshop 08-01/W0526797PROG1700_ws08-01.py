'''
temperatures = [14, 16, 18, 17, 20, 19, 15]
temperature_set = set(temperatures)

total = 0
for temp in temperature_set:
    total += temp

avg = total / len(temperature_set)
while True:
    print("what tempature do you want to add? press q to quit")
    new_temp = input()
    if new_temp.lower() == 'q':
        break
    temperature_set.add(int(new_temp))
print("Updated temperatures:", temperature_set)
print(f"New average temperature: {sum(temperature_set) / len(temperature_set):.0f}")
if temperature_set:
    print(f"The Lowest temperature was {min(temperature_set)}")
    print(f"The highest temperature was {max(temperature_set)}")
    warm_days = [temp for temp in temperature_set if temp > 18]
    # [new_thing for item in old_list if condition]
    print(f"Warm days (above 18°C): {warm_days}")

# --- 2. ---


books = {
    "Python Basics": (3, 0),
    "Web Design 101": (2, 0),
    "Networking Made Easy": (1, 0),
}

while True:
    for title, (available, borrowed) in books.items():
        print(f"{title:25} Available: {available}, Borrowed: {borrowed}")
    action = input("Do you want to borrow or return a book? ('done' to finish): ")
    if action.lower() == 'borrow':
        title = input("Enter the book title: ")
        if title in books:
            available, borrowed = books[title]
            if available > 0:
                books[title] = (available - 1, borrowed + 1)
                print(f"You have borrowed '{title}'.")
                print(f"Available copies: {books[title][0]}, Borrowed copies: {books[title][1]}")
            else:
                print(f"All copies of '{title}' have been borrowed.")
        else:
            print(f"Book '{title}' not found in library.")
    elif action.lower() == 'return':
        title = input("Enter the book title: ")
        if title in books:
            available, borrowed = books[title]
            if borrowed > 0:
                books[title] = (available + 1, borrowed - 1)
                print(f"You have returned '{title}'.")
                print(f"Available copies: {books[title][0]}, Borrowed copies: {books[title][1]}")
            else:
                print(f"You cannot return '{title}' if you don't have the book.")
        else:
            print(f"Book '{title}' not found in library.")
    elif action.lower() == 'done':
        break
'''

# --- 3. ---


items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

item_sales = set(zip(items, sales))

while True:
    print("enter a new item to add sales for (q to quit):")
    new_item = input()
    if new_item.lower() == 'q':
        break
    new_sales = input(f"Enter sales for {new_item}: ")
    if new_sales.isdigit():
        items.append(new_item)
        sales.append(int(new_sales))
    else:
        print("Invalid sales number. Please enter a valid number.")
print("Item Sales Report")
print("------------------")
for item, sale in zip(items, sales):
    message = (f"{item:15} | {'*' * sale} ({sale})")
    if sale == max(sales):
        message += ("💸")
    print(message)

print("Total sales:", sum(sales))
print(f"Average sales: {sum(sales) / len(sales):.0f}")
print(f"{items[sales.index(max(sales))]} is the best seller with {max(sales)} sales!!!")