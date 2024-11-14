phone_number = "0756188610"
email_db = "mremmaug@gmail.com"
password = "Emma256"

attempts = 0
max_attempts = 3
while attempts < max_attempts:
    email_input = input("Enter Email or Phone number: ")
    password_input = input("Enter your Password: ")
    
    email = email_input == phone_number or email_input == email_db
    Password = password_input == password
    
    if email and Password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Please try again.")
        attempts += 1