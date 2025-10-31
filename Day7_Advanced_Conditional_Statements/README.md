
Day 7 – Advanced Conditional Statements in Python

Learn and practice advanced conditional statements in Python, including:

✅ if-elif-else statements

✅ Nested conditions

✅ match-case statements (Python 3.10+)

✅ Inline (ternary) conditions

🔹 Project Overview

Conditional statements control the flow of a program, executing code only when certain conditions are met.

This project demonstrates:

🔹Basic if-elif-else – Decide outcomes based on multiple conditions.

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

🔹Expected Program Output:
It's a nice day!
Access Granted ✅
Start of the work week 💼
Odd ❌


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

This project helped strengthen my understanding of decision-making in Python:

if-elif-else for basic condition checks

Nested conditions for multi-level logic

match-case for cleaner multi-condition handling (Python 3.10+)

Inline ternary operators for concise conditional assignments

Mastering these concepts allows building robust, readable, and efficient Python applications.