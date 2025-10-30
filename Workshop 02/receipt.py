item1 = input("Enter first item: ")
price1 = float(input("Enter price of first item: "))

item2 = input("Enter second item: ")
price2 = float(input("Enter price of second item: "))

item3 = input("Enter third item: ")
price3 = float(input("Enter price of third item: "))

total = price1 + price2 + price3

print("----- Receipt -----")
print(item1, ":", price1)
print(item2, ":", price2)
print(item3, ":", price3)
print("Total:", total)