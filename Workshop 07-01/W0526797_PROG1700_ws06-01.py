
# --- 1. ---
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
flight_from = ticket[0]
flight_to = ticket[1]
flight_number = ticket[2]
flight_price = ticket[3]
print(f"A flight from {flight_from} 🧳 to {flight_to} 🌎 on flight ✈️  {flight_number} will cost ${flight_price}")


# --- 2. ---


flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

for origin, destination, price in flights:
    if price < 150:
        print(f"{origin} → {destination}: ${price} This flight is under $150! 🎉")
i = 0
total_price = 0
while i < len(flights):
    price = flights[i][2] 
    total_price += price
    i += 1
print(f"Total price of all flights: ${total_price}")


# -- 3. ---


flight = ("Halifax", "Toronto", 349.99)
print("Before:", flight)

# “Update” destination
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

def update_flight(flight, new_dest, new_price):
    return (flight[0], new_dest, new_price)
while True:
    new_destination = input("Enter new destination: ")
    try:
        new_price = float(input("Enter new price: "))
        break
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
updated_flight = update_flight(flight, new_destination, new_price)
print("Updated flight:", updated_flight)


# -- 4. ---


toppings = ["Pepperoni", "Mushroom", "Hot Peppers", "Cheese"]
t_str = "The toppings on the pizza are: "

for i in range(len(toppings)):
    if i < len(toppings) - 1:
        t_str += toppings[i] + " and "
    elif i == len(toppings) -1:
        t_str += toppings[i]
t_str += "."
print(f"{t_str}")