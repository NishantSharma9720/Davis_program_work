# Input student details
percentage_12th = float(input("Enter 12th grade percentage: "))
studied_math = input("Did the student study Mathematics? (yes/no): ").lower()
entrance_score = float(input("Enter entrance exam score: "))

# Initialize eligibility
eligible = True
reasons = []

# Check 12th grade percentage
if percentage_12th < 75:
    eligible = False
    reasons.append("12th grade percentage less than 75%")

# Check if Mathematics was studied
if studied_math != "yes":
    eligible = False
    reasons.append("Mathematics not studied in 12th grade")

# Check entrance exam score
if entrance_score < 80:
    eligible = False
    reasons.append("Entrance exam score less than 80")

# Output result
if eligible:
    print("\n✅ Student is eligible for admission.")
else:
    print("\n❌ Student is NOT eligible for admission due to:")
    for reason in reasons:
        print(f"- {reason}")