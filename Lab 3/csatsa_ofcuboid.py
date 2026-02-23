length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))

# Curved Surface Area (Lateral Surface Area)
csa = 2 * height * (length + breadth)

# Total Surface Area
tsa = 2 * (length * breadth + breadth * height + height * length)

print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)