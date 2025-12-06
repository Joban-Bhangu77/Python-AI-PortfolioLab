# Day 34 - Python File Handling

print("📂 Welcome to Day 34 - File Handling in Python!")

# ---------- Writing to a File ----------
print("\n✍️ Writing to a file...")
with open("day34_notes.txt", "w") as file:
    file.write("This is Day 34 of Jobanjit's Python & AI Journey.\n")
    file.write("Learning File Handling in Python.\n")

print("✔ File created and written successfully!")

# ---------- Appending to a File ----------
print("\n➕ Appending more content...")
with open("day34_notes.txt", "a") as file:
    file.write("Appending new line at Day 34.\n")

print("✔ Content appended successfully!")

# ---------- Reading the File ----------
print("\n📖 Reading file content:")
with open("day34_notes.txt", "r") as file:
    content = file.read()
    print(content)

# ---------- Reading Line-by-Line ----------
print("\n📄 Reading line by line:")
with open("day34_notes.txt", "r") as file:
    for line in file:
        print("•", line.strip())

# ---------- Error Handling Example ----------
print("\n⚠️ Error Handling Demo:")
try:
    with open("file_that_does_not_exist.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("❌ Error: File not found!")
except Exception as e:
    print("❌ Unexpected Error:", e)
