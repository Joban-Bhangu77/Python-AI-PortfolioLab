
print(" Welcome to Day 19 - Error Handling in Python!")

try:
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Attempt division
    result = num1 / num2

except ZeroDivisionError:
    print("Error: You cannot divide a number by ZERO!")
except ValueError:
    print("Error: Please enter numeric values only!")
except Exception as e:
    print("Unexpected Error:", e)

else:
    # Runs only if no exception occurs
    print(f"Result: {num1} ÷ {num2} = {result}")

finally:
    # Always runs
    print("Program finished — thanks for using the calculator!")
