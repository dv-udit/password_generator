from pkgUdit import generatePass

def password_validator(password):
    """
    Validating the password based on the following criteria:
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one numeric value.
    - Has a length between 6 and 12 characters.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if not 6 <= len(password) <= 12:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True

# Example usage:
password = generatePass()  # Replace this with the password you want to validate
print("password>>>>> : " + password)
is_valid = password_validator(password)
print(is_valid)  # Output: True or False
