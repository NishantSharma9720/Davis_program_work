#Generate Fibonacci series using while loop.
def fibonacci_while_loop(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1