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
    tries = 0

    while True:
        tries += 1
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
        # print(userNum) # DEBUG

        numToGuessCopy = list(numToGuess).copy()
        userNumCopy = list(userNum).copy()
        
        # print(numToGuessCopy) # DEBUG

        # print("Starting first loop (cows)") # DEBUG
        for i in range(0, 4):
            if (numToGuess[i] == userNum[i]):
                cows += 1
                numToGuessCopy.remove(userNum[i])
                userNumCopy.remove(userNum[i])
                # print("Removed from numToGuessCopy:", userNum[i]) # DEBUG
                # print("Current state of numToGuessCopy:", numToGuessCopy) # DEBUG
        
        # print("Starting second loop (bulls)") # DEBUG
        for item in userNumCopy:
            if (item in numToGuessCopy):
                bulls += 1
                numToGuessCopy.remove(item)
                # print ("Removed from numToGuessCopy:", item) # DEBUG
                # print("Current state of numToGuessCopy:", numToGuessCopy) # DEBUG
        
        userNum = 0
        print("Cows:", cows, "Bulls:", bulls)
        print("-----------------------------------")

        if (cows == 4 and tries == 1):
            print("************************")
            print("HOLY S#$T! You did it on the first try! God damn it man, go buy a lottery ticket or something")
            print("************************")
            print("I'm really impressed. How the hell did you do it?")
            print("Anyway... congratulations. You guessed it right away. You can uninstall this game now.")
            input("Press enter to quit...")
            break

        if (cows == 4):
            print("Congratulations! You correctly guessed the number!")
            print("It took you", tries, "tries! Try to guess the next number even faster!")
            input("Press enter to quit...")
            break


if __name__ == '__main__':
    cowsAndBulls()