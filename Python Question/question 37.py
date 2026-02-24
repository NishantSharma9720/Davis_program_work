#Generate Fibonacci series using for loop.
def fibonacci_series(n):
    if n < 1:
        return "Input must be a positive integer."
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series