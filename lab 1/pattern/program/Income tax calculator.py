# Input user details
income = float(input("Enter your annual income (₹): "))
age = int(input("Enter your age: "))

# Determine exemption limit
if age >= 60:
    exemption_limit = 300000
else:
    exemption_limit = 250000

# Initialize tax
tax = 0

# Calculate tax based on slabs
if income <= exemption_limit:
    tax = 0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    tax = (500000 - exemption_limit) * 0.05 + (income - 500000) * 0.20
else:
    tax = (500000 - exemption_limit) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

print(f"\nIncome Tax to be paid: ₹{tax:.2f}")