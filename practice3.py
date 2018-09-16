# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

# def lessThanFive(list):
#     num = int(input('Please enter a number... '))
#     newList = []
#     for listitem in list:
#         if (listitem < num):
#             newList.append(listitem)
#     return newList

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result = lessThanFive(a)
# print(result)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([item for item in a if item < 5])

input("Press enter to quit...")