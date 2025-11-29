# Day 11: Lists and Tuples Deep Dive
print("Welcome to Day 11 of Python & AI Journey - Lists & Tuples")

# --- Lists ---
fruits = ["apple", "banana", "cherry"]
print("\nOriginal List:",fruits)

 #Add elements
fruits.append("mango")
fruits.insert(1, "orange")
print("After Adding:", fruits)

# Remove elements
fruits.remove("banana")
popped_item = fruits.pop()
print("After Removing:", fruits)
print("Popped Item:", popped_item)

# Access elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# List slicing
print("Sliced Fruits:", fruits[0:2])

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)

# Copying lists
fruits_copy = fruits.copy()
fruits_copy.append("pineapple")
print("Copied List:", fruits_copy)
print("Original List:", fruits)

# --- Nested Lists Example ---
matrix = [[1, 2], [3, 4], [5, 6]]
print("\nMatrix Example:", matrix)
print("Accessing Element:", matrix[1][0])

# --- Tuples ---
coordinates = (10.5, 20.3)
print("\nTuple Example:", coordinates)
print("X-coordinate:", coordinates[0])

# Tuple unpacking
x, y = coordinates
print("Unpacked Values -> X:", x, ", Y:", y)

# --- Mini Project ---
# Grocery price calculator
print("\n🛒 Grocery Price Calculator")
items = [("Milk", 2.99), ("Eggs", 3.49), ("Bread", 2.79), ("Apples", 4.20)]
total = sum([price for item, price in items])
print("Items:", items)
print("Total Cost: $", round(total, 2))