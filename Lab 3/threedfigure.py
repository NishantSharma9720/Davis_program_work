import math

def cube():
    a = float(input("Enter side of cube: "))
    csa = 4 * a * a
    tsa = 6 * a * a
    volume = a ** 3
    print(f"CSA = {csa}, TSA = {tsa}, Volume = {volume}")

def cuboid():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))
    csa = 2 * h * (l + b)
    tsa = 2 * (l*b + b*h + h*l)
    volume = l * b * h
    print(f"CSA = {csa}, TSA = {tsa}, Volume = {volume}")

def cylinder():
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    csa = 2 * math.pi * r * h
    tsa = 2 * math.pi * r * (r + h)
    volume = math.pi * r * r * h
    print(f"CSA = {csa}, TSA = {tsa}, Volume = {volume}")

def cone():
    r = float(input("Enter radius: "))
    l = float(input("Enter slant height: "))
    h = float(input("Enter height: "))
    csa = math.pi * r * l
    tsa = math.pi * r * (r + l)
    volume = (1/3) * math.pi * r * r * h
    print(f"CSA = {csa}, TSA = {tsa}, Volume = {volume}")

while True:
    print("\n--- 3D Figure Calculator ---")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cube()
    elif choice == "2":
        cuboid()
    elif choice == "3":
        cylinder()
    elif choice == "4":
        cone()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")