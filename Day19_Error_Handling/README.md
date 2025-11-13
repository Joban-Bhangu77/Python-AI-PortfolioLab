📘 Day 19: Error Handling in Python (try, except, else, finally)

✨ Part of the Python & AI — 90 Days Learning Journey

🧠 Overview: Error handling is a critical component of writing professional, stable, and user-friendly Python applications.
Instead of letting your program crash, Python allows you to gracefully manage errors, guide users, and ensure the program continues operating smoothly.

💎 Why Error Handling Matters
◆ Prevents unexpected program crashes
◆ Provides meaningful feedback to the user
◆ Helps developers debug smarter and faster
◆ Ensures smooth execution even with invalid input
◆ Makes applications production-ready and resilient

🧩 Mini Project — Number Division Program

This project demonstrates how to handle user input securely while performing a simple mathematical operation.
It covers real-world exception handling scenarios that every developer faces.

💎 The Program Handles
◆ ZeroDivisionError — When the user attempts to divide by zero
◆ ValueError — When a non-numeric value is entered
◆ Exception — Catches any unexpected errors
◆ else block — Runs only if no errors occur
◆ finally block — Always executes, used for cleanup or closing messages

🧪 Python Code — Day19_Error_Handling.py
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

🖼️ Screenshots

Add your screenshots inside the folder below:

Screenshots/
├── Day19_Code.jpg
└── Day19_Output.jpg


Include them in your README like this:

![Day 19 Code](Screenshots/Day19_Code.jpg)
![Day 19 Output](Screenshots/Day19_Output.jpg)

📂 Project Folder Structure
Day19_Error_Handling/
│── Day19_Error_Handling.py
│── README.md
└── Screenshots/
    ├── Day19_Code.jpg
    └── Day19_Output.jpg

🎯 What I Learned Today
💎 Key Takeaways

◆ What exceptions are and why they occur
◆ How to use try, except, else, and finally effectively
◆ How to prevent your code from crashing
◆ How to catch multiple error types
◆ How to build user-friendly and safe programs
◆ How structured error handling helps real-world applications

🏁 Conclusion

Day 19 elevates your Python skillset by teaching you how to write safe, stable, and professional-grade code.
With error handling, you now understand how to manage unexpected user behavior, avoid crashes, and keep your applications running smoothly.

