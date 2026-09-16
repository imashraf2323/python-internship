# Write a Python program that takes marks of **5 subjects** as input and:

# - Calculate the **total** and **percentage** using arithmetic operators.

# - Determine the grade using **conditional statements**:
#     - `90+` → A
#     - `75–89` → B
#     - `60–74` → C
#     - `40–59` → D
#     - Below `40` → Fail
# - Use a **loop** to take the marks of all 5 subjects.
# - Display the total, percentage, and grade.


# subject1_marks = int(input("Enter marks of each subject:"))

totalSubjectMarks = 500
total = 0

for i in range(1, 6) :
  marks = int(input(f"Enter marks for subject - {i} = "))
  total += marks


print(f"Total marks is = {total}")
print(f"Total percentage is = {total/5}")

# coditions
if total >= 90 :
  print("Grade : A")
elif total > 75 & total < 89:
   print("Grade : B")
elif total > 60 & total < 74:
   print("Grade : C")
elif total > 40 & total < 59:
   print("Grade : D")
else:
   print("You Failed :( ")

