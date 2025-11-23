# 🌟 Day 27 – Nested Loops & Pattern Programming  
Part of the **Python & AI – 90 Days Journey**

## 📘 Overview  
Day 27 focuses on strengthening your understanding of **nested loops**, a key skill used in:  
- Pattern printing  
- Data structure traversal  
- Building matrix-based algorithms  
- AI/ML preprocessing tasks  
- Real-world problem solving  

This day helps you write cleaner and more precise loop-based logic.

---

## 🧠 What I Learned Today  

### 🔹 1. Square Pattern  
Using nested loops to create a consistent 5×5 pattern.  

### 🔹 2. Right Triangle Pattern  
Understanding how loop increments create shapes.  

### 🔹 3. Pyramid Pattern  
Balanced spacing + stars using nested loops.  

### 🔹 4. Multiplication Table (1–5)  
Shows practical use of loops for tabular data.  

### 🔹 5. Mini Project – Pattern Password Generator  
A fun beginner-level project that prints incremental patterns from a word.

---

## 🧩 Code (Day27.py)

```python
# 🌟 Day 27 – Nested Loops & Pattern Programming

print("\n=== Day 27: Nested Loops & Patterns ===\n")

# 1️⃣ Square Pattern
print("1. Square Pattern:")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# 2️⃣ Right Triangle Pattern
print("\n2. Right Triangle Pattern:")
for i in range(1, 6):
    print("*" * i)

# 3️⃣ Pyramid Pattern
print("\n3. Pyramid Pattern:")
rows = 5
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2*i + 1))

# 4️⃣ Multiplication Table (1 to 5)
print("\n4. Multiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# 5️⃣ Mini Project – Pattern Password Generator
print("\n5. Mini Project: Pattern Password Generator")
word = "PYTHON"
for i in range(len(word)):
    print(word[:i+1])

print("\n=== End of Day 27 ===")
```

---

## 🖼️ Screenshots  
Place your screenshots inside:

```
Screenshots/
│── Day27_Code.jpg
└── Day27_Output.jpg
```

---

## 🏁 Conclusion  
Day 27 strengthens your foundation in nested loops and pattern logic — essential for progressing toward **AI, ML, and data structure algorithms**. These skills will help you build more advanced projects in upcoming days.

---

## 📚 References  
- Python Official Docs  
- W3Schools Python Loops  
- GeeksforGeeks – Patterns in Python  

