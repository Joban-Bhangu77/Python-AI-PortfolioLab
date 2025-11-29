
### 1. For Loop
for i in range(5):
    print("Iteration Number:", i)

### 2. For Loop With List
fruits = ["apple", "Banana", "Cherry"]
for fruit in fruits:
 print("I like", fruits)

### 3. While Loop
count = 1
while count <=5:
   print ("counting:",count)
   count +=1

### 4. Break & Continue
   for number in range(1, 10):
      if number == 5:
         break   # Stops the loop
      print(number)

for number in range (1, 10):
   if number == 5:
      continue    # Skips number 5
   print(number)

### 5. Mini Project: Even-Odd Number Finder
print("Welcome to Day 8: Even and Odd Number Finder!")

for num in range(1, 11):
   if num % 2 == 0:
      print(num, "is Even")
   else:
      print(num, "is Odd")

      print("Loop complete! Great Job, Man..!!")