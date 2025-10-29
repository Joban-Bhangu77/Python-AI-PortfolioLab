# Day 5 — Loops in Python

This project is part of my 90-day Python and AI learning journey. On Day 5, I focused on mastering **loops in Python**, a key concept for executing repetitive tasks efficiently — essential for real-world programming and AI applications.

---

## 🧠 Objectives

- Understand **for loops** and **while loops**.
- Learn to use **break** and **continue** statements.
- Practice iterating over ranges and applying loop logic.
- Build structured coding habits for better learning and documentation.

---

## 💻 Code Example

```python
# Day 5: Loops in Python

# For Loop Example
print("For Loop Example:")
for i in range(5):
    print("Iteration:", i)

print("\nWhile Loop Example:")
# While Loop Example
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Using break and continue
print("\nBreak and Continue Example:")
for num in range(10):
    if num == 5:
        break  # stop when num == 5
    if num % 2 == 0:
        continue  # skip even numbers
    print("Odd Number:", num)

🧮 Sample Output:
For Loop Example:
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4

While Loop Example:
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4

Break and Continue Example:
Odd Number: 1
Odd Number: 3

Day5_Loops/
│
├── day5_loops.py
├── README.md
└── Screenshots/
    ├── day5_output.jpg
    ├── day5_folder_structure.jpg
    └── day5_github_repo.jpg

🔗 References:

Python Official Documentation — Loops
https://docs.python.org/3/tutorial/controlflow.html#for-statements

W3Schools — Python Loops
https://www.w3schools.com/python/python_for_loops.asp

Real Python — Python While Loops
https://realpython.com/python-while-loop/

Programiz — Python Break and Continue Statements
https://www.programiz.com/python-programming/break-continue

TutorialsPoint — Python Loop Control Statements
https://www.tutorialspoint.com/python/python_loop_control.htm



🏁 Conclusion:

Day 5 reinforced my understanding of loops in Python, including for, while, and loop control statements like break and continue. These concepts are crucial for writing efficient code and building logic for AI applications. Through consistent practice, I am developing structured coding habits that will support more complex Python and AI projects in the future.