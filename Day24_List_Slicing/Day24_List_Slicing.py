# 🌟 Day 24 – Python List Slicing & Advanced Indexing
# Part of the Python & AI 90 Days Journey

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Original List:", numbers)

# 1️⃣ Basic Slicing
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[-5:])
print("Middle elements (index 3 to 7):", numbers[3:8])

# 2️⃣ Step Slicing
print("Every 2nd element:", numbers[::2])
print("Every 3rd element:", numbers[::3])

# 3️⃣ Reverse Slicing
print("Reversed list:", numbers[::-1])

# 4️⃣ Slicing with negative step
print("Reverse every 2nd element:", numbers[::-2])

# 5️⃣ Slice assignment
modified = numbers[:]  # copy list
modified[2:5] = [300, 400, 500]
print("Modified list after slice assignment:", modified)

# 6️⃣ Extract sublists for ML-like preprocessing
data = ["joban", "python", "ai", "ml", "devops", "cloud"]
print("\nML Preprocessing Example")
print("Take first 3 labels:", data[:3])
print("Take last 2 labels:", data[-2:])
print("Skip first and last:", data[1:-1])
