#Accept numbers until 0 is entered and print sum.
total_sum = 0
while True:
    num = int(input())
    if num == 0:
        break
    total_sum += num