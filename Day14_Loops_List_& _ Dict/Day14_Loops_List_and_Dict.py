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
