# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
print("Welcome to the number guessing game!")
print("------------------------------------")

game = True
tries = 0

while game:
    if tries is 0:
      num = random.randint(1,9)
    print("Guess the number!")

    userNum = input("Pick a number between 1 and 9 OR type 'exit' to quit: ")
    tries += 1
    clear()

    if userNum == 'exit':
        break

    if (int(userNum) < num):
        print("The number you are looking for is higher.")
    elif (int(userNum) > num):
        print("The number you are looking for is smaller.")
    else:
        print("Congratulations! The number is", num, end=". \n")
        if (tries == 1):
            print("You figured it out on the first try! Well done!")
            tries = 0
            print("Let's play again! \n")
        else:
            print("It took you", tries, "tries. \n")
            tries = 0
            print("Let's play again!")
            print("-----------------")
