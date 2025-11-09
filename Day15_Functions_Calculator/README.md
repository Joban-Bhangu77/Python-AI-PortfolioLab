# 🧠 Day 15 – Python Functions and Calculator Project
# 
#
# This script demonstrates core Python function concepts and includes a mini-project:
# a Simple Calculator using modular functions.

# --- Function Examples ---

### Fuction Definition
def greet():
    """Prints a simple greeting."""
    print("Hello from a function..!!")

# Call the simple function
# greet()

### Function with Parameters and Return Value
def add_example(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Example call:
# result = add_example(5, 3)
# print(f"Add Example Result: {result}")

### Function with Default Argument
def greet_user(name="Jobanjit"):
    """Greets a user, using a default name if none is provided."""
    print(f"Welcome, {name}!")

# Example calls:
# greet_user()
# greet_user("Python Enthusiast")

### Local vs Global Variables
x = 10  # global variable

def test_scope():
    """Demonstrates variable scope (local vs global)."""
    x = 5  # local variable (only exists inside this function)
    print("Inside function (local x):", x)

# Call the scope test function
# test_scope()
# print("Outside function (global x):", x)

# ----------------------------------------------------
# 💻 Mini Project – Simple Calculator
# ----------------------------------------------------

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers, handles division by zero error."""
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

def calculator():
    """
    Main function for the Simple Python Calculator project.
    Takes user input for operation and two numbers, then calls the
    appropriate arithmetic function.
    """
    print("\n" + "="*40)
    print("🧮 Welcome to the Python Calculator!")
    print("Select operation: +, -, *, /")
    print("="*40)
    
    # Input handling
    try:
        operation = input("Enter operation: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number

---

## 🔑 Key Takeaways

1.  **Readability and Debugging:** Breaking the calculator into separate `add`, `subtract`, etc., functions makes the main program flow clean and easy to debug.
2.  **Reusability:** Each arithmetic function can now be reused instantly in any other part of the program or future projects without needing to rewrite the logic.
3.  **Error Handling:** The `divide` function was a key practice point for incorporating basic error handling (checking for division by zero) directly within the function logic.

---

## 🏁 Conclusion

**Day 15** marks a crucial pivot in the learning journey: the transition from sequential scripts to **modular, professional code**.

By successfully building the Simple Calculator using dedicated functions, I have solidified my confidence in defining logical boundaries within code and embracing the principles of **Don't Repeat Yourself (DRY)**. This foundation is essential, as functions form the backbone for creating scalable applications, sophisticated automation scripts, and complex data processing pipelines in future AI-related projects.

From here onward, I will integrate **loops, conditionals, and functions** together to create increasingly advanced mini-projects.

---