 📂 Day 20 – Python File Handling  
Part of the **Python & AI 90 Days Journey**  

Today’s lesson builds directly on **Day 19 (Error Handling)** and takes you into one of the most practical areas of Python—**reading and writing files**.  
This is essential for DevOps, Automation, AI/ML workflows, Data Engineering, and real-world scripting.

---

# 🎯 **Learning Objectives**

By the end of Day 20, you will understand:

- 📄 How to create files in Python  
- 📝 Writing data into files (`w` mode)  
- ➕ Appending data to existing files (`a` mode)  
- 📖 Reading files (entire file + line-by-line)  
- 🛑 Handling missing files using safe error handling  
- 🔒 Using `try/except/finally` with file operations  
- 🔐 Why `with open()` is best practice  
- 🧪 A mini practical exercise included in the code  

---

---

# 🧩 **Concepts Covered**

### ✔️ 1. Opening Files  
Python uses the `open()` function with different modes:
- `"w"` → Write (creates or overwrites)
- `"a"` → Append
- `"r"` → Read

### ✔️ 2. Writing Files  
```python
with open("file.txt", "w") as f:
    f.write("Hello World!")

    ✔️ 3. Appending Files
with open("file.txt", "a") as f:
    f.write("\nNext Line")

    ✔️ 4. Reading Files
with open("file.txt", "r") as f:
    print(f.read())

    ✔️ 5. Reading Line-by-Line
for line in file:
    print(line.strip())

    ✔️ 6. Handling File Exceptions

Used to prevent crashes and provide clean messages.

🚀 Output Example

File created successfully

Data written & appended

Entire file displayed

Line-by-line printed

Missing file error handled safely

Screenshot: Day20_Output.jpg

🧠 Why This Matters

This topic is the foundation for:

Logging systems

Reading configuration files

Automation scripts

Data pipelines

Machine learning datasets

DevOps CI/CD logs

JSON/CSV processing

Real-world troubleshooting tools

File handling is everywhere. Mastering it makes you 10× more capable as a Python developer.

💎 Key Takeaways

🔹 with open() ensures the file closes automatically

🔹 Always combine file handling with exceptions

🔹 Use "a" instead of "w" to avoid overwriting

🔹 .strip() cleans newline characters

🔹 File handling is core to automation & AI workflows

🏁 Conclusion

Day 20 introduces you to one of the most essential building blocks in Python.
From DevOps to Automation and AI—file handling is a skill you'll use throughout your entire tech career.
