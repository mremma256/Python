from colorama import Back, Fore
Course_work = 17.5
Exam_pass = 17.5
name = input("Enter Name: ")
clas = input("Enter Class: ")
CW_input = float(input("Enter Coursework Mark: "))
CW_Mark = (CW_input/100)*50
if CW_Mark < 17.5:
   print(Fore.RED + "Failed!" + Fore.RESET)
else:
   print(Fore.GREEN + "Passed!" + Fore.RESET)
print("Have you attended Class!")
print("1. Yes")
print("2. No")

operation = input()
if operation == '1':
    print("Yes")
else:
    print("No")

if CW_Mark >= 17.5 and operation == '1':
    print(Fore.GREEN + "You are allowed to do Exams!" + Fore.RESET)
    print(Fore.GREEN + "==== PASSED! ====" + Fore.RESET)
else:
    print(Fore.RED + "You are not allowed to do Exams!" + Fore.RESET)
    print(Fore.RED + "==== FAILED! ====" + Fore.RESET)
print()
Exam_input = float(input("Enter Exam Mark: "))
EX_mark = (Exam_input/100)*50
if EX_mark < 17.5:
   print(Fore.RED + "Failed!" + Fore.RESET)
else:
   print(Fore.GREEN + "Passed!" + Fore.RESET)
if EX_mark >= 17.5:
    print(Fore.GREEN + "Proceed to Year 1 Semester 2!" + Fore.RESET)
    print(Fore.GREEN + "==== Congratulations! ====" + Fore.RESET)
else:
    print(Fore.RED + "Retake Year 1 semester 1!" + Fore.RESET)
    print(Fore.RED + "==== FAILED! ====" + Fore.RESET)
print()


