#Validate username and password.
import re

def validate_username(username):
    if len(username) < 5 or len(username) > 15:
        return "Invalid username: must be 5-15 characters"
    elif not username.isalnum():
        return "Invalid username: must be alphanumeric"
    else:
        return "Valid username"

def validate_password(password):
    if len(password) < 8:
        return "Invalid password: must be at least 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Invalid password: must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Invalid password: must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Invalid password: must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Invalid password: must contain at least one special character"
    return "Valid password"

# Example usage
username = "User123"
password = "Pass@123"
print(validate_username(username))
print(validate_password(password))