transactions = [15000, -5000, 7000, -12000, 20000]

# Total balance
balance = sum(transactions)

# Largest withdrawal
largest_withdrawal = min(transactions)

# Count deposits > 10000
large_deposits = sum(1 for t in transactions if t > 10000)

print("Total Balance: ₹", balance)
print("Largest Withdrawal: ₹", largest_withdrawal)
print("Deposits > ₹10000:", large_deposits)