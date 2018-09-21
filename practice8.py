# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("Welcome to Rock, Paper and Scissors!")

p1Score = 0
p2Score = 0
while p1Score < 3 and p2Score < 3:

    print("Current scores are - Player 1:", p1Score, ", Player 2:", p2Score)

    player1 = input('P1: Please choose your weapon (rock, paper, scissors)! ...')
    cls()
    player2 = input('P2: Please choose your weapon (rock, paper, scissors)! ...')
    cls()

    if (player1 == "rock" and player2 == "scissors"):
        print("Player 1 wins!")
        p1Score += 1
    elif (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
        p1Score += 1
    elif (player1 == "scissors" and player2 == "paper"):
        print("Player 1 wins!")
        p1Score += 1

    if (player2 == "rock" and player1 == "scissors"):
        print("Player 2 wins!")
        p2Score += 1
    elif (player2 == "paper" and player1 == "rock"):
        print("Player 2 wins!")
        p2Score += 1
    elif (player2 == "scissors" and player1 == "paper"):
        print("Player 2 wins!")
        p2Score += 1

    if (player1 == player2):
        print("Draw! Better luck next time.")

if (p1Score == 3):
    print("Player 1 is victorious!")
    input("Press enter to quit...")
elif (p2Score == 3):
    print("Player 2 is victorious!")
    input("Press enter to quit...")

