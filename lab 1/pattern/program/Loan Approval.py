# Input applicant details
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income (₹): "))
existing_loans = float(input("Enter existing loan amount (₹): "))

# Initialize approval status
status = ""
reason = ""

# Check credit score
if credit_score < 600:
    status = "Rejected"
    reason = "Credit score below 600"
elif credit_score >= 750:
    status = "Approved"
else:  # Credit score between 600 and 749
    if monthly_income < 30000 and existing_loans > 500000:
        status = "Rejected"
        reason = "Low income (< ₹30,000) and high existing loans (> ₹5,00,000)"
    else:
        status = "Approved"

# Output
print(f"\nLoan Status: {status}")
if reason:
    print(f"Reason: {reason}")