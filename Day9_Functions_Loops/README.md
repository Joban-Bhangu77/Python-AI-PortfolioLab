Day 09 – Python Functions, Loops & Quiz Game

Repository: Python-AI-PortfolioLab

Day 9 focuses on strengthening Python fundamentals by learning:

Functions – reusable code blocks to make your program modular.

Loops – efficient iteration over data.

Mini Project – an interactive Quiz Game.

This project integrates these concepts in a hands-on, practical application, helping you practice clean coding, structured data management, and user interaction.

📌 Learning Objectives

By completing this project, you will be able to:

Define and call Python functions with parameters and return values.

Use default arguments in functions for flexibility.

Apply for and while loops for iteration.

Manage structured data using lists and dictionaries.

Build an interactive Quiz Game combining these concepts.

📝 Project Description

The Quiz Game is a console-based Python application that:

Prompts the user with multiple questions.

Provides immediate feedback on correct or wrong answers.

Tracks the score and displays it at the end.

Demonstrates modular coding using functions.

Uses loops to iterate through multiple questions efficiently.

⚡ Features

Interactive Q&A gameplay

Real-time score tracking

Case-insensitive answer validation

Modular design using a reusable function (ask_question)

Questions stored in a list of dictionaries for easy management

💻 Code Examples
1️⃣ Functions Basics
# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to Day 9 of Python practice.")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function with default parameter
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
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop example
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

3️⃣ Mini Project – Quiz Game
# Quiz Game using functions and loops
def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("🎉 Correct!")
        return 1
    else:
        print(f"❌ Wrong! The correct answer was: {answer}")
        return 0

# List of questions
quiz_questions = [
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Which hobby do you love most?", "answer": "Coding"}
]

score = 0
for q in quiz_questions:
    score += ask_question(q["question"], q["answer"])

print(f"\nYour final score is: {score} out of {len(quiz_questions)}")

📂 File Structure
Python-AI-PortfolioLab/
│
├── Day 9_Functions_Loops/
│   ├── Day 9_Functions_Loops.py      # Main Python script
│   ├── README.md                     # Documentation for Day 9
│   └── Screenshot/
│       ├── Day9_Program_Code1.jpg    # Screenshot of program code (part 1)
│       ├── Day9_Program_Code2.jpg    # Screenshot of program code (part 2)
│       └── Day9_Program_Output.jpg   # Screenshot of program output

💻 How to Run

Clone the repository:

git clone <your-repo-url>


Navigate to the Day 9 folder:

cd Python-AI-PortfolioLab/Day\ 9_Functions_Loops


Run the Python script:

python "Day 9_Functions_Loops.py"


Follow the on-screen prompts:

Enter your answers for each question.

Immediate feedback will be provided for each answer.

Your final score will be displayed at the end.

🖼 Screenshots

Day9_Program_Code1.jpg – First part of the Python script

Day9_Program_Code2.jpg – Second part of the Python script

Day9_Program_Output.jpg – Program output after execution

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

Functions: Make code modular and reusable.

Loops: Efficiently iterate through data.

Lists & Dictionaries: Manage structured data effectively.

Combining Functions and Loops: Build interactive and maintainable applications.

🏁 Conclusion

Day 9’s project strengthened my Python fundamentals by integrating functions, loops, and structured data into a practical Quiz Game. The hands-on approach reinforced the importance of modular coding, clean logic, and user interaction, which are crucial skills for building scalable Python applications. Mastering these concepts prepares me for more advanced projects in Python and AI development.

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