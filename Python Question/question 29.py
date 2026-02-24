#Find GCD using while loop.
def gcd_while_loop(a, b):
    while b:
        a, b = b, a % b
    return a