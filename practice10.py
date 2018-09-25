# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# a = random.sample(range(1,60), random.randint(1,30))
# b = random.sample(range(1,40), random.randint(1,20))

# a.sort()
# b.sort()

a = [1,1,1,3,5,7,11,16,16,17,23,23,23,23,66,123]
b = [1,1,5,7,11,11,16,17,23,23,23,24,66,123,1223]

print(a)
print(b)

list1 = [item for item in a if item in b]
newList = []
for item in list1:
    if item not in newList:
        newList.append(item)
print("\nThis is the new list:")
print("---------------------")
print(newList)

input("Press enter to quit...")