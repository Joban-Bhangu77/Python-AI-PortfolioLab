# 🌟 Day 35 – Python Lists & List Comprehensions

# -----------------------------
# 1️⃣ Basic List Creation
# -----------------------------

fruits = ["apple", "banana", "mango", "grapes"]
print("Fruits List:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Updating element
fruits[1] = "blueberry"
print("Updated Fruits:", fruits)

# -----------------------------
# 2️⃣ List Methods
# -----------------------------

numbers = [5, 2, 9, 1, 7]

numbers.append(10)
print("After append:", numbers)

numbers.insert(2, 99)
print("After insert:", numbers)

numbers.remove(9)
print("After remove:", numbers)

popped_item = numbers.pop()
print("Popped:", popped_item)
print("After pop:", numbers)

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# -----------------------------
# 3️⃣ List Slicing
# -----------------------------

data = [10, 20, 30, 40, 50, 60, 70]

print("First 3:", data[:3])
print("Last 3:", data[-3:])
print("Middle:", data[2:5])
print("Every 2nd value:", data[::2])
print("Reversed List:", data[::-1])

# -----------------------------
# 4️⃣ ⭐ List Comprehensions
# -----------------------------

# Square of numbers
nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]
print("Squares:", squares)

# Even numbers only
even = [x for x in nums if x % 2 == 0]
print("Even numbers:", even)

# Convert words to uppercase
words = ["python", "ai", "learning"]
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)

# Filter names starting with 'J'
names = ["Joban", "Aman", "Jaspreet", "Simran", "Jordan"]
j_names = [name for name in names if name.startswith("J")]
print("Names starting with J:", j_names)

# -----------------------------
# 5️⃣ Nested List Comprehension (Advanced)
# -----------------------------

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)
