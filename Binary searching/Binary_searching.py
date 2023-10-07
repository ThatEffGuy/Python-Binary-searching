import time
import random
from random import randint

def GenerateRandomNumbers():
    random_list = []
    howmany = int(input("How many numbers do you want to have in the list? "))
    for i in range(0, howmany):
        random_list.append(random.randint(0, 5000))
    return random_list

def binarySearch(myItem, myList):
    myList.sort()
    print(myList)
    theTime = str(time.perf_counter())
    print("\nThe time after sorting the list ..... ", theTime)
    found = False 
    bottom = 0
    top = len(myList)- 1
    while bottom <= top and not found:
        middle = (bottom+top)//2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found

returnedList = GenerateRandomNumbers()
print(returnedList)
userNumber = int(input("\nWhat number do you want to find: "))

theTime = str(time.perf_counter())
print("\nThe time before Binary searching ..... ", theTime)

isFound = binarySearch(userNumber, returnedList)

theTime = str(time.perf_counter())
print("\nThe time after Binary searching ..... ", theTime)

if isFound:
    print("\nThe number you typed is in the list...")
else:
    print("\nThe number you typed is not in the list...")