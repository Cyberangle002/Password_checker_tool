import re

def check_password_strength(password):
    # Check length
    length_error = len(password) < 8
    # Check for uppercase letters
    uppercase_error = not any(char.isupper() for char in password)
    # Check for lowercase letters
    lowercase_error = not any(char.islower() for char in password)
    # Check for digits
    digit_error = not any(char.isdigit() for char in password)
    # Check for special characters
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    # If any criteria fail, the password is weak
    if length_error or uppercase_error or lowercase_error or digit_error or special_char_error:
        print("Weak Password! Consider the following:")
        if length_error:
            print("- Password should be at least 8 characters long.")
        if uppercase_error:
            print("- Include at least one uppercase letter.")
        if lowercase_error:
            print("- Include at least one lowercase letter.")
        if digit_error:
            print("- Include at least one digit.")
        if special_char_error:
            print("- Include at least one special character (!@#$%^&*(), etc.).")
    else:
        print("Strong Password!")
        
# Input from user
user_password = input("Enter a password to check its strength: ")
check_password_strength(user_password)
