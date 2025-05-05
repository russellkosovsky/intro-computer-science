#Simulate dealer in blackjack
from random import *

def printIntro():
    print ("Nice intro goes here.")

def simulateGames(n):
    #run n simulations
    totalBusted = 0
    for i in range(n):
        if dealerBusts():
            totalBusted = totalBusted + 1

    
    return totalBusted #dummy return value as a placeholder for now (to allow testing)

def printSummary(nBusted, nGames):
    print("Readable summary about", nBusted, "out of", nGames, "goes here.")
    print("Dealer bust probability is " + str( round(float(nBusted)/nGames*100, 3) ) + "%")


def dealerBusts():

    #total in dealer's hand (accumulator)
    total = 0

    #run until the softstop, 17
    while total < 17:
        hasAce = False
        card = randrange(1, 14)
        if card == 1:
            card = 11
            hasAce = True
        elif card > 10:
            card = 10

        total = total + card

        if total > 21 and hasAce:
            total = total - 10
            hasAce = False
            
    if total > 21:
        return True
    else:
        return False


def main():
    #print intro
    printIntro()
    
    #ask user for input
    totalGames = eval(input("How many simulations of the blackjack dealer shall I run?"))
    
    #simulate the blackjack dealer totalGames times 
    #and record how many times the dealer busts
    numBusted = simulateGames(totalGames)
    
    #output summary of simulation results
    printSummary(numBusted, totalGames)
                                                       
    
main()
