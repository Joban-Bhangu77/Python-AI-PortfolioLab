# Day 29 – Python Functions, Args/Kwargs, Lambda Expressions & Smart Calculator  
Part of the Python & AI – 90 Days Journey

---

## Introduction  
Day 29 of my Python & AI learning journey focused on mastering the most important part of Python programming: functions. Functions make code clean, modular, reusable, and scalable. They power automation, DevOps, backend systems, and AI workflows.

Today, I practiced:
- Function arguments  
- Default arguments  
- *args  
- **kwargs  
- Lambda expressions  
- A full Smart Calculator project  

---

## Why This Day Was Important  
Functions are the foundation for:
- Real-world applications  
- AI/ML preprocessing pipelines  
- Backend services  
- Automation scripts  
- Clean and maintainable code  

Mastering functions means mastering Python.

---

## Function Concepts Practiced

### 1. Function Arguments
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Joban", 29)

3. *args – Multiple Positional Arguments
def add_numbers(*nums):
    return sum(nums)

print(add_numbers(10, 20, 30, 40))

4. **kwargs – Multiple Keyword Arguments
def user_info(**details):
    print(details)

user_info(name="Joban", role="Cloud Engineer", country="Canada")

5. Lambda Expressions
square = lambda x: x * x
add = lambda a, b: a + b

print(square(7))
print(add(10, 20))

Smart Calculator Project (Full Code)
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
        return "Cannot divide by zero"
    return a / b

def smart_calculator():
    print("\nSmart Calculator – Joban Edition")
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

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
        print("Invalid Option")

smart_calculator()

Key Takeaways

Functions help write clean and reusable code

*args and **kwargs make functions flexible

Lambda expressions simplify quick operations

Calculator project helped build logic and structure

These concepts strengthen the base for AI, automation, and large Python applications

Conclusion

Day 29 was a strong step into writing modular, well-structured, and production-style Python code. Functions are essential for every upcoming concept like OOP, APIs, ML pipelines, data processing, and automation.

On to Day 30!