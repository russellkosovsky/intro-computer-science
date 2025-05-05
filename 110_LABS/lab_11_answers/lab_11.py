
#1)
def getInput():
    n = int(input("Enter a number greater than 0: "))
    if n > 0:
        print("Thank you.")
    else:
        getInput()


#2)
def countdown(n):
    while n >= 0:
        print(n)
        n = n - 1
    print("End of program.")

#3e)
def byrows():
    twodlist = []
    for row in range(4):
        twodlist.append([])
        for col in range(4):
            twodlist[row].append(row)
    print(twodlist)

#3f)
def bycols():
    twodlist = []
    for row in range(4):
        twodlist.append([])
        for col in range(4):
            twodlist[row].append(col)
    print(twodlist)

#3g)
def multiples():
    #creates a 4x4 array of entries, each with value row*col
    twodlist = []
    for row in range(4):
        twodlist.append([])
        for col in range(4):
            twodlist[row].append(row*col)
    print(twodlist)
    
#3h)
def original():
    TwoDnumList = []
    for row in range(4):
        TwoDnumList.append([])
        for col in range(4):
            TwoDnumList[row].append((row * 4) + col + 1)
            print("row ", row)
            print("col ", col)
            print()
    print("result:", TwoDnumList)

# POSSIBLE Bonus A solution:
def monty():
    from random import randrange
    
    #Case 1: Player doesn't change their pick
    #Just count how many times player wins regardless of opened door/goat
    count = 0
    for i in range(1000): #Simulate 1000 games
        doors = [0,0,0] #Start with all goats (zeros)
        doors[randrange(0,3)] = 1 # 1 is a car
        player_pick = randrange(0,3)
        if doors[player_pick] == 1: #Check if player won
            count+=1
    print("Case 1: Player won {0:2%} of the games.".format(count/1000))

    #Case 2: Player changes their pick
    count = 0
    for i in range(1000): #Simulate 1000 games
        doors = [0,0,0] #Start with all goats (zeros)
        doors[randrange(0,3)] = 1 # 1 is a car
        player_pick = randrange(0,3)
        #Reveal one door with goat
        if doors[0]==0 and player_pick != 0:
            revealed = 0
        elif doors[1]==0 and player_pick != 1:
            revealed = 1
        else:
            revealed = 2

        #Player changes their pick to remaining door (other than revealed)
        if revealed != 0 and player_pick!=0:
            new_pick = 0
        elif revealed != 1 and player_pick!=1:
            new_pick = 1
        else:
            new_pick = 2

        #Check if player won
        if doors[new_pick] == 1:
            count+=1

    print("Case 2: Player won {0:2%} of the games.".format(count/1000))



def main():
    #1
    print("1:")
    getInput()
    print("------------------------------------")
    print()

    #2
    print("2:")
    countdown(10)
    print("------------------------------------")
    print()

    #3a)
    TwoDnumList = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

    #3b)
    print("3b:")
    print(TwoDnumList[2][3])
    print("------------------------------------")
    print()

    #3c)
    print("3c:")
    for row in range(len(TwoDnumList)):
        for col in range(len(TwoDnumList[row])):
            print(TwoDnumList[row][col])
    print("------------------------------------")
    print()

    #3d)
    print("3d:")
    for row in range(len(TwoDnumList)):
        for col in range(len(TwoDnumList[row])):
            print(TwoDnumList[row][col], end="\t")
        print()
    print("------------------------------------")
    print()

    #3e)
    print("3e:")
    byrows()
    print("------------------------------------")
    print()

    #3f)
    print("3f:")
    bycols()
    print("------------------------------------")
    print()

    #3g)
    print("3g:")
    multiples()
    print("------------------------------------")
    print()

    #3h)
    print("3h:")
    original()
    print("------------------------------------")
    print()

    #Bonus A
    print("Bonus A")
    monty()

main()
    


    
