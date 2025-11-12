# 🧠 Day 18: Map, Filter & Reduce Functions

from functools import reduce
# ----------------------------
# 1️⃣ Using map()
# ----------------------------
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled Numbers:", doubled)

# Convert Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print("Celsius to Fahrenheit:", fahrenheit)

# ----------------------------
# 2️⃣ Using filter()
# ----------------------------
# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Filter words longer than 4 characters
words = ["AI", "Python", "Code", "Data", "ML"]
long_words = list(filter(lambda w: len(w) > 4, words))
print("Words longer than 4 letters:", long_words)

# ----------------------------
# 3️⃣ Using reduce()
# ----------------------------
# Calculate the sum of all numbers
sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", sum_all)

# Find the product of all numbers
product_all = reduce(lambda a, b: a * b, numbers)
print("Product of all numbers:", product_all)

# ----------------------------
# 4️⃣ Combining map, filter, and reduce
# ----------------------------
# Example: Square even numbers and sum them
even_square_sum = reduce(
    lambda a, b: a + b,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print("Sum of squares of even numbers:", even_square_sum)
