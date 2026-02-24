# Print multiplication tables from 1 to 10.
def print_multiplication_tables():
    for i in range(1, 11):
        print(f"Multiplication Table for {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Add a blank line after each table