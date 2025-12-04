🌟 Day 32 – User Input, Validation & Smart Python Calculator

Part of the Python & AI – 90 Days Journey

📘 Overview

Day 32 focuses on one of the most fundamental skills in Python — working with user input and building logic-driven programs that interact with real users.

These concepts form the backbone of many AI and automation workflows, including:

Chatbots

CLI-based utilities

Data collection & preprocessing

AI agents

Interactive automation tools

Today’s project includes:

Taking user input

Validating numeric values

Implementing a menu-driven calculator

Handling invalid cases (like division by zero)

Producing clean, meaningful output for users

This day builds both logic-building and error-handling muscles — essential for AI coding and future automation tasks.

🧠 What I Learned Today
🔹 1. Input Handling (input())

Accepting dynamic user data

Storing it in variables

Using it inside logic blocks

🔹 2. Input Validation (try/except)

Ensures the program never crashes and always guides the user properly.

🔹 3. Building Reusable Functions

Created a custom get_number() function that loops until valid numeric input is given.

🔹 4. Menu-Driven Program Design

User chooses operations like:

Add

Subtract

Multiply

Divide

Modulus

Power

🔹 5. Error Handling (Zero Division, Invalid Choices)

Handled multiple user mistakes gracefully.

🧪 Day 32 – Python Script
# Day 32 – User Input, Validation & Basic Calculator
# Part of Python & AI – 90 Days Journey

print("🔢 Welcome to Day 32 – Python User Input + Smart Calculator")
print("-----------------------------------------------------------")

# Ask user's name
user_name = input("What is your name? : ")
print(f"Hello, {user_name}! 👋 Let's build a smart calculator.\n")

# Function to safely get numeric input
def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid number! Please enter a numeric value.\n")

# Get two numbers
num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

# Display menu
print("\nChoose an operation:")
print("1 ➕ Add")
print("2 ➖ Subtract")
print("3 ✖ Multiply")
print("4 ➗ Divide")
print("5 🔢 Modulus")
print("6 ⚡ Power")

choice = input("\nEnter your choice (1/2/3/4/5/6): ")

result = None
operation = ""

# Logic for operations
if choice == "1":
    result = num1 + num2
    operation = "Addition"
elif choice == "2":
    result = num1 - num2
    operation = "Subtraction"
elif choice == "3":
    result = num1 * num2
    operation = "Multiplication"
elif choice == "4":
    if num2 == 0:
        print("\n❌ Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        operation = "Division"
elif choice == "5":
    result = num1 % num2
    operation = "Modulus"
elif choice == "6":
    result = num1 ** num2
    operation = "Power"
else:
    print("\n❌ Invalid choice! Please run again and select from 1–6.")

# Show result
if result is not None:
    print(f"\n✅ {operation} Result for {user_name}:")
    print(f"{num1} and {num2} → {result}")

print("\n🎉 Amazing work! You just completed Day 32 of your Python & AI Journey!")
print("-----------------------------------------------------------")

🚀 Key Takeaways

Reading and validating user input is the first real step toward building AI-ready applications.

Logic-based calculators strengthen algorithmic thinking.

Error handling prevents crashes and teaches you defensive programming.

This project forms the foundation for future interactive AI agents, data tools, and automation scripts.

📝 Mini Challenges (Optional)

Try enhancing the calculator by adding:

⭐ Repeat loop → "Do you want to calculate again?"
⭐ Square root, logarithm, rounding operations
⭐ Input validation with custom exceptions
⭐ Colorful outputs using Python colorama

These will take your Day 32 project to the next level.

🏁 Conclusion

Today’s milestone continues building your confidence and capability in Python.
You didn’t just code — you built an interactive system that thinks, reacts, and responds like a real application.

🔥 Day 32 completed. Onwards to Day 33!
Your Python foundation is getting stronger every day — keep going! 💪🐍