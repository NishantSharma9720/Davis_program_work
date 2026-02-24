#Assign grades based on marks.
def assign_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Example usage
marks = 76
grade = assign_grade(marks)
print(f"Marks: {marks}, Grade: {grade}")