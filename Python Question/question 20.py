#Find the greatest of four numbers.
def greatest_of_four(a, b, c, d):
    greatest = a  # Assume a is the greatest initially
    
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    if d > greatest:
        greatest = d
        
    return greatest

# Example usage
a, b, c, d = 12, 45, 7, 33
print(f"The greatest number is: {greatest_of_four(a, b, c, d)}")