# student report card generator
name = input("Enter Student Name: ")

tamil = int(input("Enter Tamil Mark: "))
english = int(input("Enter English Mark: "))
math = int(input("Enter Math Mark: "))
science = int(input("Enter Science Mark: "))
social = int(input("Enter Social Mark: "))

# Total, Average and Percentage
total = tamil + english + math + science + social
average = total / 5
percentage = (total / 500) * 100

# Grade Calculation
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Pass or Fail
if tamil >= 35 and english >= 35 and math >= 35 and science >= 35 and social >= 35:
    result = "PASS"
else:
    result = "FAIL"

# Highest and Lowest Mark
highest = max(tamil, english, math, science, social)
lowest = min(tamil, english, math, science, social)

# Best Subject
marks = {
    "Tamil": tamil,
    "English": english,
    "Math": math,
    "Science": science,
    "Social": social
}

best_subject = max(marks, key=marks.get)

# Scholarship Eligibility
if average >= 85:
    scholarship = "Eligible"
else:
    scholarship = "Not Eligible"

# Distinction Check
if average >= 75:
    distinction = "Yes"
else:
    distinction = "No"

# Overall Performance
if average >= 90:
    performance = "Outstanding"
elif average >= 75:
    performance = "Excellent"
elif average >= 60:
    performance = "Good"
elif average >= 50:
    performance = "Average"
else:
    performance = "Poor"

# Remarks
if average >= 90:
    remarks = "Excellent"
elif average >= 75:
    remarks = "Very Good"
elif average >= 50:
    remarks = "Good"
else:
    remarks = "Needs Improvement"

# Report
print("\n========== STUDENT REPORT ==========")
print("Name            :", name)
print("Total           :", total, "/500")
print("Average         :", round(average, 2))
print("Percentage      :", round(percentage, 2), "%")
print("Grade           :", grade)
print("Result          :", result)
print("Highest Mark    :", highest)
print("Lowest Mark     :", lowest)
print("Best Subject    :", best_subject)
print("Performance     :", performance)
print("Scholarship     :", scholarship)
print("Distinction     :", distinction)
print("Remarks         :", remarks)
print("====================================")

