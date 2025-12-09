# -----------------------------------------
# 🌟 Day 36 – Python Conditionals & Logic
# Python & AI – 90 Days Journey
# -----------------------------------------

print("\n🔹 Welcome to Day 36 – Conditionals & Advanced Logic!")

# Example 1 — Basic If/Else
temperature = 32

if temperature > 30:
    print("🔥 It's a hot day!")
else:
    print("❄️ It's a pleasant day.")

# Example 2 — Using elif
score = 87

if score >= 90:
    print("🏆 Grade: A")
elif score >= 80:
    print("🎖️ Grade: B")
elif score >= 70:
    print("📘 Grade: C")
else:
    print("❌ Grade: D")

# Example 3 — Logical Operators
age = 29
has_id = True

if age >= 18 and has_id:
    print("✅ Access Granted")
else:
    print("⛔ Access Denied")

# Example 4 — Nested Conditions
user = "Jobanjit"
is_admin = True
logged_in = True

if logged_in:
    print(f"👋 Welcome back, {user}!")
    
    if is_admin:
        print("🔐 Admin Privileges Activated.")
    else:
        print("🙂 Standard User Access.")
else:
    print("🔑 Please log in first.")

# -----------------------------------------
# 🛡️ Mini Project: Access Control System
# -----------------------------------------

print("\n🔐 MINI PROJECT: SECURITY ACCESS CONTROL")

username = input("Enter username: ")
password = input("Enter password: ")

# Fake database
correct_user = "admin"
correct_pass = "secure123"

if username == correct_user:
    if password == correct_pass:
        print("🟢 Login Successful — Full Access Granted!")
    else:
        print("🔴 Incorrect Password — Access Denied!")
else:
    print("⚠️ Unknown User — Access Blocked!")

print("\n🚀 Day 36 Completed Successfully!")
