# c11ex05.py
# various list algorithms


def count(myList, x):
    ans = 0
    for item in myList:
        if item == x:
            ans = ans + 1
    return ans

def isin(myList, x):
    for item in myList:
        if item == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
    # If not found, raise a value error
    #   an alternative would be to return -1
    raise ValueError("x not in list")

def reverse(lst):
    for i in range(len(lst)/2):
        j = -(i+1)
        lst[i], lst[j] = lst[j], lst[i]


def sort(lst):
    # selection sort. See Chapter 13 for other examples.
    for i in range(len(lst)-1):
        # find min of remaining items
        minpos = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[minpos]:
                minpos = j
        # swap min to front of remaining
        lst[i], lst[minpos] = lst[minpos], lst[i]



