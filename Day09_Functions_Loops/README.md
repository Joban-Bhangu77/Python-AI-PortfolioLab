# 🚀 Day 9 – Python Functions, Loops & Quiz Game
**Repository:** [Python-AI-PortfolioLab](https://github.com/Joban-Bhangu77/Python-AI-PortfolioLab)

[![Python Version](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📌 Learning Objectives
By completing this project, you will learn to:

- ✅ Define and call Python functions with parameters and return values
- ✅ Use default arguments in functions for flexibility
- ✅ Apply `for` and `while` loops for iteration
- ✅ Manage structured data using lists and dictionaries
- ✅ Build an interactive Quiz Game combining these concepts

---

## 📝 Project Description
The **Quiz Game** is a console-based Python application that:

- Prompts the user with multiple questions
- Provides immediate feedback for correct or wrong answers
- Tracks the score and displays it at the end
- Demonstrates modular coding using functions
- Uses loops to iterate efficiently through questions

---

## ⚡ Features
- 🎮 Interactive Q&A gameplay
- 📊 Real-time score tracking
- 📝 Case-insensitive answer validation
- 🔄 Modular design with reusable function `ask_question`
- 📋 Questions stored in a list of dictionaries for easy management

---

## 🐍 Code Examples

### 1️⃣ Functions Basics
```python
def greet_user(name):
    print(f"Hello, {name}! Welcome to Day 9 of Python practice.")

def add_numbers(a, b):
    return a + b

def favorite_hobby(hobby="Coding"):
    print(f"My favorite hobby is {hobby}")

# Testing the functions
greet_user("Jobanjit")
result = add_numbers(5, 7)
print("Sum:", result)
favorite_hobby()
favorite_hobby("Soccer")

2️⃣ Loops Basics
# For loop example
for i in range(1, 6):
    print(i)

# While loop example
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

3️⃣ Mini Project – Quiz Game
def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("🎉 Correct!")
        return 1
    else:
        print(f"❌ Wrong! The correct answer was: {answer}")
        return 0

quiz_questions = [
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Which hobby do you love most?", "answer": "Coding"}
]

score = 0
for q in quiz_questions:
    score += ask_question(q["question"], q["answer"])

print(f"\nYour final score is: {score} out of {len(quiz_questions)}")

📂 Folder Structure
Python-AI-PortfolioLab/
│
├── Day 9_Functions_Loops/
│   ├── Day 9_Functions_Loops.py
│   ├── README.md
│   └── Screenshots/
│       ├── Day9_Program_Code1.jpg
│       ├── Day9_Program_Code2.jpg
│       ├── Day9_Program_Output.jpg
│       └── Day9_GitHub_Push.jpg

🔑 Sample Output
Hello, Jobanjit! Welcome to Day 9 of Python practice.

What is the capital of Canada? Ottawa
🎉 Correct!

What is 5 + 7? 12
🎉 Correct!

Which hobby do you love most? Coding
🎉 Correct!

Your final score is: 3 out of 3

💡 Key Takeaways

Functions: Modular and reusable code

Loops: Efficient iteration

Lists & Dictionaries: Structured data management

Combining Functions and Loops: Build interactive, maintainable apps

🔜 Next Steps

Randomize questions for dynamic gameplay

Add difficulty levels or a timer

Store questions in JSON/CSV for easy updates

Implement a leaderboard

Enhance UX with visual cues or emojis

🏁 Conclusion

Day 9 reinforced my understanding of Python functions, loops, and modular coding. Creating the Quiz Game helped me:

Apply theory into practical, interactive projects

Manage structured data effectively

Prepare for future AI and Python-based applications

🔗 References

Python Official Documentation – Functions
https://docs.python.org/3/tutorial/controlflow.html#defining-functions

W3Schools – Python Loops
https://www.w3schools.com/python/python_for_loops.asp

Real Python – Python Functions Guide
https://realpython.com/defining-your-own-python-function/

GeeksforGeeks – Python Lists & Dictionaries
https://www.geeksforgeeks.org/python-data-structures/

Programiz – Python Quiz Game Tutorial
https://www.programiz.com/python-programming/examples/quiz-game