name = "Jobanjit"
age = 29
height = 6.1 
is_learning = True
hobbies = ["Coding", "Soccer", "Reading"]

print("Hello,", name) 
print("Age:", age)
print("Height:", height)
print("Learning Python", is_learning)
print("Hobbies:", hobbies)

print("Age in 5 years", age + 5)
print("Uppercase Name:", name.upper())
print("First Hobby:", hobbies[0])

import random
print("\nWelcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == number_to_guess:
    print("🎉 Congratulations! You guessed it right!")
else:
    print(f"❌ Sorry! The correct number was {number_to_guess}")

