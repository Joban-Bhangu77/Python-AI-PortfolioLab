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

# Ascending & descending sort
print("Sorted Asc:", sorted(values))
print("Sorted Desc:", sorted(values, reverse=True))

# Sorting with .sort()
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
print("Student Marks Analyzer")

marks = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    score = int(input(f"Enter marks for student {i+1}: "))
    marks.append(score)

print("\n All Marks:", marks)
print("Highest Score:", max(marks))
print("Lowest Score:", min(marks))
print("Average Score:", sum(marks) / len(marks))

# Bonus: Above-average students count
average = sum(marks) / len(marks)
above_avg = [m for m in marks if m > average]
print("🎯 Students above average:", len(above_avg))