📘 Day 19: Error Handling in Python (try, except, else, finally)

✨ Part of the Python & AI — 90 Days Learning Journey

🧠 Overview

Error handling is a critical skill in professional Python development. When programs receive unexpected input or encounter invalid operations, they normally crash — but with proper error handling, you can:

💎 Respond to errors gracefully

💎 Guide the user with meaningful messages

💎 Prevent program failure

💎 Maintain code stability

💎 Build resilient real-world applications

Today’s lesson covers exception handling using Python’s four pillars:

try

except

else

finally

You also built a practical mini-project that demonstrates how real applications handle user errors.

🧩 Mini Project — Number Division Program

This simple yet powerful program demonstrates how to safely divide two numbers while handling all common user mistakes.

✔️ What the program handles:

💎 ZeroDivisionError → When the user tries dividing by zero

💎 ValueError → When the user enters non-numeric input

💎 General Exception → Unexpected errors

💎 else block → Executes only if no errors occur

💎 finally block → Runs no matter what, great for cleanup

🧪 Python Code (Day19_Error_Handling.py)

print("🔢 Welcome to Day 19 - Error Handling in Python!")

try:
    # Ask user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Attempt division
    result = num1 / num2

except ZeroDivisionError:
    print("❌ Error: You cannot divide a number by ZERO!")
except ValueError:
    print("❌ Error: Please enter numeric values only!")
except Exception as e:
    print("⚠️ Unexpected Error:", e)

else:
    # Runs only if no exception occurs
    print(f"✅ Result: {num1} ÷ {num2} = {result}")

finally:
    # Always runs
    print("📌 Program finished — thanks for using the calculator!")

  🖼️ Screenshots:

Place your screenshots in the following folder:

Screenshots/
├── Day19_Code.jpg
└── Day19_Output.jpg  

Add them to the README like this:

![Day 19 Code](Screenshots/Day19_Code.jpg)
![Day 19 Output](Screenshots/Day19_Output.jpg)

📂 Project Folder Structure:
Day19_Error_Handling/
│── Day19_Error_Handling.py
│── README.md
└── Screenshots/
    ├── Day19_Code.jpg
    └── Day19_Output.jpg

    🎯 What I Learned Today:

💎 What Python exceptions are

💎 Why programs crash and how to prevent it

💎 How try, except, else, and finally work together

💎 How to catch specific error types

💎 How to write user-friendly and safe programs

💎 How to build a practical mini-project using error handling

💎 How production-level code handles unexpected failures

🏁 Conclusion:

Day 19 strengthened your foundation in writing stable, crash-proof applications.
With strong error-handling skills, you are now prepared to move into more advanced Python concepts such as:

💎 File handling

💎 Working with APIs

💎 Data validation

💎 Exception classes

💎 Logging and debugging

