#Calculate BMI category.
def bmi_category(weight, height):
    if height <= 0:
        return "Invalid height"
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"
    
    return f"BMI: {bmi:.2f}, Category: {category}"

# Example usage
weight = 70  # in kg
height = 1.75  # in meters
print(bmi_category(weight, height))