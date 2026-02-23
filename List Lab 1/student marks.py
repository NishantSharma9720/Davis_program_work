# Sample list of student marks (can include invalid marks)
student_marks = {
    "Alice": 95,
    "Bob": 105,      # Invalid
    "Charlie": 87,
    "David": -5,     # Invalid
    "Eva": 92,
    "Frank": 87
}

# Step 1: Remove invalid marks (<0 or >100)
valid_marks = {name: mark for name, mark in student_marks.items() if 0 <= mark <= 100}

# Step 2: Calculate average
if valid_marks:
    average = sum(valid_marks.values()) / len(valid_marks)
else:
    average = 0

# Step 3: Find topper(s)
if valid_marks:
    max_mark = max(valid_marks.values())
    toppers = [name for name, mark in valid_marks.items() if mark == max_mark]
else:
    toppers = []

# Step 4: Assign grades based on average
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Step 5: Display results
print("Valid Marks:", valid_marks)
print("Average Marks:", average)
print("Grade based on Average:", grade(average))
print("Topper(s):", toppers)