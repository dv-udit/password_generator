import random
import csv
import os

# Saving the required data for making the password in lists
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_caps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']
upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
             'U', 'V', 'W', 'X', 'Y', 'Z']

combined_chars = numerals + lower_caps + upper_chars
module_dir = os.path.dirname(__file__)

# print("module_dir>>>>>>>" , module_dir)

def read_csv_file(file_name):
    """
    Read a CSV file and return its contents as a list.

    Args:
        file_name (str): The name of the CSV file to read.

    Returns:
        list: A list containing the values read from the CSV file.
    """
    file_path = os.path.join(module_dir,"data",file_name)
    # print("file_path>>>>>>",file_path)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        return [row[0] for row in csv_reader]

name_list = read_csv_file('Names.csv')
place_list = read_csv_file('Places.csv')

def custom_choice(chars):
    """
    Choose a random character from the given character set.

    Args:
        chars (list): A list containing characters to choose from.

    Returns:
        str: A random character from the given character set.
    """
    return random.choice(chars)

def make_random():
    """
    Generate a random password that is not present in the name or place list.

    Returns:
        str: A randomly generated password.
    """
    pass_length = random.randint(6, 10)
    password = [custom_choice(combined_chars) for _ in range(pass_length)]
    password.insert(0, random.choice(numerals))  # Include one numeric value
    random.shuffle(password)
    pswd = "".join(password)
    return pswd if password_checker(pswd) else make_random()

def password_checker(created_pass):
    """
    Check if the generated password is not present in the name or place list.

    Args:
        created_pass (str): The password to be checked.

    Returns:
        bool: True if the password is not in the name or place list, False otherwise.
    """
    return created_pass not in (name_list + place_list)

def generate_pass():
    """
    Generate a random password that is not present in the name or place list.

    Returns:
        str: A randomly generated password.
    """
    return make_random()

# Example usage:
# final_pass = generate_pass()
# print(len(final_pass))
# print(final_pass)


    