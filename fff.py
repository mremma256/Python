import re

def is_valid_email(email):
    # Basic regex for validating an email address
    pattern = r'[a-z0-9]+@[gmailyahooicloud]+.[com]'
    return re.match(pattern, email)

def is_valid_phone(phone):
    # Check if the phone number contains only digits and has a reasonable length (e.g., 10-15 digits)
    return phone.isdigit() and len(phone) == 10

def is_valid_password(password):
    pattern = r'[a-zA-Z0-9]+[/;,._%+-]'
    return re.match(pattern, password) and len(password) >=8

def get_user_input():
    email = input("Enter your email address: ")
    while not is_valid_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email address: ")

    phone = input("Enter your phone number: ")
    while not is_valid_phone(phone):
        print("Invalid phone number!")
        phone = input("Enter your phone number: ")

    password = input("Enter your password: ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter your password: ")

    print("Successfully logged in!")

get_user_input()
