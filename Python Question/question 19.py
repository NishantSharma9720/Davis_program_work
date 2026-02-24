#Check whether a number lies within a given range.
def check_number_in_range(number, lower, upper):
    if lower <= number <= upper:
        return True
    else:
        return False

# Example usage
number = 25
lower = 10
upper = 30
result = check_number_in_range(number, lower, upper)
print(f"Number {number} is within range {lower}-{upper}? {result}")