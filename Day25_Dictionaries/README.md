# Day 25 – Python Dictionaries
Python & AI – 90 Days Journey

---

## Overview
Day 25 focuses on Python Dictionaries, one of the most important and flexible data structures. Dictionaries store data in key–value pairs and are widely used in JSON, APIs, configurations, machine learning workflows, and automation scripts.

This session covers dictionary creation, updating values, looping through dictionaries, dictionary methods, nested dictionaries, and an interactive mini-project.

---

## Learning Objectives
- Understand what dictionaries are  
- Create and access key–value pairs  
- Update dictionary values  
- Loop through keys, values, and items  
- Use common dictionary methods  
- Build and use nested dictionaries  
- Apply concepts through a mini-project  

---

## What Are Dictionaries?
A dictionary in Python stores data in key–value pairs.

Example:

```python
student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Kubernetes"]
}
```

Keys must be unique, values can be of any type, and dictionaries are mutable.

---

## Code Snippets

### 1. Creating and Accessing a Dictionary

```python
student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Kubernetes"],
    "is_active": True
}

print(student["name"])
print(student["skills"][0])
```

---

### 2. Adding and Updating Data

```python
student["country"] = "Canada"
student["age"] = 30
```

---

### 3. Looping Through a Dictionary

```python
for key, value in student.items():
    print(key, ":", value)
```

---

### 4. Dictionary Methods

```python
student.keys()
student.values()
student.items()
```

---

### 5. Nested Dictionaries

```python
network_devices = {
    "Router1": {"ip": "192.168.1.1", "vendor": "Cisco"},
    "Firewall": {"ip": "192.168.1.3", "vendor": "Palo Alto"}
}

print(network_devices["Firewall"]["vendor"])
```

---

## Mini Project – Student Info System

```python
student_data = {}

num = int(input("How many students to add? "))

for i in range(num):
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    student_data[name] = grade

print("\nFinal Student Records:")
for name, grade in student_data.items():
    print(name, ":", grade)
```

---

## References
- Python Dictionaries: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- W3Schools Python Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
- RealPython Dictionary Guide: https://realpython.com/python-dicts/

---

## Conclusion
Day 25 strengthened your understanding of Python dictionaries, a fundamental structure used everywhere in real-world development and AI/ML applications. By mastering dictionary operations, looping, and nested structures, you are now prepared for more complex data-driven tasks.
