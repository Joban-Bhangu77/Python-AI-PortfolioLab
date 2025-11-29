# 🐍 Python & AI Learning Journey – Day 8  
**Author:** Jobanjit Singh  

---

## 🌟 Overview  
This repository contains my daily Python learning exercises as part of my **90-Day Python & AI Journey**.  
Each day focuses on core programming concepts, with practical examples and mini-projects.

---

## 📅 Day 8 – Loops in Python (For & While)

### 🎯 Learning Objectives  
- Understand how **loops** work in Python.  
- Learn to use **for** and **while** loops effectively.  
- Practice using **range()**, **lists**, and conditional logic inside loops.  
- Build a short project to identify **Even** and **Odd** numbers.  

---

## 🧠 Key Concepts  

### 🔹 For Loop  
Used to iterate through a sequence (like a list or range).  
```python
for i in range(5):
    print("Iteration number:", i)

🔹 For Loop with Lists

Iterating through each element in a list.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

🔹 While Loop

Repeats execution as long as the condition is True.
count = 1
while count <= 5:
    print("Counting:", count)
    count += 1

🔹 Break and Continue

Used to control loop flow.

for number in range(1, 10):
    if number == 5:
        break     # Stop loop completely
    print(number)

for number in range(1, 10):
    if number == 5:
        continue  # Skip number 5
    print(number)


🧩 Mini Project: Even & Odd Number Finder

File Name: Day8_Loops_Practice.py

print("Welcome to Day 8: Even and Odd Number Finder!")

for num in range(1, 11):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

print("Loop complete! Great job, Jobanjit!")

Sample Output:

1 is Odd
2 is Even
3 is Odd
...
10 is Even
Loop complete! Great job, Man...!!

📂 Folder Structure
📦 Python-AI-PortifoliLab
 ┣ 📁 Day8_Loops_Practice
 ┃ ┣ 🖼️ Screenshots/
 ┃ ┣ 📜 README.md
 ┃ ┗ 📜 Day8_Loops_Practice.py
 
 🏁 Conclusion

Day 8 was a major step forward in building a strong logical foundation in Python.
Understanding loops — both for and while — allows for automation, iteration, and efficient handling of repetitive tasks.
These concepts form the backbone for future topics like data processing, automation scripts, and machine learning model training loops.

With every loop executed, I am looping closer to mastery!💪

📚 References
📘 Official Documentation

Python.org – Control Flow Statements

💡 Learning Tutorials

W3Schools – Python For Loops

GeeksforGeeks – While Loop in Python

🧠 In-Depth Guides

Real Python – Understanding For Loops

Programiz – Python Loops Explained