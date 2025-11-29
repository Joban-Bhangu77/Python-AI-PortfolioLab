# -------------------------------
# 🌟 Day 26 – Advanced For Loops
# Python & AI – 90 Days Journey
# -------------------------------

# 1️⃣ Basic range loops
print("1. Range Loop Examples:")
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print("Even number:", i)


# 2️⃣ Looping through a dictionary
print("\n2. Looping Through a Dictionary:")
student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Cloud"]
}

for key, value in student.items():
    print(f"{key} : {value}")


# 3️⃣ Using enumerate()
print("\n3. Enumerate Example:")
hobbies = ["Coding", "Soccer", "Reading"]

for index, hobby in enumerate(hobbies):
    print(f"Index {index}: {hobby}")


# 4️⃣ Nested loops
print("\n4. Nested Loop Example:")
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x},{y})")


# 5️⃣ break, continue, pass
print("\n5. break / continue / pass Example:")
for num in range(1, 10):
    if num == 5:
        continue
    if num == 8:
        break
    print(num)


# 6️⃣ Real-World Mini Project: Student Marks Analyzer
print("\n🎓 Mini Project – Student Marks Analyzer")

marks = [85, 92, 76, 88, 95]
total = 0

for score in marks:
    total += score

average = total / len(marks)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Performance: Outstanding ⭐")
elif average >= 80:
    print("Performance: Excellent 🔥")
elif average >= 70:
    print("Performance: Good 👍")
else:
    print("Performance: Needs Improvement ❗")
