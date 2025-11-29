# 🌟 Day 28 – Advanced Python Functions
# Part of Python & AI – 90 Days Journey

# 1️⃣ Returning Multiple Values
def student_profile(name, age, country):
    return name, age, country

profile = student_profile("Jobanjit", 29, "Canada")
print("Profile:", profile)


# 2️⃣ *args – Unlimited Positional Arguments
def sum_numbers(*nums):
    total = sum(nums)
    return total

print("Sum:", sum_numbers(5, 10, 15, 20))

# 3️⃣ **kwargs – Unlimited Keyword Arguments
def describe_person(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

describe_person(name="Joban", role="Cloud Network Engineer", country="Canada")

# 4️⃣ Lambda Functions (Small Inline Functions)
square = lambda x: x * x
print("Square of 7:", square(7))

add = lambda a, b: a + b
print("Add:", add(10, 20))

# 5️⃣ Function Inside a Function
def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

result = outer_function(10)
print("Inner Result:", result(20))


# 6️⃣ Real-Life Use Case: Applying Discount
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

discounted_value = apply_discount(200, 15)
print("Discounted Price:", discounted_value)
