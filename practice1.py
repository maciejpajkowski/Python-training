# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime

now = datetime.datetime.now()

print('Hi! Please enter your name: ')
name = input()
print('Now enter your age:')
age = int(input())
print('Also, please enter one random (preferably small) number...')
randomNum = int(input())
year = now.year
print(year)
yearOfHundred = year - age + 100
while randomNum:
    print('It turns out you\'ll turn 100 in ' + str(yearOfHundred) + '!')
    randomNum -= 1

input("Press enter to quit...")

