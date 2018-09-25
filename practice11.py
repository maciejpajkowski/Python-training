# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def get_number():
    return int(input("Please enter a number: "))

number = get_number()
theRange = range(1, (number + 1))
print("Divisors for " + str(number) + ":", [item for item in theRange if number % item == 0])
if len([item for item in theRange if number % item == 0]) == 2:
    print("This is a primal number!")
else:
    print("This is not a primal number...")