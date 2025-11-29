# Day 22 – Python List Comprehensions
# Python & AI 90 Days Journey
# Topic: Beginner to Advanced List Comprehensions

# 1️⃣ Basic List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print("Squares:", squares)

# 2️⃣ Filtering inside List Comprehension
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)

# 3️⃣ Using conditions with else
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Labels:", labels)

# 4️⃣ List Comprehension with Strings
names = ["joban", "piyush", "cloud", "python"]
capitalized = [name.capitalize() for name in names]
print("Capitalized:", capitalized)

# 5️⃣ Nested List Comprehension
matrix = [[1, 2], [3, 4]]
flattened = [item for row in matrix for item in row]
print("Flattened List:", flattened)

# 6️⃣ Comprehension with Functions
def cube(x):
    return x ** 3

cubes = [cube(n) for n in numbers]
print("Cubes:", cubes)

# 7️⃣ Comprehension with if...elif...else
grades = [95, 67, 80, 45, 89]
grade_labels = [
    ("A" if g >= 85 else "B" if g >= 70 else "C" if g >= 50 else "F")
    for g in grades
]
print("Grade Labels:", grade_labels)

# 8️⃣ Set & Dictionary Comprehensions
unique_letters = {char for char in "jobanjit"}
print("Unique Letters Set:", unique_letters)

name_lengths = {name: len(name) for name in names}
print("Name Length Map:", name_lengths)
