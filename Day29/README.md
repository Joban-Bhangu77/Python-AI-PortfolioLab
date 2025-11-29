Day 29 – Python Functions, Args/Kwargs, Lambda and Smart Calculator

Part of the Python & AI – 90 Days Journey

Overview

Today I practiced Python functions in depth, including:

Function arguments

Default parameters

*args

**kwargs

Lambda expressions

A complete Smart Calculator project

Concepts Practiced
1. Function Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Joban", 29)

2. Default Arguments
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Joban")

3. *args (Multiple Positional Arguments)
def add_numbers(*nums):
    return sum(nums)

print(add_numbers(10, 20, 30))

4. **kwargs (Multiple Keyword Arguments)
def user_info(**details):
    print(details)

user_info(name="Joban", country="Canada", role="Cloud Engineer")

5. Lambda Functions
square = lambda x: x * x
add = lambda a, b: a + b

print(square(7))
print(add(10, 20))

Smart Calculator Project (Full Code)
def add(*nums):
    return sum(nums)

def subtract(a, b):
    return a - b

def multiply(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def smart_calculator():
    print("\nSmart Calculator – Joban Edition")
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Result:", add(*numbers))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == "3":
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Result:", multiply(*numbers))

    elif choice == "4":
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result:", divide(a, b))

    else:
        print("Invalid Option")

smart_calculator()

Key Takeaways

Functions make code reusable and organized

*args and **kwargs allow flexible inputs

Lambda functions simplify small operations

The Smart Calculator helped practice logic flow and user input

These concepts form the base for automation, AI logic, and larger Python projects

Final Notes

Day 29 helped strengthen my core Python fundamentals and improved my function-writing confidence. On to Day 30 next!