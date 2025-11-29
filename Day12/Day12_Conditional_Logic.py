marks = 85 

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade:A")
elif marks >=70:
    print("Grade: B")
else:
    print("Grade:C or below")

# Day 12: Conditional Logic & Student Grade Evaluator
print("🎓 Welcome to the Student Grade Evaluator System 🎓")

# Step 1: Take student details
name = input("Enter student name: ")
subject = input("Enter subject: ")

# Step 2: Input marks
marks = float(input(f"Enter marks for {subject} (out of 100): "))

# Step 3: Apply conditional logic
if marks >= 90:
    grade = "A+"
    remark = "Outstanding performance! Keep it up!"
elif marks >= 80:
    grade = "A"
    remark = "Excellent work!"
elif marks >= 70:
    grade = "B"
    remark = "Good effort!"
elif marks >= 60:
    grade = "C"
    remark = "Satisfactory. You can do better."
else:
    grade = "F"
    remark = "Needs improvement. Study harder!"

# Step 4: Display Result
print("\n📊 --- Student Report ---")
print(f"Name: {name}")
print(f"Subject: {subject}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Teacher's Remark: {remark}")

# Step 5: Bonus Feature
if grade in ["A+", "A"]:
    print("🏆 You are eligible for the Honor Roll!")
