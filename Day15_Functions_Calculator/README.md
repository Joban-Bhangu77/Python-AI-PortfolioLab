# 🧠 Day 15 – Python Functions and Simple Calculator Project

***

## 🌟 Project Title: Modular Arithmetic with Python Functions


### **🗓️ Day 15 of Python & AI 90-Days Learning Journey**

---

## 🎯 Overview

In **Day 15**, the focus was on **Python Functions**—the core mechanism for creating organized, reusable, and efficient code. The learning culminated in developing a **Simple Python Calculator** that uses separate functions for each arithmetic operation, clearly demonstrating **modular programming**.

| **Key Feature** | **Functionality** |
| :--- | :--- |
| **Addition** | Implemented using a dedicated `add()` function. |
| **Subtraction** | Implemented using a dedicated `subtract()` function. |
| **Multiplication** | Implemented using a dedicated `multiply()` function. |
| **Division** | Implemented using a dedicated `divide()` function with **error handling** for division by zero. |

---

## 📚 Core Learning Objectives

| Concept | Status | Description |
| :--- | :--- | :--- |
| **Function Definition** | ✅ MASTERED | Defining reusable code blocks using the `def` keyword. |
| **Parameters & Arguments** | ✅ MASTERED | Passing data into functions for flexible operations. |
| **Return Statements** | ✅ MASTERED | Sending computed results back from functions. |
| **Modular Design** | ✅ APPLIED | Structuring a program with multiple, interconnected functions. |

---

## 💻 Programming Part: Code Implementation

### **File:** `day15_functions_calculator.py`

This is the core logic demonstrating the use of distinct functions for each operation and controlling the program flow using conditionals and loops.

```python
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers with error handling
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("🧮 Welcome to the Python Calculator!")
print("Select operation: +, -, *, /")

while True:
    choice = input("Enter operation: ")

    if choice in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")
        
        # Ask if the user wants another calculation
        next_calculation = input("Do you want another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Operation. Please select +, -, *, or /")

Sample Execution
The output below shows the result of running the script:

Console Example:

🧮 Welcome to the Python Calculator!
Select operation: +, -, *, /
Enter operation: +
Enter first number: 12
Enter second number: 8
Result: 20.0
🔑 Key Takeaways
Readability and Debugging: Breaking the calculator into separate functions (e.g., add, subtract) makes the main program flow clean and easy to debug.

Reusability (DRY Principle): Each arithmetic function can now be reused instantly in any other part of the program or future projects without needing to rewrite the core logic.

Robustness: The divide function was a key practice point for incorporating basic error handling (checking for division by zero) directly within the function logic, making the code more robust.

🏁 Conclusion
Day 15 marks a crucial pivot in the learning journey: the transition from sequential scripts to modular, professional code.

By successfully building the Simple Calculator using dedicated functions, I have solidified my confidence in defining logical boundaries within code and embracing the principles of Don't Repeat Yourself (DRY). This foundation is essential, as functions form the backbone for creating scalable applications, sophisticated automation scripts, and complex data processing pipelines in future AI-related projects.