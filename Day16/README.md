# 🐍 Day 16 – Advanced Functions in Python

### 📅 Python & AI 90 Days Journey  
Welcome to **Day 16** of my Python & AI 90 Days Journey!  
Today’s focus is on mastering **Advanced Functions** in Python — one of the most important concepts for writing clean, reusable, and efficient code.

---

## 🔍 Topics Covered
- ✅ Default Parameters  
- ✅ Keyword Arguments  
- ✅ Returning Values  
- ✅ Lambda (Anonymous) Functions  
- ✅ Variable Scope (Local vs Global)  
- ✅ Mini Calculator Project  

---

## 🧩 Code Implementation

```python
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

🧠 Project Overview

This day focuses on understanding how functions can become powerful tools when combined with parameters, return statements, and lambda expressions.

To put everything together, we built a Mini Calculator Project that supports:

➕ Addition

➖ Subtraction

✖️ Multiplication

➗ Division (with zero-handling)

This project shows how reusable logic can simplify larger programs.

📸 Screenshots
Code Screenshots	Output Screenshot

	

(Naming Convention: Day16_Code1.jpg, Day16_Code2.jpg, Day16_Output.jpg)

🧾 Key Takeaways

Default Arguments make your functions flexible.

Keyword Arguments improve readability and reduce errors.

Lambda Functions are perfect for short, one-line operations.

Scope helps understand how variables behave inside and outside functions.

A Mini Calculator shows real-world application of multiple concepts together.

🏁 Conclusion

Functions are at the heart of Python programming.
By mastering arguments, return types, and variable scope, we take a big step toward writing modular, efficient, and scalable code.

Each concept builds the foundation for the upcoming topics like Modules and Imports, which we’ll explore next.