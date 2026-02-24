#Find the sum of digits of a number.
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10       # Get the last digit
    sum_digits += digit    # Add it to sum
    num = num // 10        # Remove the last digit

print("Sum of digits is:", sum_digits)