
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
