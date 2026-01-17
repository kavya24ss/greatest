import sys
classes_held = int(sys.argv[1])
classes_attended = int(sys.argv[2])

percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")