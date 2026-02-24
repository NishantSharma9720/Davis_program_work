#Determine the type of triangle.
def triangle_type(a, b, c):
    # Check for a valid triangle
    if a + b <= c or b + c <= a or a + c <= b:
        return "Not a valid triangle"
    
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Example usage
a, b, c = 5, 5, 8
print(triangle_type(a, b, c))