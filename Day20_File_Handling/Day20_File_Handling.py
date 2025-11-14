# Day 20 – Python File Handling
# This lesson builds directly on Day 19 (Error Handling)

# 1️⃣ Create & Write Data into a File
try:
    with open("students.txt", "w") as file:
        file.write("Joban - Python & AI\n")
        file.write("Charanjeet - Cloud & DevOps\n")
        file.write("Neeru - Networking\n")
    print("✅ File created and initial data written successfully.")
except Exception as e:
    print(f"❌ Error writing file: {e}")

# 2️⃣ Append Data to Existing File
try:
    with open("students.txt", "a") as file:
        file.write("Gurnaaz - Future Superstar 🌟\n")
    print("✅ New data appended successfully.")
except Exception as e:
    print(f"❌ Error appending to file: {e}")

# 3️⃣ Read Entire File
print("\n📖 Reading full file content:\n")
try:
    with open("students.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ The file does not exist.")
except Exception as e:
    print(f"❌ Error reading file: {e}")

# 4️⃣ Read File Line-by-Line
print("\n📚 Reading file line by line:\n")
try:
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"❌ Error: {e}")

# 5️⃣ Demonstrate Handling Missing File
print("\n🔍 Trying to read a missing file:\n")
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ 'missing.txt' not found. (Handled safely)")
finally:
    print("✨ File handling demo completed.")
