📘 Day 19: Error Handling in Python (try, except, finally)

✨ Part of the Python & AI – 90 Days Learning Journey

🧠 Overview

Today’s focus was Error Handling — one of the most essential skills for writing reliable and production-ready Python applications.

Error handling allows your program to:

Stop unexpected crashes

Provide user-friendly error messages

Manage invalid inputs gracefully

Continue executing safely even when errors occur

In real-world software systems, proper error handling is critical for logging, debugging, user experience, and system stability.

🎯 Learning Objectives

By completing Day 19, you learned:

✅ What exceptions are in Python
✅ How try, except, else, and finally work
✅ How to catch multiple error types
✅ How to avoid program crashes
✅ How to write professional and safe code
✅ How to build a mini-project using error handling

## 🧩 Mini Project — Number Division Program

This program asks the user to input **two numbers** and performs division while safely handling all common errors.

## 🧩 Mini Project — Number Division Program

This program asks the user to input **two numbers** and performs division while safely handling all common errors.

### ✔️ The program handles:

- **ZeroDivisionError** – when the user tries to divide by zero → show a clear friendly warning  
- **ValueError** – when the user enters something that is not a number → ask the user to enter digits  
- **Exception** – any other unexpected error → show a debug-friendly message  
- **else block** – runs only when no error occurs → show the final result  
- **finally block** – always runs → display a program completion message  

🧪 Day19_Error_Handling.py
print("🔢 Welcome to Day 19 - Error Handling in Python!")

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

Add your images:

Day19_Code.jpg

Day19_Output.jpg

Then reference them inside README:

![Day 19 Code](Screenshots/Day19_Code.jpg)
![Day 19 Output](Screenshots/Day19_Output.jpg)

📂 Project Folder Structure
Day19_Error_Handling/
│── Day19_Error_Handling.py
│── README.md
└── Screenshots/
    ├── Day19_Code.jpg
    └── Day19_Output.jpg

🧠 Key Takeaways

🔹 Errors help identify bugs and weaknesses in code
🔹 try/except blocks make scripts stable and user-friendly
🔹 You can catch specific errors or general errors
🔹 else runs only when no error happens
🔹 finally always executes — good for cleanups
🔹 Proper error handling = professional-level coding

🏁 Conclusion

Day 19 strengthens your Python fundamentals by teaching you how to control the flow of your program even when things go wrong.

This is a crucial step toward becoming a professional Python developer, and prepares you for future topics like:

➡️ File handling
➡️ API error responses
➡️ Logging
➡️ Exception classes
➡️ Building robust real-world applications

Amazing progress, Joban — keep going! 🚀🔥