# https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

def cowsAndBulls():
    import random

    print("Welcome to the Cows and Bulls game!")
    print("-----------------------------------")
    print("Instructions:")
    print("A 4-digit has been randomly generated. Try to guess it!")
    print("For each number correctly guessed in the correct place you will receive a cow.")
    print("For each number correctly guessed but in the incorrect place you will receive a bull.")
    print("-----------------------------------")
    
    
    
    numToGuess = str(random.randint(1000,9999))

    while True:
        userNum = 0
        cows = 0
        bulls = 0 

        while len(str(userNum)) != 4:
            try:
                userNum = int(input("Input a 4-digit number: "))
                if (len(str(userNum)) != 4):
                    print("This is not a valid number. Try again.")
            except (TypeError, ValueError):
                print("This is not a valid number. Try again.")
        
        userNum = str(userNum)

        # print(numToGuess) # DEBUG
        print(userNum) # DEBUG

        for num in userNum:
            for guessNum in numToGuess:
                if (num == guessNum):
                    bulls += 1

        for i in range(0, 4):        
            if (userNum[i] == numToGuess[i]):
                bulls -= 1
                cows += 1
        
        userNum = 0
        print("Cows:", cows, "Bulls:", bulls)
        print("-----------------------------------")

        if (cows == 4):
            print("Congratulations! You correctly guessed the number!")
            input("Press enter to quit...")
            break


if __name__ == '__main__':
    cowsAndBulls()