# 🗓️ Day 14 – Loops with Lists and Dictionaries

## 🎯 Objective
Today’s goal was to understand and implement **loops** in Python using **lists** and **dictionaries**  "the foundation of automation and data iteration in Python programming.  
You also learned how to enhance loop control with `break`, `continue`, and nested loops".

---

## 🧠 Key Learning Topics
- Looping through **Lists** using `for`
- Looping through **Dictionaries** using `.items()`
- Using **`while`** loops for repetition
- **Nested loops** for multi-dimensional iteration
- Loop control statements: **`break`** and **`continue`**

---

## 💻 Project File
**File Name:** `Day14_Loops_List_and_Dict.py`

### 🧩 Code Overview
```python
# Day 14 – Loops with Lists and Dictionaries

# Loop through a list
fruits = ["apple", "banana", "cherry", "mango"]

print("🍎 Looping through a list:")
for fruit in fruits:
    print(f"I like {fruit}")

# While loop example
count = 1
print("\n🔢 Counting numbers using while loop:")
while count <= 5:
    print("Count:", count)
    count += 1

# Looping through a dictionary
person = {
    "name": "Jobanjit",
    "age": 29,
    "country": "Canada"
}

print("\n👨‍💻 Looping through a dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Nested loop example
print("\n📦 Nested loop example:")
colors = ["Red", "Green", "Blue"]
for fruit in fruits:
    for color in colors:
        print(f"{color} {fruit}")

# Using break and continue
print("\n🚦 Using break and continue:")
for num in range(1, 10):
    if num == 5:
        print("Skipping number 5 using continue")
        continue
    if num == 8:
        print("Breaking loop at 8")
        break
    print(num)

🧩 Concept Demonstrations
🔹 For Loop (List Iteration)

Iterating through a list to display each element dynamically.

🔹 While Loop

Used to repeat code execution until a condition is false — great for counters or retry logic.

🔹 Dictionary Iteration

Access both keys and values efficiently using .items().

🔹 Nested Loops

Loop within another loop — ideal for combinations or matrix-like data structures.

🔹 Break & Continue

break: Exit the loop completely.

continue: Skip the current iteration and move to the next one.

🧮 Output Example
🍎 Looping through a list:
I like apple
I like banana
I like cherry
I like mango

🔢 Counting numbers using while loop:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

👨‍💻 Looping through a dictionary:
name: Jobanjit
age: 29
country: Canada

📦 Nested loop example:
Red apple
Green apple
Blue apple
...
Breaking loop at 8

📂 Folder Structure
Python-AI-PortfolioLab/
│
├── Day14_Loops_List_and_Dict/
│   ├── Day14_Loops_List_and_Dict.py
│   ├── Screenshots/
│   │   ├── Day14_Code1.jpg
│   │   ├── Day14_Code2.jpg
│   └── README.md
│
└── ...

🧭 How to Run

Open your terminal or VS Code and execute:

cd Python-AI-PortfolioLab/Day14_Loops_List_and_Dict
python Day14_Loops_List_and_Dict.py

🧾 Conclusion

✔ Learned how to efficiently iterate over data structures in Python.
✔ Understood the difference between for and while loops.
✔ Practiced dictionary iteration and nested loops.
✔ Explored break and continue for loop control.
✔ Strengthened logic building — a key step toward automation and AI coding.