toppings = ["Pepperoni", "Mushroom", "Hot Peppers", "Cheese"]
t_str = "The toppings on the pizza are: "

for i in range(len(toppings)):
    if i < len(toppings) - 1:
        t_str += toppings[i] + " and "
    elif i == len(toppings) -1:
        t_str += toppings[i]
t_str += "."
print(f"{t_str}")