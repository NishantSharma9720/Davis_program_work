#Print all divisors of a number.
def print_divisors(n):
    if n < 1:
        return "Input must be a positive integer."
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors