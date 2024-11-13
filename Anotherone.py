CWk = 17.5
Exam_pass = 17.5
CW_input = float(input("Enter Coursework Mark: "))
CW_Mark = (CW_input/100)*50
print("Have you attended Class?")
print("1. Yes")
print("2. No")
operation = input()
if CW_Mark >= 17.5 and operation == '1':
    print("You are allowed to do Exams!")
else:
    print("You are not allowed to do Exams!")
Exam_input = float(input("Enter Exam Mark: "))
EX_mark = (Exam_input/100)*50
if EX_mark >= 17.5:
    print("Proceed to Year 1 Semester 2")
    print("Congratulations")
else:
    print("FAILED")


