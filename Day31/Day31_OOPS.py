# ----------------------------------------
# Day 31 - Python OOP: Classes & Objects
# Part of Python & AI – 90 Days Journey
# ----------------------------------------

class Student:
    # Constructor
    def __init__(self, name, program, year):
        self.name = name
        self.program = program
        self.year = year

    # Method to introduce the student
    def introduce(self):
        print(f"Hello, I am {self.name}. I am studying {self.program} in Year {self.year}.")

    # Method to show progress
    def progress(self):
        print(f"{self.name} has successfully completed Day 31 of the Python & AI Journey!")


# Creating objects
student1 = Student("Jobanjit", "Computer Science & AI", 2025)
student2 = Student("Charanjeet", "Cloud Engineering", 2024)

# Using object methods
student1.introduce()
student2.introduce()

student1.progress()
