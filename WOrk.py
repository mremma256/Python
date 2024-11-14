#Qn2: Guess a number between 1 and 20
while True:
 guess = int(input("Guess a number between 1 and 20: "))
 if guess == 15:
  print("Well guessed!")
  break

#Qn4: Program that accepts a word from the user and reverses it. 
word = input("Enter a word: ")
reversed_word = word

#Qn8: Multiplication table for a given number. 
num = int(input("Enter number: "))
condition = 1
while condition <= 10:
    result = num * condition
    print(f"{num} x {condition} = {result}")
    condition += 1

#Qn12: Program that accepts a string and calculates the number of uppercase letters and lowercase letters
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
     if char.isupper():
            upper_count += 1
     elif char.islower():
            lower_count += 1
    return upper_count, lower_count
input_string = input("Enter Word: ")
upper_count, lower_count = count_upper_lower(input_string)
print(f"Uppercase letters : {upper_count}")
print(f"Lowercase letters : {lower_count}")

#Qn13: Validity of passwords input by users.
import string
password = input("Enter a password: ")
alphabet_letters = string.ascii_lowercase
alphabet_letters1 = string.ascii_uppercase
alphabet_digits = string.digits
alphabet_special = string.punctuation

if len(password) < 8 or len(password) > 16:
    print("Password must be between 8 and 16 characters!")

elif not any(char in alphabet_letters for char in password) or not any(char in alphabet_letters1 for char in password):
    print("Password must contain at least one Uppercase & Lowercase letter!")

elif not any(char in alphabet_special for char in password):
    print("Password must contain at least one special character [$%&]")

elif not any(char in alphabet_digits for char in password):
    print("Password must contain at least one number!")

else:
    print("Password is valid!")

#Qn39: Number is positive, negative or zero
number = int(input("Input a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

#Qn47: Previous day of a given date
year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))
prev_date = day - 1
print(f"The previous date is [yyyy-mm-dd] {year}-{month}-{prev_date}")

#Qn48: Calculate the product and average of n integer numbers (input from the user). Input 0 to finish
def main():
    numbers = []
    
    while True:
        num = int(input("Enter Number (enter 0 to finish): "))
        
        if num == 0:
            break
        
        numbers.append(num)
    
    if not numbers:
        print("No numbers were entered.")
        return
    
    product = 1
    for num in numbers:
        product *= num
    
    average = sum(numbers) / len(numbers)
    
    print(f"Product of the numbers: {product}")
    print(f"Average of the numbers: {average}")
if __name__ == "__main__":
    main()

#Qn49: Create the division table (from 1 to 10) of a number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} / {i} = {number/i}")
    
#Qn50: Using a nested loop number. 
condition = 10
for N in range(condition):
    for No in range(N, -1, -1):
        print(No, end='')
    print()