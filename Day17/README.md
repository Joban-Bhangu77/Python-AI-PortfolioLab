# 🧠 Day 17 – Lambda Functions, Map, Filter & Reduce  

## 🌟 Overview  
Today marks **Day 17** of my **Python & AI 90 Days Journey**.  
I explored the power of **Lambda (anonymous) functions** and how they integrate beautifully with **Map, Filter, and Reduce** to perform functional-style programming in Python.  

These functions help make the code **concise**, **efficient**, and **readable** — especially when working with lists, transformations, and aggregations.  

---

## 📂 Project Structure  
Day17_Lambda_Functions/
│
├── Day17_Lambda_Functions.py
├── README.md
└── screenshots/
├── Day17_Code.jpg
└── Day17_Output.jpg


---

## 📘 Topics Covered  
✅ Lambda Functions (Anonymous Functions)  
✅ Using `map()` to apply operations on iterables  
✅ Using `filter()` to extract specific elements  
✅ Using `reduce()` for cumulative results  
✅ Practical chaining example using all three  

---

## 💻 Code Example  
```python
from functools import reduce

# 🔹 Lambda Functions
square = lambda x: x ** 2
add = lambda a, b: a + b

print("Square of 5:", square(5))
print("Addition of 10 and 20:", add(10, 20))

# 🔹 Using map() to square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared)

# 🔹 Using filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# 🔹 Using reduce() to calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)

# 🔹 Practical Example – Combine all
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

🖼️ Code Screenshot: screenshots/Day17_Code.jpg
🖼️ Output Screenshot: screenshots/Day17_Output.jpg

🚀 Key Takeaways

Lambda functions allow inline, one-line function definitions.

Map transforms data.

Filter selects data.

Reduce aggregates data.

Together, they create cleaner and faster functional workflows.