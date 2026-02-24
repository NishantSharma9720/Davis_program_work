# Calculate compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (in years): "))

amount = principal * (1 + rate/100) ** time
compound_interest = amount - principal

print("Compound Interest is:", compound_interest)
print("Total Amount is:", amount)
