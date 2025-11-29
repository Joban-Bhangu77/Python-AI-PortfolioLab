# 🌟 Day 12 – Conditional Logic & Student Grade Evaluator 🎓

Welcome to **Day 12** of the **Python & AI 90-Day Journey**!  
Today’s focus is on mastering **conditional logic** and applying it to a **real-world mini project** — a **Student Grade Evaluator System**.  

---

## 🧠 Learning Objectives

By the end of this lesson, you will be able to:

- Understand and implement `if`, `elif`, and `else` statements.  
- Use **logical operators** (`and`, `or`, `not`) to combine conditions.  
- Write structured conditional programs.  
- Build a real-world project that evaluates and displays grades dynamically.

---

## 🧩 Concept Overview

```python
# Example: Basic Conditional Logic
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")

Explanation:

The if statement checks the first condition.

The elif (else-if) allows for multiple condition checks.

The final else block executes when none of the above conditions are true.

🚀 Project: Student Grade Evaluator System

A simple yet practical Python program that takes a student’s name, subject, and marks, then evaluates their grade with remarks and eligibility for an honor roll.

📁 File Name

Day12_Conditional_Logic.py

💻 Source Code

# 🎓 Student Grade Evaluator System 🎓
print("🎓 Welcome to the Student Grade Evaluator System 🎓")

# Step 1: Take student details
name = input("Enter student name: ")
subject = input("Enter subject: ")

# Step 2: Input marks
marks = float(input(f"Enter marks for {subject} (out of 100): "))

# Step 3: Apply conditional logic
if marks >= 90:
    grade = "A+"
    remark = "Outstanding performance! Keep it up!"
elif marks >= 80:
    grade = "A"
    remark = "Excellent work!"
elif marks >= 70:
    grade = "B"
    remark = "Good effort!"
elif marks >= 60:
    grade = "C"
    remark = "Satisfactory. You can do better."
else:
    grade = "F"
    remark = "Needs improvement. Study harder!"

# Step 4: Display Result
print("\n📊 --- Student Report ---")
print(f"Name: {name}")
print(f"Subject: {subject}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Teacher's Remark: {remark}")

# Step 5: Bonus Feature
if grade in ["A+", "A"]:
    print("🏆 You are eligible for the Honor Roll!")


🧾 Example Output

🎓 Welcome to the Student Grade Evaluator System 🎓
Enter student name: Jobanjit
Enter subject: Python Basics
Enter marks for Python Basics (out of 100): 87

📊 --- Student Report ---
Name: Jobanjit
Subject: Python Basics
Marks: 87.0
Grade: A
Teacher's Remark: Excellent work!
🏆 You are eligible for the Honor Roll!

🧱 Folder Structure
Python-AI-PortfolioLab/
│
├── Day12_Conditional_Logic/
│   ├── Screenshot/
│   │   ├── Day12_Code1.jpg
│   │   ├── Day12_Code2.jpg
│   │   └── Day12_Output.jpg
│   ├── Day12_Conditional_Logic.py
│   └── README.md

⚙️ How to Run the Program

Open VS Code or any code editor.

Navigate to your project folder using the terminal:
cd Python-AI-PortfolioLab/Day12_Conditional_Logic

Run the Python script:
python Day12_Conditional_Logic.py

Enter the student’s details when prompted.

🧩 Key Concepts Covered

| Concept              | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `if`, `elif`, `else` | Conditional control flow in Python                   |
| Logical Operators    | Combine multiple conditions using `and`, `or`, `not` |
| User Input           | Capture user data with `input()`                     |
| Type Casting         | Convert strings to numeric types using `float()`     |
| f-Strings            | Format output for cleaner readability                |

🏁 Summary

In this lesson, you learned how to make your Python programs think and decide using conditional logic.
This foundation is crucial for developing smart AI systems and automation workflows later in your Python journey.