# Iteration_statement.py
# 10 Python Iteration Statement Examples

# 1. For Loop Basics
print("1. For Loop Basics:")
for i in range(1, 11):
    print(i, end=" ")
print("\n" + "-"*30)

# 2. Sum of Even Numbers from 1 to 50
print("2. Sum of Even Numbers from 1 to 50:")
sum_even = 0
for i in range(2, 51, 2):
    sum_even += i
print("Sum =", sum_even)
print("-"*30)

# 3. While Loop from 10 to 1
print("3. While Loop from 10 to 1:")
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print("\n" + "-"*30)

# 4. List Iteration - Uppercase Fruits
print("4. List Iteration - Uppercase Fruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())
print("-"*30)

# 5. Nested Loops - 3x3 Grid
print("5. Nested Loops - 3x3 Grid:")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
print("-"*30)

# 6. Break Statement - Stop at 5
print("6. Break Statement - Stop at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print("\n" + "-"*30)

# 7. Continue Statement - Skip multiples of 3
print("7. Continue Statement - Skip multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print("\n" + "-"*30)

# 8. Loop with Else - First divisible by 7
print("8. Loop with Else - First divisible by 7:")
for i in range(2, 11):
    if i % 7 == 0:
        print("First number divisible by 7 is", i)
        break
else:
    print("No number found")
print("-"*30)

# 9. Count Vowels in a String
print("9. Count Vowels in a String:")
text = "Programming"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels in '{text}':", count)
print("-"*30)

# 10. User Input Loop - Sum Until 0
print("10. User Input Loop - Sum Until 0:")
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum of entered numbers:", total)