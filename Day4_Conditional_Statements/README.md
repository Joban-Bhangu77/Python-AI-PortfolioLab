# Day 4 — Conditional Statements in Python

💻 **Project:** "AI Mood Detector"

In this project, we learned **conditional statements** in Python (`if`, `elif`, `else`) and combined them with user input to create a small AI-like program that reacts based on the user's mood.

---

## 🧠 What You Learn Today
- Using `if`, `elif`, and `else` for decision-making.
- Comparing values using `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Combining conditions using `and`, `or`, `not`.
- Building a mini project: **AI Mood Detector**, which reacts to your input mood.

---

## 💻 Code Example

```python
# day4_conditional_statements.py

name = input("What's your name? ")
mood = input("How are you feeling today? (happy/sad/tired/angry): ").lower()

print(f"\nHello {name}! Let's check your mood...")

if mood == "happy":
    print("😊 That's awesome! Keep spreading positivity!")
elif mood == "sad":
    print("💖 It's okay to feel low sometimes. Better days are coming!")
elif mood == "tired":
    print("😴 You should take a short break or nap. You’ve earned it!")
elif mood == "angry":
    print("🔥 Take a deep breath, calm down — you’ve got this!")
else:
    print("🤔 Hmm... that's a unique mood! Stay balanced and positive!")

print("\nEnd of Day 4 — Learning Conditional Logic in Python 💻")


🧮 Output Preview: 
What's your name? Joban
How are you feeling today? (happy/sad/tired/angry): tired

Hello Joban! Let's check your mood...
😴 You should take a short break or nap. You’ve earned it!

End of Day 4 — Learning Conditional Logic in Python 💻

Day4_Conditional_Statements/
│
├── day4_conditional_statements.py
├── README.md
└── Screenshots/
    ├── day4_output.jpg
    ├── day4_folder_structure.jpg
    └── day4_github_repo.jpg

🔗 References:

Python Official Documentation – Conditional Statements
Learn Python’s if, elif, else statements directly from the official docs.
https://docs.python.org/3/tutorial/controlflow.html#if-statements

W3Schools – Python If…Else
Beginner-friendly guide with examples of conditional statements.
https://www.w3schools.com/python/python_conditions.asp

Real Python – Python Comparison Operators
Understand how to compare values and combine conditions using and, or, not.
https://realpython.com/python-operators-expressions/

Programiz – Python Input and Output
Learn how to take user input and display output with Python.
https://www.programiz.com/python-programming/input-output

GeeksforGeeks – Python Conditional Statements
Clear examples of if, elif, else with real-world scenarios.
https://www.geeksforgeeks.org/python-conditional-statements/

🏁 Conclusion

Day 4 reinforced the fundamentals of decision-making in Python.
From checking user moods to responding dynamically, conditional statements are essential for building intelligent programs.

This project helps build structured coding habits, laying the foundation for more advanced AI & Machine Learning logic in the upcoming days.