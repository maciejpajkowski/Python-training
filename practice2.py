# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = int(input('Please input a number... '))

if (number % 2 == 0):
    if (number % 4 == 0):
        print("This number is not only even, but is a multiple of 4!")
    else:
        print("This is an even number.")
else:
    print("This is an odd number.")

input('Press any key to continue!')

num = int(input("Now, please enter any number... "))
check = int(input("Thanks! Now please enter another number... "))

if (num % check == 0):
    print("The first number,", num,", is divided evenly by", check)
else:
    print("Number", num, "is not divided evenly by", check)

input("Press enter to quit...")