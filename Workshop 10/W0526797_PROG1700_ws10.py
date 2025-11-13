import csv
with open("results.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Operation", "Result"])


def calculate(a, b, op):
        match op:
            case '+':
                return add(a, b)
            case '-':
                return subtract(a, b)
            case '*':
                return multiply(a, b)
            case '/':
                return divide(a, b)
            case _:
                return "Invalid operator"
def add(a, b): return round(a + b)
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(num, b): 
    try:
        result = num / b
        if result < 1:
            raise ValueError
    except ZeroDivisionError:
        print("Cannot divide by 0.")
    return (f"{result:.03}")


while True:
    a = input("Input your number 'exit to finish': ")
    if a.lower() == 'exit':
        break
    else:
        num = int(a)
    op = input("enter operation: (+, -, *, /): ")
    b = int(input("Inpuit your second number: "))
    result = calculate (num, b, op)
    print(result)
print("thanks for calculatin' ")


#--- B ---
'''
def c_to_f(c):
    return (c * 9/5) + 32
    '''