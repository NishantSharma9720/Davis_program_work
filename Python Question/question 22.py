#Find factorial using while loop.
def factorial_while_loop(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result