#Multiplication Table
number = int(input("Enter Mark: "))
condition = 0
while condition<number:
    condition += 1
    result = condition*number
    print(f"{condition}x{number}={result}")

#counting number of words
text = input("Enter Text: ")
word_count = len(text.split())
print(f"Text has: {word_count} word[s]")

#counting no. of letters in text
text = input("Enter Text: ")
word_count = len(text)
print(f"Text has: {word_count} letter[s]")

#checking if text is a palindrome
string = input("Enter Text: ")
output = string [::-1]
if output == string:
    print("Text input is a palindrome")
else:
    print("Text input is not a palindrome")

#reversing without using built in function
string = input("Enter Text: ")
output = string [::-1]
print(output)

#Substring of one text in another
string = input("Enter Text 1: ")
string1 = input("Enter Text 2: ")
sorted_string1 = sorted(string)
sorted_string2 = sorted(string1)
if sorted_string1 == sorted_string2:
    print("Text 2 is a Substring of Text 1")
else:
    print("Text 2 is not a Substring of Text 1")

#Fizz Buzz
for num in range(1, 100):
    if num%3 ==0 and num%5 ==0:
        print("FizzBuzz")
    elif num%5 ==0:
        print("Buzz")
    elif num%3 ==0:
        print("Fizz")
    else:
        print(num)

#summation of Even Numbers upto upper limit
upper_limit = int(input("Enter Number: "))
condition = 1
sum_even = 0 
while condition < upper_limit:
    if condition % 2 == 0:
        print(condition)
        sum_even += condition
    condition += 1
print("Sum of even numbers up to", upper_limit, "is:", sum_even)
