# Program 1: Hello World & Print Basics
## Goal: Understand how Python executes a program and prints output

print("Hello World")
print("Welcome to Pyton Programming!")
print("Let's get started with Python basics.")
print("This is a simple Python script.")
print("Enjoy coding in Python!")

# Program 2: Variables and Simple Calculations
## Goal: Learn how to declare variables and perform basic calculations

name = "Jobanjit"
age = 29
height = 6.0 # in feet
is_learning_python = True

print("Name:", name)
print("Age:")
print("Height:", height)
print("Is learning Python:", is_learning_python)

# Simple calculations   
print("Age after 5 years:", age + 5)

#  Program 3 : User Input + Decision Making
## Goal: Get user input and make decisions based on it (interaction and logic)

#  Input and If-Else

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")