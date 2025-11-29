# 🌟 Day 16 - Advanced Functions in Python

# 1️⃣ Default Parameters
def greet(name="Jobanjit", greeting="Welcome to Day 16!"):
    print(f"{greeting} {name}")

greet()
greet("Alice", "Good Morning")

# 2️⃣ Keyword Arguments
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info(age=29, name="Jobanjit", city="Toronto")

# 3️⃣ Returning Values
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)

# 4️⃣ Lambda Functions (Anonymous Functions)
square = lambda x: x ** 2
print("Square of 5:", square(5))

# 5️⃣ Scope Example
x = 100  # Global Variable

def modify_variable():
    x = 50  # Local Variable
    print("Inside function:", x)

modify_variable()
print("Outside function:", x)

# 6️⃣ Combine Concepts - Mini Calculator
def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"

print("Add:", calculator(10, 5))
print("Subtract:", calculator(10, 5, "subtract"))
print("Multiply:", calculator(10, 5, "multiply"))
print("Divide:", calculator(10, 5, "divide"))
