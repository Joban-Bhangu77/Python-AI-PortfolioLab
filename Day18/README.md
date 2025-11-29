# 🧠 Day 18 – Map, Filter & Reduce Functions in Python  
📘 *Python & AI 90 Days Journey – Functional Programming Concepts*

---

## 📖 Overview
Today’s focus was on mastering **functional programming** tools in Python — the powerful trio of  
`map()`, `filter()`, and `reduce()`.  

These functions help in **processing collections of data efficiently** without writing traditional `for` loops — enabling cleaner, faster, and more readable code.  

- **map()** → applies a function to every element.  
- **filter()** → selects elements that satisfy a condition.  
- **reduce()** → combines elements into a single output value.  

---

## 🧩 Code — `Day18_Map_Filter_Reduce.py`

```python
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

📂 Project Structure
📁 Day18_Map_Filter_Reduce/
│
├── Day18_Map_Filter_Reduce.py
├── screenshots/
│   ├── Day18_Code.jpg
│   ├── Day18_Output.jpg
│
└── README.md

🧠 Concept Summary
Function	Description	Example	Output
map()	Applies a function to all items	map(lambda x:x*2,[1,2,3])	[2,4,6]
filter()	Filters elements based on a condition	filter(lambda x:x>2,[1,2,3])	[3]
reduce()	Reduces iterable into single value	reduce(lambda x,y:x+y,[1,2,3])	6
💡 Key Takeaways

🔹 map() transforms data effortlessly.
🔹 filter() extracts elements meeting criteria.
🔹 reduce() condenses data into a single summary value.
🔹 Combining all three gives expressive and concise data pipelines.
🔹 Widely used in data analysis, AI/ML preprocessing, and functional programming.

🧭 Output Preview
Doubled Numbers: [2, 4, 6, 8, 10]
Celsius to Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
Even Numbers: [2, 4]
Words longer than 4 letters: ['Python']
Sum of all numbers: 15
Product of all numbers: 120
Sum of squares of even numbers: 20

🏁 Conclusion

Day 18 deepened my understanding of Python’s functional programming approach.
The combination of map(), filter(), and reduce() allows us to write cleaner, faster, and more scalable code, crucial for large-scale AI and data-driven applications.