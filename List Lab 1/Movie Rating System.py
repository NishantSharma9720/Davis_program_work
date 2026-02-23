ratings = [5, 4, 6, 3, 5, 0, 2]

# Remove invalid ratings
valid_ratings = [r for r in ratings if 1 <= r <= 5]

# Average rating
avg_rating = sum(valid_ratings)/len(valid_ratings)

# Count 5-star ratings
five_star_count = valid_ratings.count(5)

# Sort ascending
valid_ratings.sort()

print("Valid Ratings:", valid_ratings)
print("Average Rating:", avg_rating)
print("5-Star Ratings:", five_star_count)