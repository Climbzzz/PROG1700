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
    # new_thing for item in old_list if condition
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


# --- 3. ---


items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

# Lists to store only user inputted items
user_items = []
user_sales = []

while True:
    new_item = input("Enter item name: ('q' to quit): ")

    if new_item.lower() == 'q':
        break
    try:
        new_sales = int(input("Enter sales: "))
    except ValueError:
        print("Invalid sales number. Please enter a valid number.")
    if new_item in items:
        index = items.index(new_item)
        sales[index] += new_sales
    else:
        items.append(new_item)
        sales.append(new_sales)

        # Add also to user-input lists
        user_items.append(new_item)
        user_sales.append(new_sales)

# all items
print("\nItem Sales Report")
print("------------------")
for item, sale in zip(items, sales):
    message = f"{item:15} | {'*' * sale} ({sale})"
    if sale == max(sales):
        message += "💸"
    print(message)

print("\nTotal sales:", sum(sales))
print(f"Average sales: {sum(sales) / len(sales):.0f}")
print(f"{items[sales.index(max(sales))]} is the best seller with {max(sales)} sales!!!")

# Chart for only user-inputted items
print("\nUnique Items Sold")
print("---------------------------")

if user_items:
    for item, sale in zip(user_items, user_sales):
        print(f"{item:15} | {'*' * sale} ({sale})")
    print(f"\nTotal user-inputted items: {len(user_items)}")
else:
    print("No user inputted items.")

    
# --- 4. ---

adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2,
    "Cats": 4,
    "Dogs": 6,
}

unique_species = set(adoptions.keys())

print(f"Current adoptions:")
print("------------------")
for species, count in adoptions.items():
    message = f"{species:10} | {'*' * count} ({count})"
    print(message)
while True:
        update = input(f"would you like to update or add a new adoption? 'q to end' (u/n/q): ")
        if update.lower() == 'u':
            species = input("Enter the species to update: ")
            if species in adoptions:
                try:
                    new_count = int(input(f"Enter the new adoption count for {species}: "))
                    if new_count < 0:
                        raise ValueError
                    adoptions[species] = new_count
                    print(f"Updated {species} adoptions to {new_count}.")
                except ValueError:
                    print("Cant enter a negative value. Please enter a valid integer.")
            else:
                print(f"{species} not found in the adoption list.")
        elif update.lower() == 'n':
            species = input("Enter the new species to add: ")
            try:
                count = int(input(f"Enter the adoption count for {species}: "))
                if count < 0:
                    raise ValueError
                adoptions[species] = count
                print(f"Added {species} with {count} adoptions.")
            except ValueError:
                print("Invalid number. Please enter a valid integer.")
        elif update.lower() == 'q':
            break
        else:
            print("Invalid option. Please enter 'u', 'n', or 'q'.")
print(f"Current adoptions:")
print("------------------")
for unique_species, count in adoptions.items():
    message = f"{unique_species:10} | {'*' * count} ({count})"
    if count == max(adoptions.values()):    
        message += f" {unique_species} has the most adoptions!"
    print(message)
print(f"Total adoptions: {sum(adoptions.values())}")


#  _____       __ _           _   _             
# |  __ \     / _| |         | | (_)            
# | |__) |___| |_| | ___  ___| |_ _  ___  _ __  
# |  _  // _ \  _| |/ _ \/ __| __| |/ _ \| '_ \ 
# | | \ \  __/ | | |  __/ (__| |_| | (_) | | | |
# |_|  \_\___|_| |_|\___|\___|\__|_|\___/|_| |_|


# 1. Weather was by far the easiest one. As you can have negative weather, you cant have negative pets or negative overall sales.


# 2. It makes it faster by not having to manually input everything, and can be quickly changed with a few inputs.


# 3. Set was by far the most useful. I used set a lot more than i had dict or list, it seems to be more of an important and more common code than list or dict.


# 4. one improvement i would do, is my efficency in writing and overall preformance for cleaner code and well structured sets, values, dictionaries, etc.