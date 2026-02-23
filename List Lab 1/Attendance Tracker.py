attendance = [1, 0, 1, 0, 0, 1, 1, 0, 0, 0]  # 1 = present, 0 = absent

# Calculate attendance %
attendance_percent = sum(attendance) / len(attendance) * 100

# Students below 75%
status = "Below 75%" if attendance_percent < 75 else "Satisfactory"

# Replace consecutive absences with warning flag
warning_attendance = []
consecutive_absence = 0
for mark in attendance:
    if mark == 0:
        consecutive_absence += 1
    else:
        consecutive_absence = 0
    warning_attendance.append('Warning' if consecutive_absence >= 2 else mark)

print("Attendance %:", attendance_percent)
print("Status:", status)
print("Attendance with Warnings:", warning_attendance)