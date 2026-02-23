temperatures = [34, 42, 46, 38, 40, 47]

# Hottest and coldest
hottest = max(temperatures)
coldest = min(temperatures)

# Replace above 45°C with "Heat Alert"
temperatures = ['Heat Alert' if t > 45 else t for t in temperatures]

# Count extreme days (>40°C)
extreme_days = sum(1 for t in temperatures if isinstance(t, int) and t > 40)

print("Temperatures:", temperatures)
print("Hottest:", hottest, "Coldest:", coldest)
print("Extreme Days:", extreme_days)