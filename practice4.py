# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input('Please enter a number: '))
rangeNum = number + 1
theRange = range(1, rangeNum)
newList = []
for element in theRange:
    if (number % element == 0):
        newList.append(element)
print("This is the list of all the divisors of", number, ":", newList)

input("Press enter to quit...")