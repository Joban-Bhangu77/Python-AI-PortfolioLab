# 📘 Day 22: Mastering Python List Comprehensions

## 🚀 Overview

This project marks **Day 22** of the **Python & AI 90 Days Journey**. The focus is on **List Comprehensions**—a fundamental, powerful, and highly *Pythonic* feature used for creating lists (and other collections) based on existing iterables in a concise and efficient manner.

Mastering comprehensions is an essential step towards writing clean, performant code, and is crucial for advanced topics like **NumPy**, **Pandas**, and modern **AI/ML data processing** pipelines.

---

## 🧠 Key Learning Objectives

| Concept | Description |
| :--- | :--- |
| **Basic Syntax** | Converting verbose `for` loops into compact, single-line list expressions. |
| **Conditional Logic** | Implementing `if` (filtering) and `if...else` (labeling/transformation) directly within the comprehension. |
| **Data Transformation** | Applying string methods and calling custom functions for complex data manipulation. |
| **Nested Comprehensions** | Handling multi-dimensional data, such as flattening matrices (2D lists) into a single list. |
| **Advanced Syntax** | Utilizing the ternary operator for `if/elif/else` logic to assign dynamic labels. |
| **Beyond Lists** | Extending the syntax to create **Set Comprehensions** (for uniqueness) and **Dictionary Comprehensions** (for key-value mapping). |

---

## 💻 Code Examples: `Day22_List_Comprehensions.py`

The script demonstrates various levels of complexity for comprehensions, from basic squaring to advanced dictionary creation.

### 1. Basic & Conditional List Comprehensions
```python
# 1️⃣ Basic List Comprehension: Squaring numbers
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers] 

# 2️⃣ Filtering: Creating a list of only even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

# 3️⃣ Conditional Expression: Labeling numbers as "Even" or "Odd"
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
2. String, Nested, and Function-Based Comprehensions
Python

# 4️⃣ String Manipulation: Capitalizing names
names = ["joban", "piyush", "cloud", "python"]
capitalized = [name.capitalize() for name in names]

# 5️⃣ Nested Comprehension: Flattening a 2D matrix
matrix = [[1, 2], [3, 4]]
flattened = [item for row in matrix for item in row]

# 6️⃣ Function-Based: Calculating cubes using a custom function
def cube(x):
    return x ** 3
cubes = [cube(n) for n in numbers]
3. Advanced Ternary Logic
Python

# 7️⃣ Complex if...elif...else Logic (Ternary)
grades = [95, 67, 80, 45, 89]
grade_labels = [
    ("A" if g >= 85 else "B" if g >= 70 else "C" if g >= 50 else "F")
    for g in grades
]
4. Set and Dictionary Comprehensions
Python

# 8️⃣ Set Comprehension: Generating unique characters
unique_letters = {char for char in "jobanjit"}

# 9️⃣ Dictionary Comprehension: Mapping names to their lengths
name_lengths = {name: len(name) for name in names}
💡 Key Takeaways
Readability & Performance: List Comprehensions significantly reduce lines of code while often improving execution speed compared to traditional for loops.

Versatility: The syntax supports filtering (if), transformation (if/else), and complex iteration (nesting).

Consistency: The core comprehension structure applies uniformly to Lists, Sets, and Dictionaries, making it a universally valuable tool in Python.

Professional Skill: This feature is a hallmark of professional, efficient, and Pythonic code, directly preparing for high-level data manipulation.

🏁 Conclusion
Day 22 successfully transformed an essential but often verbose programming task (list creation via loops) into an elegant, concise, and highly efficient feature. This is a critical skill for advancing into data-intensive fields like AI and Data Engineering.