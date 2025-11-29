# 🌟 Day 27 – Nested Loops & Pattern Programming
# Part of Python & AI – 90 Days Journey

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

# 4️⃣ Nested Loop Example – Multiplication Table
print("\n4. Multiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# 5️⃣ Mini Project – Password Pattern Generator
print("\n5. Mini Project: Pattern Password Generator")

word = "PYTHON"
for i in range(len(word)):
    print(word[:i+1])

print("\n=== End of Day 27 ===")
