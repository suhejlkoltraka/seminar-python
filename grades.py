name = input("Enter student's name: ")
score = float(input("Enter test score (0–100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if score >= 60:
    result = "Pass"
else:
    result = "Fail"

print("\nStudent Name:", name)
print("Score:", score)
print("Grade:", grade)
print("Result:", result)
