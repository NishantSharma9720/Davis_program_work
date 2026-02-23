scores = [28, 34, 45, 32, 50, 25, 30]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks 5 for scores between 30-35
scores = [s+5 if 30 <= s <= 35 else s for s in scores]

# Count passed students (>=40)
passed_count = sum(1 for s in scores if s >= 40)

print("Processed Scores:", scores)
print("Number of Passed Students:", passed_count)