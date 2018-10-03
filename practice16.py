# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random

def generatePassword():
    basePassword = ''
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z')
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    length = int(input("Please specify how long the password should be: "))

    while length > 0:
        i = random.randint(0, len(letters) - 1)
        basePassword += letters[i]
        length -= 1
    
    password = list(basePassword)

    for letter in range(0, len(password) - 1):
        change = random.randint(0,1)
        randomNum = random.randint(0, len(numbers) - 1)
        upperCase = random.randint(0, 1)

        if change == 1:
            password[letter] = str(numbers[randomNum])
        if upperCase == 1 and password[letter].isdigit() is False:
            password[letter] = password[letter].upper()

    result = "".join(password)
    print(result)
    input("Press enter to quit...")

generatePassword()