# Input transaction details
amount = float(input("Enter transaction amount (₹): "))
account_age_months = int(input("Enter account age in months: "))
transaction_type = input("Enter transaction type (domestic/international): ").lower()

# Initialize flag
flagged = False

# Check suspicious transaction criteria
if amount > 200000 and account_age_months < 6 and transaction_type == "international":
    flagged = True

# Display result
if flagged:
    print("\n⚠ Suspicious transaction detected! Flagged for manual verification.")
else:
    print("\n✅ Transaction appears normal.")