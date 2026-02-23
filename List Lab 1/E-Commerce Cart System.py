cart_prices = [1200, 2500, 1200, 500, 3000]

# Remove duplicates
unique_prices = list(set(cart_prices))

# Calculate total
total = sum(unique_prices)

# Apply 10% discount if total > 5000
if total > 5000:
    total *= 0.9

# Add GST 18%
final_amount = total * 1.18

print("Final Payable Amount: ₹", round(final_amount, 2))