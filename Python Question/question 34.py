#Find sum of first N natural numbers.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2