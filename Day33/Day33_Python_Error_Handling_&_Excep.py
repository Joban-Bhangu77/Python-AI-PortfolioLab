# Day 33 - Python Error Handling & Exceptions
# Python & AI – 90 Days Journey


print("✨ Welcome to Day 33 – Error Handling in Python!")

# ---------------------------
# 1. Basic Try-Except Example
# ---------------------------

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer!")


# --------------------------------------
# 2. Handling Multiple Exception Types
# --------------------------------------

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Only numbers are allowed!")


# ---------------------------
# 3. Try-Except-Finally Block
# ---------------------------

try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File does not exist!")
finally:
    print("‘finally’ block always runs!")
    

# ---------------------------
# 4. Raising Your Own Exception
# ---------------------------

age = 17
try:
    if age < 18:
        raise Exception("Access denied: Age must be 18+.")
    print("Access granted.")
except Exception as e:
    print("⚠️ Custom Error:", e)
