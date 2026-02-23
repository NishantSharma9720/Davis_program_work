# Input details
cart_value = float(input("Enter cart value (₹): "))
membership = input("Enter membership type (Silver/Gold/Platinum): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

# Initialize discount percentages
discounts = []

# 1️⃣ Discount based on cart value
if cart_value >= 5000:
    discounts.append(10)   # 10% discount for cart ≥ ₹5000
elif cart_value >= 2000:
    discounts.append(5)    # 5% discount for cart ≥ ₹2000
else:
    discounts.append(0)    # No discount for cart < ₹2000

# 2️⃣ Discount based on membership
if membership == "platinum":
    discounts.append(15)
elif membership == "gold":
    discounts.append(10)
elif membership == "silver":
    discounts.append(5)
else:
    discounts.append(0)  # Non-members

# 3️⃣ Discount for festival season
if festival == "yes":
    discounts.append(20)
else:
    discounts.append(0)

# Apply highest eligible discount
max_discount = max(discounts)
final_amount = cart_value * (1 - max_discount / 100)

# Output
print(f"\nHighest Discount Applied: {max_discount}%")
print(f"Final Payable Amount: ₹{final_amount:.2f}")