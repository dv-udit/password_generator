import random

numerals = ['0','1','2','3','4','5','6','7','8','9']
lowerCaps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

combinedChars = numerals + lowerCaps + upperChars


def custom_choice(combinedChars):
    idx = random.randint(0, len(combinedChars)-1)
    return combinedChars[idx]

def make_random():
    passLength = random.randint(6, 12)
    password = []
    password.append(random.choice(numerals))  # Include one numeric value
    
    for _ in range(passLength - 1):
        password.append(custom_choice(combinedChars))
    
    random.shuffle(password)
    return password

def generatePass():
    created_pass = make_random()
    return ''.join(created_pass)

# password = generatePass()
# print(password)
# print(len(password))