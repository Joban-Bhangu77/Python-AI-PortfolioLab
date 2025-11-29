🌟 Day 29 – Python Functions, Args/Kwargs, Lambda & Smart Calculator

Part of the Python & AI – 90 Days Journey

📘 Overview

Today’s focus was on strengthening Python functions by learning:

Function arguments

Default parameters

*args and **kwargs

Lambda (anonymous) functions

A hands-on mini project: Smart Calculator

These concepts help build clean, reusable, and scalable code — essential for automation, AI, DevOps, and backend scripting.

🧠 What I Learned Today
🔹 1. Function Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

🔹 2. Default Arguments
def welcome(name="Guest"):
    print("Welcome,", name)

🔹 3. *args (Multiple Positional Arguments)
def add_numbers(*nums):
    return sum(nums)

🔹 4. **kwargs (Multiple Keyword Arguments)
def user_info(**details):
    print(details)

🔹 5. Lambda Functions
square = lambda x: x * x
add = lambda a, b: a + b

🤖 Mini Project – Smart Calculator

A command-line calculator that supports addition, subtraction, multiplication, and division.

✔️ Smart Calculator Code
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
        return "❌ Cannot divide by zero!"
    return a / b

def smart_calculator():
    print("\n🤖 Smart Calculator – Joban Edition 🤖")
    print("\nSelect Operation:")
    print("1️⃣ Add")
    print("2️⃣ Subtract")
    print("3️⃣ Multiply")
    print("4️⃣ Divide")

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
        print("❌ Invalid Option")

🚀 Key Takeaways

Functions improve modularity and reusability

*args and **kwargs allow flexible input handling

Lambda functions simplify logic

Smart Calculator builds strong logic and reinforces function concepts

These fundamentals are essential for AI, automation, and real-world programming

🎯 Final Thoughts

Day 29 boosted my understanding of structured, clean, and reusable Python code.
You're leveling up with every single day — keep pushing forward! 💪🔥