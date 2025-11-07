# 🧠 Day 13 – Python String Manipulation & Formatting  

---

## 🏆 Overview  
In **Day 13**, we explored one of Python’s most essential concepts — **String Manipulation & Formatting**.  
This lesson covered how to **create**, **slice**, **concatenate**, and **format strings** efficiently.  
We concluded the session with a fun and interactive **Username Generator Project** using string methods and user input.  

---

## 🎯 Learning Objectives  
- Learn how to **create and manipulate strings** in Python.  
- Understand **slicing**, **concatenation**, and **f-string formatting**.  
- Explore common string methods:  
  - `.upper()`  
  - `.lower()`  
  - `.strip()`  
  - `.replace()`  
  - `.split()`  
- Build a **Username Generator** mini project combining these techniques.  

---

## 💻 Code Highlights  

### 🔹 String Basics  
```python
name = "Jobanjit"
greeting = "Hello"
print(greeting + ", " + name + "!")   # Concatenation

🔹 String Slicing
text = "PythonProgramming"
print(text[0:6])   # Output: Python
print(text[-3:])   # Output: ing

🔹 String Formatting
age = 29
print(f"My name is {name} and I am {age} years old.")

🔹 Common String Methods
text = "  python is Fun!  "
print(text.upper())          # PYTHON IS FUN!
print(text.lower())          # python is fun!
print(text.strip())          # removes spaces
print(text.replace("Fun", "Powerful"))   # python is Powerful!
print(text.split())          # ['python', 'is', 'Fun!']

🚀 Mini Project: Username Generator
# Day 13 - String Manipulation & Formatting

print("Welcome to the Username Generator!\n")

# Taking user input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Creating username variations
username1 = first_name.lower() + last_name.lower()
username2 = first_name[:3].lower() + last_name[:3].lower() + birth_year[-2:]
username3 = f"{first_name.capitalize()}_{last_name.capitalize()}{birth_year[-2:]}"

# Display results
print("\n✨ Here are some username suggestions for you:")
print("1️⃣", username1)
print("2️⃣", username2)
print("3️⃣", username3)

print("\nExperiment complete. You just learned Python String Manipulation! 💪")

🖼️ Screenshots
Screenshot	Description
Day13_Code1.jpg	String manipulation examples
Day13_Code2.jpg	Username Generator code
Day13_Output.jpg	Program output with generated usernames

📂 Folder Structure
Python-AI-PortfolioLab/
│
├── Day13_String_Manipulation/
│   ├── Day13_String_Manipulation.py
│   ├── Screenshots/
│   │   ├── Day13_Code1.jpg
│   │   ├── Day13_Code2.jpg
│   │   └── Day13_Output.jpg
│   └── README.md

🏁 Conclusion

Today’s session reinforced Python string concepts with a practical twist.
You learned how to manipulate, format, and style text, and applied it to create a personalized Username Generator Project.
A small but powerful step in becoming a professional Python developer!