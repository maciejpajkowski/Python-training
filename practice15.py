# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

print("This program will reverse the entered sentence.")

def inputString():
    return input("Please insert a short sentence: ")

def reverseString():
    string = inputString()
    newString = string.split()
    newString.reverse()
    newerString = " ".join(newString)
    print(newerString)

reverseString()

input("Press enter to quit...")