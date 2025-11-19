📘 Day 25 – Python Dictionaries

Python & AI – 90 Days Journey

🚀 Overview

Day 25 focuses on one of Python’s most powerful and flexible data structures — Dictionaries.
They are used extensively in real-world applications like JSON data handling, APIs, configurations, NLP token maps, and AI/ML pipelines.

Today, you explored dictionary fundamentals, advanced operations, and created a meaningful mini-project using key–value data storage.

🎯 Learning Objectives

By the end of this session, you will understand:

What Python Dictionaries are and how they work

Creating dictionaries from scratch

Accessing, updating, and modifying dictionary data

Looping through keys, values, and items

Common dictionary methods

Nested (multi-level) dictionaries

Building an interactive mini project using dictionaries

🧠 What Are Dictionaries?

A dictionary in Python stores data in key–value pairs, making it ideal for structured information.

Example:

student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Kubernetes"]
}


Keys must be unique

Values can be of any type

Order is preserved (Python 3.7+)

Dictionaries are mutable

🧪 Code Snippets
1️⃣ Creating and Accessing a Dictionary
student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Kubernetes"],
    "is_active": True
}

print(student["name"])
print(student["skills"][0])

2️⃣ Adding & Updating Values
student["country"] = "Canada"
student["age"] = 30

3️⃣ Looping Through Dictionary
for key, value in student.items():
    print(key, "➡️", value)

4️⃣ Dictionary Methods
student.keys()
student.values()
student.items()

5️⃣ Nested Dictionaries (Advanced)
network_devices = {
    "Router1": {"ip": "192.168.1.1", "vendor": "Cisco"},
    "Firewall": {"ip": "192.168.1.3", "vendor": "Palo Alto"}
}

print(network_devices["Firewall"]["vendor"])

🧩 Mini Project — Student Info System

This project collects student names and grades, stores them in a dictionary, and displays all records.

student_data = {}

num = int(input("How many students to add? "))

for i in range(num):
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    student_data[name] = grade

print("\nFinal Student Records:")
for name, grade in student_data.items():
    print(name, "➡️", grade)

📚 References

Python Official Documentation – Dictionaries
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

W3Schools – Python Dictionary Guide
https://www.w3schools.com/python/python_dictionaries.asp

Real Python – Dictionaries Deep Dive
https://realpython.com/python-dicts/