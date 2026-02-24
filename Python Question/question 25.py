# Find sum of even numbers up to N
N = int(input())
sum_even = 0
i = 2
while i <= N:
    sum_even += i
    i += 2
print(sum_even)