# Day 6 - Python Data Structures

# 1️⃣ Lists
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

fruits.append("orange")
print("After Append:", fruits)

fruits.remove("banana")
print("After Remove:", fruits)

# 2️⃣ Tuples
coordinates = (10.5, 20.8)
print("\nTuple Example:", coordinates)

# 3️⃣ Sets
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print("\nSet Example (No Duplicates):", unique_numbers)

unique_numbers.add(6)
print("After Adding 6:", unique_numbers)

# 4️⃣ Dictionaries
person = {
    "name": "John",
    "age": 25,
    "city": "Toronto"
}
print("\nDictionary Example:", person)

person["age"] = 26
print("Updated Dictionary:", person)

# 5️⃣ Looping through Dictionary
print("\nIterating Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
