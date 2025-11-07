### Creating Strings
name = "Jobanjit"
greeting = 'Hello'
sentence = """"This is multiline string example"""

### String Concatenation
message = greeting + ", " + name + "!"
print(message)
 
### String Slicing
text = "PythonProgramming"
print(text[0:6])   # Output: Python
print(text[-3:])   # Output: ing

### String Formatting (f-strings)
age = 29
print(f"My name is {name} and I am {age} years old.")

### Common String Methods
text = "  python is Fun!  "
print(text.upper())     # PYTHON IS FUN!
print(text.lower())     # python is fun!
print(text.strip())     # removes spaces
print(text.replace("Fun", "Powerful"))  # python is Powerful!
print(text.split())     # ['python', 'is', 'Fun!']

###🧩 Mini Project: Username Generator
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
