# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

print("Welcome! This program will tell show you the Fibonacci sequence to a chosen number.")
number = int(input("First, enter your number: "))

def fibonacci(number):
    result = []
    usedRange = list(range(1,(number + 1)))
    for num in usedRange:
        if len(result) < 2:
            result.append(1)
        else:
            result.append(result[num-3] + result[num-2])
    print(result)


fibonacci(number)
input("Press enter to quit...")