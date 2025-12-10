# 🌟 Day 37 – Python Lists (Advanced) + List Methods + Mini Project  
Part of the **Python & AI – 90 Days Journey**

## 📘 Overview  
Day 37 focused on understanding and practicing **Python Lists**, an essential data structure used in automation, AI, machine learning preprocessing, and general scripting.  
The goal was to learn how to manipulate lists, loop through items, and build a mini interactive project.

## 🧠 Topics Covered

### 🔹 Python List Methods  
I practiced commonly used list operations:

```python
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "orange")
fruits.remove("banana")
fruits.pop()    # removes last item

🔹 Sorting & Reversing
numbers = [5, 3, 8, 1]
numbers.sort()
numbers.reverse()

🔹 Looping Through Lists
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(i, color)

🧩 Mini Project – Grocery List Manager

A fully interactive console program where users can add, remove, and view their grocery items.

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
        print(f"✔ '{item}' added!")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"❌ '{item}' removed!")
        else:
            print("Item not found!")

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

📤 How I Saved My Output (Without Screenshots)

To save output professionally:

python day37_lists.py > Day37_Output.txt


This creates a clean text file containing all printed results.

🏁 Conclusion

Day 37 strengthened my understanding of how Python handles dynamic lists.
I gained confidence in:

manipulating list data

looping through items

creating interactive console applications

This knowledge is foundational for future topics like data structures, AI data preprocessing, and automation.