

# 1. Write a recursive version of the following iterative program.

def getInputI():
    
    n = eval(input("Enter a number greater than 0: "))
    while n <= 0:
        n = eval(input("Enter a number greater than 0: "))
    print("Thank you.")



def getInputR():
    
    n = eval(input("Enter a number greater than 0: "))
    if n <= 0:
        return getInput()
    else:
        print("Thank you.")
        return n

# 2. Write an iterative (using a while or for loop) version of this recursive “countdown” program from class.

def countdown(n):
    print(n)
    if n == 0:
        print("End of program.")
    else:
        countdown(n-1)

def countdownR(n):
    while n >= 0:
        print(n)
        if n == 0:
            print("End of program.")
        n -= 1

###### 3 ######

##A##
twoDnumList = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

##B##
def b():
    print(twoDnumList[2][3])
#b()
    
##E##
def e():
    twoDListByRows = []
    for i in range(4):
        row = [i] * 4
        twoDListByRows.append(row)
    print(twoDListByRows)
#e()

##F##
def f():
    twoDListByCols = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(j) 
        twoDListByCols.append(row)
    print(twoDListByCols)
#f()

##G##
def g():
    print("g")
    multiples = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(i * j)
        multiples.append(row)
    print(multiples)
#g()

##H##
def h():
    twoDnumList = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(i * 4 + j + 1)
        twoDnumList.append(row)
    print(twoDnumList)
#h()

##I##
def i():
    
    n = int(input("Enter the size of the nxn matrix: "))

    twoDnumList_nxn = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * n + j + 1)
        twoDnumList_nxn.append(row)

    print(twoDnumList_nxn)
    
#i()

getInputI()
getInputR()

countdown(n)
countdownR(n)

b()




