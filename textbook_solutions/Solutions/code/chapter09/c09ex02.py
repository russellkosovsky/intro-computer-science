# c09ex02.py
#    Racquetball simulation with shutouts

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, shutsA, winsB, shutsB = simNGames(n, probA, probB)
    printSummary(winsA, shutsA, winsB, shutsB)

def printIntro():
    # Prints an introduction to the program
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    # RETURNS probA, probB, number of games to simulate
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players A and B
    # RETURNS number of wins for A, number of wins for B
    winsA = winsB = 0
    shutsA = shutsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
            if scoreB == 0:
                shutsA = shutsA + 1
        else:
            winsB = winsB + 1
            if scoreA == 0:
                shutsB = shutsB + 1
    return winsA, shutsA, winsB, shutsB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a,b):
    # a and b are scores for players in a racquetball game
    # RETURNS true if game is over, false otherwise
    return a == 15 or b == 15 \
           or (a == 7 and b == 0) \
           or (b == 7 and a == 0)

def printSummary(winsA, shutsA, winsB, shutsB):
    # Print a nicely formatted report
    n = winsA + winsB
    print("Summary of", n , "games:")
    print()
    print("          wins (% total)   shutouts (% wins)  ")
    print("--------------------------------------------")
    printLine("A", winsA, shutsA, n)
    printLine("B", winsB, shutsB, n)

def printLine(label, wins, shuts, n):
    template = "Player {0}:  {1:4} ({2:6.1%}) {3:11}  ({4})"
    if wins == 0:        # Avoid division by zero!
        shutStr = "------"
    else:
        shutStr = "{0:6.1%}".format(shuts/wins)
    print(template.format(label, wins, wins/n, shuts, shutStr)) 


if __name__ == "__main__": main()





