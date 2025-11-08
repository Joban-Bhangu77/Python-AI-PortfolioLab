# 🗓️ Day 7 – Conditional Statements in Python

## 🎯 Objective
Today’s goal was to master Python’s **decision-making statements** that allow your program to make intelligent choices based on certain conditions.  
You learned how to use **if, elif, else, nested if**, and advanced control structures like **match-case** and **ternary operators**.

---

## 🧠 Key Learning Topics
- `if`, `elif`, `else` conditions  
- Nested conditional logic  
- `match-case` statement (Python 3.10+)  
- Inline (Ternary) conditional expressions  

---

## 💻 Project File
**File Name:** `Day7_Conditional_Statements.py`

### 🧩 Code Overview
```python
# 1️⃣ Basic if-elif-else example
temperature = 25
 
if temperature > 30:
    print("It's is a hot day!")
elif temperature > 20:
    print("It's a nice day!")
else:
    print("It's cold outside!")

# 2️⃣ Nested if example
age = 18
has_id = True

if age >= 18:
    if has_id:
        print("Access Granted ✅")
    else:
        print("ID Required ❌")

# 3️⃣ Match-case example (Python 3.10+)
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

# 4️⃣ Inline (Ternary) condition
number = 7
result = "Even ✅" if number % 2 == 0 else "Odd ❌"
print(result)

🧩 Concept Demonstrations
🔹 If-Elif-Else

Controls logic flow based on multiple possible conditions.

🔹 Nested If

A conditional statement inside another if block — useful for layered checks.

🔹 Match-Case

A cleaner alternative to multiple if-elif chains (available in Python 3.10+).

🔹 Ternary Operator

Single-line shorthand for if-else — perfect for quick conditional assignments.

🧮 Output Example
It's a nice day!
Access Granted ✅
Start of the work week 💼
Odd ❌

📂 Folder Structure
Python-AI-PortfolioLab/
│
├── Day7_Conditional_Statements/
│   ├── Day7_Conditional_Statements.py
│   ├── Screenshots/
│   │   ├── Day7_Code1.jpg
│   │   ├── Day7_Code2.jpg
        ├── Day7_Program_Output.jpg
│   └── README.md
│
└── ...

🧭 How to Run

Open your terminal or VS Code and execute:

cd Python-AI-PortfolioLab/Day7_Conditional_Statements
python Day7_Conditional_Statements.py

🧾 Conclusion

✔ Learned how to make decisions in Python using if, elif, and else.
✔ Practiced nested conditions for complex logic.
✔ Explored the modern match-case structure.
✔ Applied ternary conditions for concise logic expressions.
✔ Strengthened your control flow foundation for upcoming projects.