# Day 23 – Dictionary Comprehensions

# Example 1: Basic Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print("Squares:", squares)

# Example 2: Dictionary with Conditional Logic
even_numbers = {num: num**2 for num in numbers if num % 2 == 0}
print("Even Squares:", even_numbers)

# Example 3: Transforming Keys & Values
names = ["john", "sam", "priya"]
name_map = {name: name.upper() for name in names}
print("Name Mapping:", name_map)

# Example 4: Dictionary from Two Lists
students = ["John", "Aman", "Sonia"]
marks = [90, 85, 92]
result = {student: mark for student, mark in zip(students, marks)}
print("Student Marks:", result)

# Example 5: Nested Dictionary Comprehension
matrix = {
    i: {j: i * j for j in range(1, 4)}
    for i in range(1, 4)
}
print("Multiplication Matrix:", matrix)
