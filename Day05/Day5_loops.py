# Day 5 - Loops in Python

# For Loop Example
print("For Loop Example:")
for i in range(5):
    print("Iteration:", i)

print("\nWhile Loop Example:")
# While Loop Example
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Using break and continue
print("\nBreak and Continue Example:")
for num in range(10):
    if num == 5:
        break  # stop when num == 5
    if num % 2 == 0:
        continue  # skip even numbers
    print("Odd Number:", num)
