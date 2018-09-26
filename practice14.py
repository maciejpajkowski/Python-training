# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

# Two different functions which do the exact same thing:

a = [3, 3, 5, 5, 7, 8, 11, 11, 11, 32]

def removeDupesSet(givenList):
    print(list(set(givenList)))
    return list(set(givenList))

removeDupesSet(a)
print("-------------")

def removeDupesLoop(list):
    newList = []
    for item in list:
      if (item not in newList):
          newList.append(item)
    print(newList)
    return newList

removeDupesLoop(a)