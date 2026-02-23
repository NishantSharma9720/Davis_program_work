# Emergency Triage System

# Input patient details
age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate (bpm): "))
injury_severity = input("Enter injury severity (none/mild/severe): ").lower()

# Initialize condition
condition = "Normal"

# Check for Critical
if heart_rate < 50 or heart_rate > 120 or injury_severity == "severe":
    condition = "Critical"
# Check for Moderate
elif injury_severity == "mild":
    condition = "Moderate"

# Upgrade priority for age > 65 and condition moderate
if condition == "Moderate" and age > 65:
    condition = "High Priority (Moderate upgraded due to age)"

print(f"\nPatient Triage Status: {condition}")