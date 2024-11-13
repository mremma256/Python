#Qn2: Character frequency count
def count_char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1   
    return freq
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    print(f"Character frequency: {count_char_frequency(input_string)}")

#Qn4: Concatenate and swap first two characters
def concatenate_and_swap(str1, str2):
    concatenated_str = str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]
    return concatenated_str
if __name__ == "__main__":
    string1 = input("Enter first word: ")
    string2 = input("Enter second word: ")
    print(f"Strings: ({string1}, {string2})")
    modified_string = concatenate_and_swap(string1, string2)
    print(f"Modified string: {modified_string}")

#Qn7: Remove characters at odd indices
def remove_odd_indices(input_string):
    result = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            result += char
    return result
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    modified_string = remove_odd_indices(input_string)
    print(f"Modified string: {modified_string}")

#Qn10: Reverse a string: Write a Python program to reverse a string
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

#Qn12: Reverse words in a string 
def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
if __name__ == "__main__":
    input_string = input("Enter words: ")
    print(f"String: \"{input_string}\"")
    reversed_words_string = reverse_words(input_string)
    print(f"Reversed words: {reversed_words_string}")

#Qn16: Sum of digits in a string
def sum_of_digits(input_string):
    total_sum = 0
    for char in input_string:
        if char.isdigit():
            total_sum += int(char)
    return total_sum
if __name__ == "__main__":
    input_string = input("Enter word and Digits: ")
    print(f"String: \"{input_string}\"")
    sum_digits = sum_of_digits(input_string)
    print(f"Sum of digits: {sum_digits}")

#Qn18: Count character types
def count_character_types(input_string):
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    numeric_count = 0
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count += 1
    return uppercase_count, lowercase_count, special_count, numeric_count
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    uppercase, lowercase, special, numeric = count_character_types(input_string)
    print(f"Uppercase: {uppercase}")
    print(f"Lowercase: {lowercase}")
    print(f"Special characters: {special}")
    print(f"Numeric values: {numeric}")

#Qn49: Check if strings can be rearranged
def can_be_rearranged(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        return True
    else:
        return False
if __name__ == "__main__":
    string1 = input("Enter first word: ")
    string2 = input("Enter second word: ")
    print(f"String 1: \"{string1}\"")
    print(f"String 2: \"{string2}\"")  
    rearranged = can_be_rearranged(string1, string2)
    print(f"Rearranged: {rearranged}")

#Qn47: Remove adjacent duplicates
def remove_adjacent_duplicates(input_string):
    result = []
    for char in input_string:
        if result and result[-1] == char:
            continue
        else:
            result.append(char)
    return ''.join(result)
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    modified_string = remove_adjacent_duplicates(input_string)
    print(f"Modified string: \"{modified_string}\"")

#Qn48: Length of longest substring without repeating characters
def longest_substring_length(input_string):
    max_length = 0
    left = 0
    seen = set()
    for right, char in enumerate(input_string):
        while char in seen:
            seen.remove(input_string[left])
            left += 1
        seen.add(char)
        max_length = max(max_length, right - left + 1)
    return max_length
if __name__ == "__main__":
    input_string = input("Enter word: ")
    print(f"String: \"{input_string}\"")
    longest_length = longest_substring_length(input_string)
    print(f"Length of longest substring: {longest_length}")

