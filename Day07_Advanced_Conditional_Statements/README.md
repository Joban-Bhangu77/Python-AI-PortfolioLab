Day 7 - Advanced Conditional Statements in Python 🐍

This project demonstrates advanced conditional statements in Python, including if-elif-else, nested conditions, match-case statements (Python 3.10+), and inline (ternary) conditions.

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

📂 Folder Structure
Day7_Advanced_Conditional_Statements/
│
├── Day7_Conditional_Logic.py
├── README.md
└── Screenshots/
    ├── Day7_GitHub_Push.jpg
    ├── Day7_Program_Output.jpg
    └── Day7_Folder_Structure.jpg

🔗 References

Python Official Documentation – Control Flow Tools
https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools

Real Python – Python Match Case
https://realpython.com/python-match-case/

W3Schools – Python Conditional Operators
https://www.w3schools.com/python/python_operators.asp

GeeksforGeeks – Python if, elif, else Statements
https://www.geeksforgeeks.org/python-if-else/

Programiz – Python Ternary Operator
https://www.programiz.com/python-programming/ternary-operator

🏁 Conclusion

Day 7 helped me master Python decision-making techniques:

if-elif-else for basic conditional checks

Nested if for multi-level logic

Match-case statements (Python 3.10+) for clean multi-condition handling

Inline ternary operators for concise condition-based assignments

These concepts are essential for building robust, readable, and efficient Python programs.