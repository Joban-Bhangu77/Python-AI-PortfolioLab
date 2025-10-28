name = input("what your name?")
mood = input("How are you feeling today? (happy/sad/tired/angry):").lower()
print(f"/nHello {name}! Let's check your mood...")

if mood == "happy":
    print("😊 That's awesome! Keep spreading positivity!")
elif mood == "sad":
    print ("💖 It's okay to feel low sometimes. Better days are coming!")
elif mood == "tired":
    print ("😴 You should take a short break or nap. You’ve earned it!")
elif mood == "angry":
    print ("🔥 Take a deep breath, calm down — you’ve got this!")
else:
    print("🤔 Hmm... that's a unique mood! Stay balanced and positive!")

print("\nEnd of Day 4 - Learning Conditional Logic in Python 💻")

