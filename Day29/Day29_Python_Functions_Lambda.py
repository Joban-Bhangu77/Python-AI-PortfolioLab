# -------------------------------
# Day 29 - Python Functions, Args, Kwargs, Lambda + Smart Calculator
# -------------------------------

# 1. Basic Function
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

# Call the function
greet("Jobanjit", 29)


# 2. Default Argument
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()
welcome("Joban")


# 3. *args Example
def add_numbers(*nums):
    return sum(nums)

print("\nAddition Result:", add_numbers(10, 20, 30, 40))


# 4. **kwargs Example
def user_info(**details):
    print("\nUser Details:", details)

user_info(name="Joban", role="Cloud Engineer", country="Canada")


# 5. Lambda Functions
square = lambda x: x * x
print("\nSquare of 7:", square(7))

add = lambda a, b: a + b
print("Lambda Add (10 + 20):", add(10, 20))


# -------------------------------
# SMART CALCULATOR PROJECT
# -------------------------------

def add(*nums):
    return sum(nums)

def subtract(a, b):
    return a - b

def multiply(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b


def smart_calculator():
    print("\n🤖 Smart Calculator – Joban Edition 🤖")

    print("\nSelect Operation:")
    print("1️⃣ Add")
    print("2️⃣ Subtract")
    print("3️⃣ Multiply")
    print("4️⃣ Divide")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Result:", add(*numbers))

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == "3":
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Result:", multiply(*numbers))

    elif choice == "4":
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result:", divide(a, b))

    else:
        print("❌ Invalid Option")


# CALL THE CALCULATOR
smart_calculator()

print("\n✅ Day 29 Code Completed Successfully!")
