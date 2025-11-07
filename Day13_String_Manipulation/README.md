🧠 Day 13 – Python String Manipulation & Formatting

🏆 Overview
In Day 13, I  explored one of Python’s most powerful features — string manipulation and formatting.
Strings are everywhere in programming, and today’s practice taught how to slice, format, and modify them effectively.
The session concluded with a fun Username Generator mini-project, combining all learned string operations.

🎯 Learning Objectives

Understand how to create and work with strings in Python.

Learn concatenation, slicing, and string formatting using f-strings.

Use common string methods like .upper(), .lower(), .replace(), .split(), .strip().

Build a Username Generator that combines user input and string formatting logic.

🧩 Code Highlights
# String Concatenation
name = "Jobanjit"
greeting = "Hello"
print(greeting + ", " + name + "!")

# String Slicing
text = "PythonProgramming"
print(text[0:6])   # Python
print(text[-3:])   # ing

# String Formatting
age = 29
print(f"My name is {name} and I am {age} years old.")

# Common Methods
text = "  python is Fun!  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Fun", "Powerful"))
print(text.split())

🚀 Mini Project: Username Generator
# Day 13 - String Manipulation & Formatting

print("Welcome to the Username Generator!\n")

# Taking user input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Creating username variations
username1 = first_name.lower() + last_name.lower()
username2 = first_name[:3].lower() + last_name[:3].lower() + birth_year[-2:]
username3 = f"{first_name.capitalize()}_{last_name.capitalize()}{birth_year[-2:]}"

# Display results
print("\n✨ Here are some username suggestions for you:")
print("1️⃣", username1)
print("2️⃣", username2)
print("3️⃣", username3)

print("\nExperiment complete. You just learned Python String Manipulation! 💪")

📂 Folder Structure
Python-AI-PortfolioLab/
│
├── Day13_String_Manipulation/
│   ├── Day13_String_Manipulation.py
│   ├── Screenshots/
│   │   ├── Day13_Code1.jpg
│   │   ├── Day13_Code2.jpg
│   │   └── Day13_Output.jpg
│   └── README.md


🏁 Conclusion

This lesson covered everything from basic string operations to real-world formatting and manipulation.
You learned how to use Python’s built-in methods efficiently and created a personalized Username Generator — a fun and practical application of string concepts.