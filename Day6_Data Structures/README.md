# Day 6 – Python Data Structures

In Day 6 of my Python and AI journey, I focused on learning and practicing **core data structures in Python**: Lists, Tuples, Sets, and Dictionaries. These are fundamental for organizing, storing, and manipulating data efficiently, which is essential for AI and Machine Learning projects.

## 🧠 Code Examples

### 1️⃣ Lists
```python
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

fruits.append("orange")
print("After Append:", fruits)

fruits.remove("banana")
print("After Remove:", fruits)

### 2️⃣ Tuples
coordinates = (10.5, 20.8)
print("Tuple Example:", coordinates)

### 3️⃣ Sets
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set Example (No Duplicates):", unique_numbers)

unique_numbers.add(6)
print("After Adding 6:", unique_numbers)

### 4️⃣ Dictionaries
person = {
    "name": "John",
    "age": 25,
    "city": "Toronto"
}
print("Dictionary Example:", person)

person["age"] = 26
print("Updated Dictionary:", person)

### 5️⃣ Looping through a Dictionary
for key, value in person.items():
    print(f"{key}: {value}")

📂 Folder Structure:
Day6_Data_Structures/
│
├── data_structures.py
├── README.md
└── Screenshots/
    ├── Day6_Program_Output.jpg
    └── Day6_folder_structure.jpg
    └── Day6-Code_Of_Program.jpg
     └── Day6_Github_Push.jpg
    

🔗 References: 
References

Python Official Documentation – Data Structures
https://docs.python.org/3/tutorial/datastructures.html

W3Schools – Python Lists
https://www.w3schools.com/python/python_lists.asp

W3Schools – Python Tuples
https://www.w3schools.com/python/python_tuples.asp

W3Schools – Python Sets
https://www.w3schools.com/python/python_sets.asp

W3Schools – Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp

Real Python – Python Data Structures Guide
https://realpython.com/python-data-structures/


    🏁 Conclusion:

Day 6 reinforced my understanding of Python’s core data structures. By practicing Lists, Tuples, Sets, and Dictionaries, and iterating through them using loops, I am building a strong foundation for data manipulation — a crucial step for AI and Machine Learning projects.