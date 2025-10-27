# 🧠 Day 3: Variables & Mini AI Guessing Game  

## 💻 Project Overview  
Day 3 of my Python learning journey combines **variables**, **data types**, and **basic logic** to simulate a **mini AI-style guessing game**.  

In this project, I explored how variables, lists, conditionals, and Python’s `random` module can mimic decision-making — a fundamental concept in Artificial Intelligence.  

---

## 🎯 Learning Objectives  
- Understand and implement **Python variables** (string, integer, float, boolean, list)  
- Learn how to **store, update, and manipulate** data  
- Use **conditional logic (`if-else`)** to create interactive behavior  
- Implement **randomness** to simulate “AI-like” decision-making  
- Strengthen **user interaction** with Python’s `input()` function  

---

## 💻 Project — “Variables & Mini AI Guessing Game”  

In this project, I combined Python fundamentals with a small AI-like guessing logic.  
The user tries to guess a random number between 1 and 10 — showing how logic and randomness can mimic simple decision-making behavior.  

---

## 🧠 Code Example  
```python
# day3_variables_ai.py

name = "Joban"
age = 25
height = 5.9
is_learning = True
hobbies = ["Coding", "Soccer", "Reading"]

print("Hello,", name)
print("Age:", age)
print("Height:", height)
print("Learning Python", is_learning)
print("Hobbies:", hobbies)

print("Age in 5 years:", age + 5)
print("Uppercase Name:", name.upper())
print("First Hobby:", hobbies[0])

import random

print("\nWelcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == number_to_guess:
    print("🎉 Congratulations! You guessed it right!")
else:
    print(f"❌ Sorry! The correct number was {number_to_guess}")

🧮 Output Preview:
Hello, Joban
Age: 25
Height: 5.9
Learning Python True
Hobbies: ['Coding', 'Soccer', 'Reading']
Age in 5 years: 30
Uppercase Name: JOBAN
First Hobby: Coding

Welcome to the Number Guessing Game!
Guess a number between 1 and 10:

📂 Folder Structure:
Day3_variable-ai/
│
├── day3_variables_ai.py
├── README.md
└── Screenshot/
    ├── day3_output.jpg
    ├── day3_folder_structure.jpg
    └── day3_github_repo.jpg

📘 Key Concepts Covered

Variables: Storing and manipulating data values

Data Types: String, Integer, Float, Boolean, List

Conditionals: Making logical decisions using if-else

Random Module: Introducing unpredictability with random.randint()

User Interaction: Taking input and displaying dynamic responses

## 🔗 References  

- [🐍 Python Official Documentation – Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)  
- [📘 W3Schools – Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)  
- [🧮 Real Python – Random Module Guide](https://realpython.com/python-random/)  
- [🎲 Python Official Documentation – Random Module](https://docs.python.org/3/library/random.html)  
- [💡 GeeksforGeeks – Python Variables](https://www.geeksforgeeks.org/python-variables/)  

## 🏁 Conclusion  

Day 3 was all about strengthening my foundation in Python.  
I explored how variables, data types, and simple logic can be combined to create dynamic behavior — just like the core decision-making process behind AI.  

By adding a small number guessing game, I applied concepts like user input, conditional statements, and randomness, which simulate the unpredictability and learning nature of AI systems.  

This project marks another step forward in my journey toward mastering Python and Artificial Intelligence, focusing on writing clean, structured, and meaningful code every single day.
