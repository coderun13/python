import re

email_condition = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def validate_with_regex(email):
    if re.search(email_condition, email):
        print(f"'{email}' is a valid email format.")
    else:
        print(f"'{email}' is NOT a valid format.")

if __name__ == "__main__":
    user_email = input("Enter email to check: ").lower()
    validate_with_regex(user_email)