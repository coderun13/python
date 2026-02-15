from email_validator import validate_email, EmailNotValidError

def check_email(email):
    try:
        email_info = validate_email(email, check_deliverability=True)
        normalized_email = email_info.normalized
        
        print(f"The email '{normalized_email}' is valid!")
        print(f"Domain: {email_info.domain}")
        
    except EmailNotValidError as e:
        print(f"Invalid email: {str(e)}")

if __name__ == "__main__":
    user_input = input("Enter an email to validate: ")
    check_email(user_input)