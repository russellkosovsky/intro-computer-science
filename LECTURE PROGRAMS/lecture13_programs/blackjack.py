#Simulate dealer in blackjack

from random import *

def printIntro():
    print ("Nice intro goes here.")

def simulateGames(n):
    #run n simulations
    #we need more code here!

    return 0 #dummy return value as a placeholder for now (to allow testing)

def printSummary(nBusted, nGames):
    print("Readable summary about", nBusted, "out of", nGames, "goes here.")


#add dealerBusts() function here!
#this function will simulate if a dealerbust occurs or not
#randrange() is useful to simulate a card pic from a deck

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
