# Inputs
balance = float(input("Enter account balance: ₹"))
atm_cash = float(input("Enter ATM available cash: ₹"))
withdraw = float(input("Enter withdrawal amount: ₹"))

# Daily withdrawal limit
daily_limit = 50000

# Check conditions
if withdraw > balance:
    print("Transaction failed: Insufficient account balance.")
elif withdraw > daily_limit:
    print(f"Transaction failed: Daily withdrawal limit ₹{daily_limit} exceeded.")
elif withdraw > atm_cash:
    print("Transaction failed: ATM does not have sufficient cash.")
else:
    balance -= withdraw
    atm_cash -= withdraw
    print(f"Transaction successful! Withdrawn: ₹{withdraw}")
    print(f"Remaining account balance: ₹{balance}")
    print(f"Remaining ATM cash: ₹{atm_cash}")