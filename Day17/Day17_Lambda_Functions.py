# Simple lambda example
square = lambda x: x ** 2
print(square(5))  # Output: 25


# Multiple arguments in lambda
add = lambda a, b: a + b
print(add(10, 20))  # Output: 30


# Using map() to square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# Using filter() to get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


from functools import reduce

# Using reduce() to calculate product of all numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Combine map, filter, reduce together
from functools import reduce

numbers = [2, 4, 6, 8, 10]

# Step 1: Square all numbers
squares = list(map(lambda x: x**2, numbers))

# Step 2: Filter numbers > 20
filtered = list(filter(lambda x: x > 20, squares))

# Step 3: Reduce to sum all remaining numbers
sum_of_filtered = reduce(lambda x, y: x + y, filtered)

print("Squares:", squares)
print("Filtered (>20):", filtered)
print("Sum of filtered:", sum_of_filtered)
