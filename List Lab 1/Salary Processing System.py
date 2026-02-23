salaries = [40000, 52000, 60000, 30000, 75000]

# Remove below minimum wage (assume 35000)
valid_salaries = [s for s in salaries if s >= 35000]

# Add 5% bonus if salary > 50000
valid_salaries = [s*1.05 if s > 50000 else s for s in valid_salaries]

# Sort descending
valid_salaries.sort(reverse=True)

# Top 3 salaries
top_3 = valid_salaries[:3]

print("Processed Salaries:", valid_salaries)
print("Top 3 Salaries:", top_3)