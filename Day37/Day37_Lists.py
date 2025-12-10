# 🌟 Day 37 – Python Lists (Advanced) + List Methods + Mini Project
# Part of the Python & AI – 90 Days Journey

# --------------------------------------------
# 📘 Overview
# Today we learn: list methods, sorting, looping,
# and a Grocery List Manager mini project.
# --------------------------------------------

# 🔹 1. List Methods

print("=== List Methods Demo ===")

# Append
fruits = ["apple", "banana"]
fruits.append("mango")
print("After append:", fruits)

# Insert
fruits.insert(1, "orange")
print("After insert:", fruits)

# Remove
fruits.remove("banana")
print("After remove:", fruits)

# Pop
fruits.pop()  # removes last item
print("After pop:", fruits)

# Sorting
numbers = [5, 3, 8, 1]
numbers.sort()
print("Sorted numbers:", numbers)

# Reverse
numbers.reverse()
print("Reversed numbers:", numbers)

# --------------------------------------------
# 🔹 2. Looping Through Lists
# --------------------------------------------

print("\n=== Looping Demo ===")

colors = ["red", "green", "blue"]

# Simple Loop
for color in colors:
    print("Color:", color)

# Loop with index
for i, color in enumerate(colors):
    print(f"Index {i} -> {color}")

# --------------------------------------------
# 🧩 3. Mini Project – Grocery List Manager
# --------------------------------------------

print("\n🛒 Welcome to Grocery List Manager!")

grocery_list = []

while True:
    print("\nChoose an option:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        grocery_list.append(item)
        print(f"✔ '{item}' added to your list!")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"❌ '{item}' removed!")
        else:
            print("Item not found in list!")

    elif choice == "3":
        print("\n📋 Your Grocery List:")
        if len(grocery_list) == 0:
            print("Your list is empty.")
        else:
            for i, item in enumerate(grocery_list, start=1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Try again!")
