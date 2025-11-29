# 🟦 Day 25 – Python Dictionaries

# 1️⃣ Creating a dictionary
student = {
    "name": "Jobanjit",
    "age": 29,
    "skills": ["Python", "Networking", "Kubernetes"],
    "is_active": True
}

print("Student Info:", student)

# 2️⃣ Accessing values
print("Name:", student["name"])
print("Skills:", student["skills"])
print("First Skill:", student["skills"][0])

# 3️⃣ Adding new key-value pair
student["country"] = "Canada"
print("Updated Student:", student)

# 4️⃣ Updating values
student["age"] = 30

# 5️⃣ Looping through dictionary
print("\n📌 Looping through dictionary keys:")
for key in student:
    print(key, ":", student[key])

print("\n📌 Looping through items:")
for key, value in student.items():
    print(key, "➡️", value)

# 6️⃣ Using dictionary methods
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 7️⃣ Nested dictionary example
network_devices = {
    "Router1": {"ip": "192.168.1.1", "vendor": "Cisco", "status": "Active"},
    "Switch1": {"ip": "192.168.1.2", "vendor": "Cisco", "status": "Active"},
    "Firewall": {"ip": "192.168.1.3", "vendor": "Palo Alto", "status": "Active"}
}

print("\nNetwork Devices:", network_devices)
print("Firewall Vendor:", network_devices["Firewall"]["vendor"])

# 8️⃣ Mini Project — Student Info System
print("\n🎓 Student Info System")
student_data = {}

num = int(input("How many students to add? "))

for i in range(num):
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    student_data[name] = grade

print("\n📘 Final Student Records:")
for name, grade in student_data.items():
    print(name, "➡️", grade)
