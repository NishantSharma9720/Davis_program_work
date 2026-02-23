# Program to calculate Simple Interest

# Taking input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Displaying the result
print("Simple Interest =", simple_interest)