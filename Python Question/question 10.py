#Reverse a given number.
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10          # Get the last digit
    reverse = reverse * 10 + digit   # Append it to reversed number
    num = num // 10            # Remove the last digit

print("Reversed number is:", reverse)