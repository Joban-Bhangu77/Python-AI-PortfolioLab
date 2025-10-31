Day 7 - Advanced Conditional Statements in Python

This project demonstrates advanced conditional statements in Python, including if-elif-else, nested conditions, match-case statements (Python 3.10+), and inline (ternary) conditions.

🔹 Project Overview

Python conditional statements allow you to control the flow of a program by executing code only when certain conditions are met. This project covers:

🔹Basic if-elif-else statements – Decide outcomes based on multiple conditions.

🔹Nested if statements – Handle multiple conditions within a single branch.

🔹Match-case statements – Python 3.10+ syntax for clean, readable multi-condition checks.

🔹Inline (ternary) conditions – Compact syntax for simple condition-based assignments.

🔹 Code Examples

1️⃣ Basic if-elif-else
temperature = 25

if temperature > 30:
    print("It's a hot day! ☀️")
elif temperature > 20:
    print("It's a nice day! 🌤️")
else:
    print("It's cold outside! ❄️")

2️⃣ Nested if
age = 18
has_id = True

if age >= 18:
    if has_id:
        print("Access Granted ✅")
    else:
        print("ID Required ❌")

3️⃣ Match-case (Python 3.10+)
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week 💼")
    case "Friday":
        print("Weekend is near 🎉")
    case "Sunday":
        print("Rest day 😴")
    case _:
        print("Midweek hustle 🔥")

4️⃣ Inline (Ternary) Condition
number = 7
result = "Even ✅" if number % 2 == 0 else "Odd ❌"
print(result)

🔹 Folder Structure
Day7_Advanced_Conditional_Statements/
├── Day7_Conditional_Logic.py
├── README.md
└── Screenshots/
    ├── Day7_GitHub_Push.jpg
    ├── Day7_Program_Output.jpg
    └── Day7_Folder_Structure.jpg

🔹 References

1. Python Official Documentation – Control Flow Tools
https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools

2. Real Python – Python Match Case
https://realpython.com/python-match-case/

3. W3Schools – Python Conditional Operators
https://www.w3schools.com/python/python_operators.asp

4. GeeksforGeeks – Python if, elif, else Statements
https://www.geeksforgeeks.org/python-if-else/

5. Programiz – Python Ternary Operator
https://www.programiz.com/python-programming/ternary-operator


🔹 Conclusion

Today’s project on Advanced Conditional Statements in Python helped reinforce the concept of controlling program flow using multiple decision-making techniques. By exploring:

if-elif-else statements for basic condition checks

Nested if statements for handling multiple levels of logic

Match-case statements (Python 3.10+) for readable multi-condition handling

Inline ternary operators for concise conditional assignments

I  now have a stronger grasp of how Python handles decision-making scenarios. Mastering these concepts is crucial for building robust, efficient, and readable Python applications.