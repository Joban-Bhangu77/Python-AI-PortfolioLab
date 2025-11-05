# 1️⃣ Basic if-elif-else example

temperature = 25
 
if temperature > 30:
 print ("It's is a hot day!")
elif temperature > 20: 
 print("It's a nice day!")
else:
 print("Its cold outstide!")

# 2️⃣ Nested if example
age = 18
has_id = True

if age >= 18:
    if has_id:
        print("Access Granted ✅")
    else:
        print("ID Required ❌")

 
#3️⃣ Match-case example (Python 3.10+)

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week 💼")
    case "Friday":
        print("Weekend is near 🎉")
    case "Sunday":
        print("Rest day 😴")
    case _:
        print("Midweek hustle 🔥")


# 4️⃣ Inline (Ternary) condition
number = 7
result = "Even ✅" if number % 2 == 0 else "Odd ❌"
print(result)