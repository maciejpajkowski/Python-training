# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [123, 32, 5, 10, 15, 20, 25, 555, 61353, 321, 2]

def firstLast(list):
    print("First list element:",list[0], "Last list element:", list[len(list)-1])

firstLast(a)