#Qn1:Maximum of three numbers
def find_max(num1, num2, num3):
    maximum = max(num1, num2, num3)
    return maximum
num1 = 10
num2 = 5
num3 = 20
print(f"The maximum of {num1}, {num2}, and {num3} is: {find_max(num1, num2, num3)}")

#Qn2:summing all numbers in a list
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
my_list = [1, 2, 3, 4, 5]
print(f"The sum of numbers in the list {my_list} is: {sum_list(my_list)}")

#Qn3:multipying all numbers in a list
def multiply_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
my_list = [1, 2, 3, 4, 5]
print(f"The product of numbers in the list {my_list} is: {multiply_list(my_list)}")

#Qn4:reversing a sting
def reverse_string(input_string):
    return input_string[::-1]
my_string = "Hello, world!"
reversed_string = reverse_string(my_string)
print(f"The reversed string of '{my_string}' is: '{reversed_string}'")

#Qn7:counting no. of Upper Case and lower case letters
def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count
my_string = input("Enter String: ")
upper_count, lower_count = count_upper_lower(my_string)
print(f"Original string: {my_string}")
print(f"Number of uppercase letters: {upper_count}")
print(f"Number of lowercase letters: {lower_count}")



#Qn1:summing all items in a list
numbers = [1, 2, 3, 4]
add = sum(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {add}")

#Qn2:multipying all items in a list
numbers = [1, 2, 3, 4]
product = 1
print(f"Numbers: {numbers}")
for num in numbers:
    product *= num
print(f"Product: {product}")

#Qn3:largest number from a list
numbers = [1, 2, 3, 4, 5]
largest = max(numbers)
print(f"Numbers: {numbers}")
print(f"Largest number: {largest}")

#Qn4:Smallest number from a list
numbers = [1, 2, 3, 4, 5]
smallest = min(numbers)
print(f"Numbers: {numbers}")
print(f"Maximum number: {smallest}")

#Qn7:Removing duplicates from a list
lis = [1, 2, 3, 4, 4, 6, 1, 8, 9]
unique_list = list(set(lis))
unique_list.sort()
print(unique_list)

#Qn9:Clone or copy a list
original = [1, 2, 3, 4, 5]
clone = original
print("Original List:", original)
print("Cloned List:", clone)

#Qn11:Checking for common member
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
if set1.intersection(set2):
    print("True, The lists have common member[s].")
else:
    print("False, The lists do not have any common member[s].")

#Qn12:Removing the 0th, 4th and 5th element from a list
lis = [1, 2, 3, 4, 5, 6]
indices_to_remove = [0, 4, 5]
filtered_list = [lis[i] for i in range(len(lis)) if i not in indices_to_remove]
print("Original List:", lis)
print("Modified List:", filtered_list)

#Qn15:List Shuffling
import random
lis = [1, 2, 3, 4, 5, 6]
random.shuffle(lis)
print("Shuffled List:", lis)

#Qn20:Coverting list of characters into a string
lis = [1, 2, 3, 4, 5, 6]
lis_str = ''.join(map(str, lis))
print("List as string:", lis_str)

#Qn1Dictionaries:ascending and descending a dictionary by value
dic = {'Emma': 2, 'Brian': 4, 'Riak': 3, 'Otto': 1}
sorted_dic1 = dict(sorted(dic.items(), key=lambda item: item[1]))
print("Sorted Dictionary (Ascending):", sorted_dic1)
sorted_dic2 = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
print("Sorted Dictionary (Descending):", sorted_dic2)

#Qn2Dictionaries:Adding a key to a dictionary
dic = {'Emma': 2, 'Brian': 4, 'Riak': 3, 'Otto': 1}
print("Dictionary:", dic)
dic['Charles'] = 5
print("Updated Dictionary:", dic)

#Qn1Tuples:Creating a tuple
tuple = (1, 2, 3, 4, 5)
print(tuple)

#Qn2Tuple:Tuple with different data types
tuple = ('apple', 3.14, True, (1, 2, 3))
print("Mixed data type tuple:", tuple)

#SETS:Qn1:Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

#SETS:Qn3:Adding to a set
my_set = {"Emma", "Riak", "Otto"}
print("Set:", my_set)
my_set.add("Charles")
print("Updated Set:", my_set)
