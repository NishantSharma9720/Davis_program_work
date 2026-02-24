# Check whether a number is divisible by both 3 and 5.
def divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

# Example usage
num = 30
result = divisible_by_3_and_5(num)
print(f"Number: {num}, Divisible by both 3 and 5? {result}")