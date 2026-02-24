#Check whether a number is even or odd without modulus operator.
num = int(input("Enter a number: "))

if num // 2 * 2 == num:
    print("Even number")
else:
    print("Odd number")