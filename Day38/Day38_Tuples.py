# -----------------------------
# Day 38 – Python Tuples
# Python & AI: 90 Days Journey
# -----------------------------

# 1️⃣ Creating Tuples
fruits = ("Apple", "Banana", "Cherry")
numbers = (10, 20, 30, 40, 50)

print("Fruits Tuple:", fruits)
print("Numbers Tuple:", numbers)

# 2️⃣ Accessing Elements
print("First fruit:", fruits[0])
print("Last number:", numbers[-1])

# 3️⃣ Tuple Length
print("Length of fruits tuple:", len(fruits))

# 4️⃣ Tuple Slicing
print("Slice numbers (1:4):", numbers[1:4])

# 5️⃣ Checking Membership
print("Is 'Banana' in fruits?", "Banana" in fruits)

# 6️⃣ Tuples are Immutable (Demonstration)
try:
    fruits[0] = "Mango"
except TypeError:
    print("❌ Tuples cannot be modified (immutable)")

# 7️⃣ Tuple with Mixed Data Types
person = ("Jobanjit", 29, "Engineer", True)
print("Person Tuple:", person)

# 8️⃣ Returning Multiple Values with Tuples
def get_coordinates():
    return (45.123, -79.456)

lat, lon = get_coordinates()
print("Latitude:", lat)
print("Longitude:", lon)

# 9️⃣ Looping Over Tuples
for fruit in fruits:
    print("Fruit:", fruit)

# 🔟 Tuple Methods
print("Count of 20 in numbers:", numbers.count(20))
print("Index of 30:", numbers.index(30))

print("\n🎉 Day 38 practice complete!")
