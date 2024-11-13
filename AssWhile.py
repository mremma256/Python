"""#1. Basic Countdown: Write a while loop to count down from 10 to 1 and print each number.
condition = 10
while condition >= 1:
    print(condition)
    condition -= 1

#2. Sum of Natural Numbers: Use a while loop to find the sum of the first 20 natural numbers.
condition = 0
condition1 = 1
while condition1 <= 20:
    condition += condition1
    condition1 += 1
    print(condition)

#3. Even Numbers Up to 50: Write a while loop to print all even numbers between 1 and 50.
condition = 2
while condition < 50:
    print(condition)
    condition += 2

#4. Password Attempts: Create a while loop that allows the user to enter a password up to 3 times.
#If the password is correct before 3 attempts, print "Access granted".

password = "Emma256"

attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password_input = input("Enter your Password: ")
    Password = password_input == password
    
    if Password:
        print("Access granted!")
        break
    else:
        print("wrong password!. Please try again.")
        attempts += 1

#5. Prime Numbers Less Than 20: Use a while loop to print all prime numbers less than 20.
def prime(condition):
    if condition <= 1:
        return False
    if condition == 2:
        return True 
    if condition % 2 == 0:
        return False
    
    i = 3
    while i * i <= condition:
        if condition % i == 0:
            return False
        i += 2 
    return True

number = 2
while number < 20:
    if prime(number):
        print(number)
    number += 1

#6. User Input Sum: Write a while loop to keep taking numbers from the user and
#   adding them to a sum until the user enters '0'.
sum = 0
while True:
    number = input("Enter number: ")
    num = int(number)
    if num == 0:
        break
    sum += num
print(f"Sum is: {sum}")
"""
#7. Multiplication Table: Use a while loop to print the multiplication table of a given number up to
num = int(input("Enter number: "))
condition = 1
while condition <= num:
    result = num * condition
    print(f"{condition} x {num} = {result}")
    condition += 1
