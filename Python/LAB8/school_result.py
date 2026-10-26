print("="*100)
print("                SCHOOL RESULT PROCESSING")
print("="*100)
name=input("Enter Student Name: ")
no=input("Enter Roll Number: ")
print("\n")
print("----- Enter Marks for 5 Subjects(0-100) -----")
total=0
passed=True
for i in range(1,6):
  marks=float(input(f"Enter marks for subject {i}: "))
  if marks<0 or marks>100:
    print("Invalid marks! Marks must be between 0 and 100.")
    break
  total+=marks
  if marks<40:
    passed=False
percentage=(total/500)*100
if not passed:
  result="FAIL"
  grade="F"
  remark="Failed in one or more subjects"  
elif percentage>=90:
  result="PASS"
  grade="A+"
  remark="Outstanding"
elif percentage>=80:
  result="PASS"
  grade="A"
  remark="Excellent"
elif percentage>=70:
  result="PASS"
  grade="B"
  remark="Very Good"
elif percentage>=60:
  result="PASS"
  grade="C"
  remark="Good"
elif percentage>=40:
  result="PASS"
  grade="E"
  remark="Pass"
else:
  result="FAIL"
  grade="F"
  remark="Fail"

print("="*100)
print("         STUDENT REPORT CARD")
print("="*100)
print(f"Student Name: {name}")
print(f"Roll Number:   {no}")
print("-"*100)
print(f"Total Marks: {total}")
print(f"Percentage: {percentage}")
print(f"Result: {result}")
print(f"Grade: {grade}")
print(f"Remarks: {remark}")
print("="*100)