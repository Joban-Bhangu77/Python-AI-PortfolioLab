# 🐍 Day 21 – Advanced Python Lists & Data Analysis

***

## 🌟 Project Title: Student Marks Analyzer

### **🗓️ Day 21 of Python & AI 90-Days Learning Journey**

---

## 💡 Overview: From Basics to Data-Driven Problem Solving

In Day 21, we went beyond the basics of Python lists, mastering advanced techniques crucial for **data processing** and **AI preparation**. This lesson focused on efficiency, clean code practices (like List Comprehensions), and multi-dimensional data handling.

The core learning was cemented by building the **Student Marks Analyzer** mini-project, which demonstrates how to use list operations and built-in functions to extract meaningful insights from raw data.

---

## 📊 Mini-Project Spotlight: Student Marks Analyzer

This project collects marks from a user and immediately performs key descriptive statistics, showcasing the power of lists combined with built-in functions (`sum()`, `max()`, `len()`).

### **Features Implemented:**

| Feature | Python Concept Used |
| :--- | :--- |
| **Data Collection** | `list.append()` inside a `for` loop |
| **Highest/Lowest Marks** | `max(marks)` and `min(marks)` |
| **Average Score** | `sum(marks) / len(marks)` |
| **Above-Average Count** | **List Comprehension** with a conditional filter |

### **Console Example:**

📊 Student Marks Analyzer Enter number of students: 3 Enter marks for student 1: 85 Enter marks for student 2: 92 Enter marks for student 3: 78

✔️ All Marks: [85, 92, 78] 📈 Highest Score: 92 📉 Lowest Score: 78 📊 Average Score: 85.0 🎯 Students above average: 1



---

## 🧠 Advanced Concepts Covered

| Skill Area | Key Concepts Mastered |
| :--- | :--- |
| **Data Extraction** | Mastering advanced list **slicing** (`[::2]`, `[:3]`, `[3:]`). |
| **Code Efficiency** | **List Comprehensions** for creating new lists in a single, fast line. |
| **Data Integrity** | Sorting lists efficiently using `sorted()` and the in-place `.sort()`. |
| **Multi-Dimension** | Working with **nested lists** (2D lists) for handling tabular data (like a matrix). |
| **Manipulation** | Adding (`.append()`, `.insert()`), updating, and removing (`.remove()`) items. |
| **Utility** | Leveraging powerful built-in functions: `sum()`, `len()`, `max()`, `min()`. |

---

## 💻 Code Implementation

### **File:** `Day21_Advanced_Lists.py`

This code demonstrates all the concepts covered, from slicing to the final project.

```python
# ---------------------------------------------
# 📘 Day 21 – Advanced Python Lists
# Python & AI | 90 Days Journey
# ---------------------------------------------

# 1️⃣ List Slicing
numbers = [10, 20, 30, 40, 50, 60]
print("Original List:", numbers)
print("Slice [1:4] →", numbers[1:4])
print("Slice [:3]  →", numbers[:3])
print("Slice [3:]  →", numbers[3:])
print("Slice with step [::2] →", numbers[::2])
print("\n" + "-"*50)

# 2️⃣ Modifying Lists
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("banana")
print("Updated Fruits List:", fruits)
print("\n" + "-"*50)

# 3️⃣ Sorting Lists
values = [5, 2, 9, 1, 7]
print("Original Values:", values)
print("Sorted Asc:", sorted(values))
print("Sorted Desc:", sorted(values, reverse=True))

values.sort()
print("Values after sort():", values)
print("\n" + "-"*50)

# 4️⃣ List Comprehension
squares = [x*x for x in range(1, 11)]
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Squares (1-10):", squares)
print("Even Numbers (1-20):", even_numbers)
print("\n" + "-"*50)

# 5️⃣ Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Middle element →", matrix[1][1])
print("Last row →", matrix[2])
print("First row, last element →", matrix[0][2])
print("\n" + "-"*50)

# 6️⃣ Useful List Functions
numbers2 = [5, 10, 15, 20, 25]
print("Length:", len(numbers2))
print("Sum:", sum(numbers2))
print("Max:", max(numbers2))
print("Min:", min(numbers2))
print("\n" + "-"*50)

# 7️⃣ Mini Project – Student Marks Analyzer
print("📊 Student Marks Analyzer")

marks = []
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    score = int(input(f"Enter marks for student {i+1}: "))
    marks.append(score)

print("\n✔️ All Marks:", marks)
print("📈 Highest Score:", max(marks))
print("📉 Lowest Score:", min(marks))

# Calculate and print average
average = sum(marks) / len(marks)
print("📊 Average Score:", average)

# Bonus: Students above average using List Comprehension
above_avg = [m for m in marks if m > average]
print("🎯 Students above average:", len(above_avg))

💎 Key Takeaways
Dynamic and Flexible: Lists remain the most commonly used, flexible data structure in Python.

Efficiency: List comprehensions are not just cleaner, they are often significantly faster than traditional for loops for creating lists.

Data Preparation: The ability to slice, sort, and handle nested data forms the crucial preprocessing foundation needed before working with advanced libraries like Pandas and NumPy in machine learning workflows.

Problem Solving: Combining lists with loops and conditions allows for effective real-world data analysis, as demonstrated by the Analyzer project.

🏁 Conclusion
Day 21 successfully strengthened the understanding of Python lists and transitions the focus from basic programming logic into data-driven problem solving.

The skills acquired—especially list comprehensions and data aggregation—are directly applicable to upcoming lessons involving advanced data structures, automation scripts, and foundational AI projects.

Keep pushing forward — one day at a time! 🚀🐍