user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")

x = 7
y = 3

if x > 5 and y < 5:
    print("Case 1")
elif x < 5:
    print("Case 2")
else:
    print("Case 3")