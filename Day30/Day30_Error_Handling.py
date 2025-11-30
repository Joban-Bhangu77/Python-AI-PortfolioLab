# 🌟 Day 30 – Python Error Handling & Debugging
# Part of the Python & AI – 90 Days Journey

print("🔧 Welcome to Day 30 – Error Handling & Debugging in Python!")

# --------------------------------------------------------------------
# 1. Basic Try/Except
# --------------------------------------------------------------------
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero!"
    except TypeError:
        return "❌ Error: Both inputs must be numbers!"

print("\n1️⃣ Basic Error Handling")
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("10", 5))


# --------------------------------------------------------------------
# 2. Try/Except/Else/Finally
# --------------------------------------------------------------------
print("\n2️⃣ Full Error Handling Structure")

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("❌ That's not a valid integer.")
else:
    print(f"✅ You entered a valid number: {number}")
finally:
    print("🔚 Input handling completed.")


# --------------------------------------------------------------------
# 3. Raising Your Own Errors
# --------------------------------------------------------------------
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Your age is {age}"

print("\n3️⃣ Raising Custom Errors")
try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as err:
    print("❌ Custom Error:", err)


# --------------------------------------------------------------------
# 4. Debugging with print() statements
# --------------------------------------------------------------------
print("\n4️⃣ Debugging Example")

def calculate_value(x):
    print("Debug -> Received:", x)
    result = x * 10
    print("Debug -> After multiplication:", result)
    return result

print("Final Output:", calculate_value(5))

# --------------------------------------------------------------------
# 5. Mini Project: Safe Calculator
# --------------------------------------------------------------------
print("\n5️⃣ Mini Project – Safe Calculator")

def safe_calculator():
    try:
        num1 = float(input("Enter number 1: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter number 2: "))

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "❌ Cannot divide by zero."
        else:
            return "❌ Invalid operator."

    except ValueError:
        return "❌ Invalid input — please enter numbers only."

print("Result:", safe_calculator())
