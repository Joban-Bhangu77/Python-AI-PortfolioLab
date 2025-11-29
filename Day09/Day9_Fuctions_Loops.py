
### 1.Functions Basics:
# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to Day 9 of Python practice.")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function with default parameter
def favorite_hobby(hobby="Coding"):
    print(f"My favorite hobby is {hobby}")

# Testing the functions
greet_user("Jobanjit")
result = add_numbers(5, 7)
print("Sum:", result)
favorite_hobby()
favorite_hobby("Soccer")

### 2. Loops Basics: 
# For loop example
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop example
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

###Step 3: Mini Project – Quiz Game
# Quiz Game using functions and loops

def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("🎉 Correct!")
        return 1
    else:
        print(f"❌ Wrong! The correct answer was: {answer}")
        return 0

# List of questions
quiz_questions = [
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Which hobby do you love most?", "answer": "Coding"}
]

score = 0

for q in quiz_questions:
    score += ask_question(q["question"], q["answer"])

print(f"\nYour final score is: {score} out of {len(quiz_questions)}")
