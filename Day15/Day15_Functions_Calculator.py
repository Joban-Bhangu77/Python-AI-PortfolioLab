### Fuction Definition
def greet():
    print("Hello from a function..!!")

###  Function with Parameters
def add(a, b):
    return a + b

### Function with Return Value
def greet_user(name="Jobanjit"):
    print(f"Welcome, {name}!")

### Local vs Global Variables
x = 10  # global

def test():
    x = 5  # local
    print("Inside function:", x)

test()
print("Outside function:", x)

###💻 Mini Project – Simple Calculator
# Day 15 - Functions and Calculator Project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

def calculator():
    print("🧮 Welcome to the Python Calculator!")
    print("Select operation: +, -, *, /")
    
    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")

calculator()
