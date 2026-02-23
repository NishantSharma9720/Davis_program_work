import math

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))

# Curved Surface Area
csa = 2 * math.pi * radius * height

# Total Surface Area
tsa = 2 * math.pi * radius * (radius + height)

print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)