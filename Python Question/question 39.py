# Calculate power without using exponent operator.
def power(base, exponent):
    if exponent < 0:
        return "Exponent must be a non-negative integer."
    if exponent == 0:
        return 1
    result = 1
    for _ in range(exponent):
        result *= base
    return result