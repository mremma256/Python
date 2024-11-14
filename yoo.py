print("Welcome to the simple calculator!")
print("Please choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
    
operation = input("Enter the number of the operation you want to perform: ")
    
if operation in('1', '2', '3', '4'):
 num1 = int(input("Enter the first number: "))
 print("Great!")
num2 = int(input("Enter the second number: "))

Add = num1+num2
Subtract = num1-num2
Multiply = num1*num2
Divide = num1/num2

input1 = input(f"What is {num1} + {num2} = ")
if input1 == Add:
    print("Correct")
else:
    print("Wrong answer! correct answer is", input1)
if operation == '2':
    print(f"What is {num1} - {num2} ?")
    right_answer = num1-num2

if operation == '3':
    print(f"What is {num1} * {num2} ?")
    right_answer = num1*num2

if operation == '4':
    print(f"What is {num1} / {num2} ?")
    right_answer = num1/num2
