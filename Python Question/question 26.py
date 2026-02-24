#Check whether a number is Armstrong
num = int(input())
original = num
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit ** 3  # assuming 3-digit number
    num //= 10
if sum_digits == original:
    print("Yes")
else:
    print("No")