"""
Custom Password Validator Script

This script generates a random password using the `generatePass` function from the `pkgUdit` package
and then validates it based on the following criteria:
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one numeric value.
    - Has a length between 6 and 12 characters.
    - Does not match any data in 'Names.csv' and 'Places.csv' files.

This script depends on the 'pkgUdit' package for generating passwords and requires 'Names.csv' and 'Places.csv'
files in the same directory to check if the password matches any data in those files.

"""

from pkgUdit import generate_pass
import os
import csv

module_dir = os.path.dirname(__file__)

def read_csv_file(file_name):
    file_path = os.path.join(module_dir, file_name)
    with open(file_path) as csv_file:
        return [row[0] for row in csv.reader(csv_file)]

name_list = read_csv_file("Names.csv")
place_list = read_csv_file("Places.csv")

def password_validator(password):
    """
    Validate the password based on the following criteria:
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

    return not password in (name_list + place_list)

# for single usage

# Example usage:
# password = generatePass()
# print("Generated Password: " + password)
# is_valid = password_validator(password)
# print("Password Valid: ", is_valid)  # Output: True or False



# for checking mulitple password

# for i in range(1000):
#     password = generate_pass()
#     print("Generated Password: " + password)
#     is_valid = password_validator(password)
#     print("Password Valid: ", is_valid)  # Output: True or False
