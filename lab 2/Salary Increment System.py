# Employee details
salary = float(input("Enter current salary: ₹"))
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

# Base increment based on performance
if rating == 5:
    increment = 10
elif rating == 4:
    increment = 7
elif rating == 3:
    increment = 5
elif rating == 2:
    increment = 2
else:
    increment = 0

# Bonus for experience
if experience > 5:
    increment += 2

# Bonus for good attendance
if attendance > 95:
    increment += 1

# Calculate increment amount
increment_amount = salary * increment / 100
new_salary = salary + increment_amount

print(f"\nIncrement Percentage: {increment}%")
print(f"Increment Amount: ₹{increment_amount:.2f}")
print(f"New Salary: ₹{new_salary:.2f}")