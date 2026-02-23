import math

radius = float(input("Enter radius of cone: "))
slant_height = float(input("Enter slant height of cone: "))

csa = math.pi * radius * slant_height

print("Curved Surface Area of Cone =", csa)