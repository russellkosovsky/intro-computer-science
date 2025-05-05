#Simulating the dealer in blackjack

## Needs minor modifications
## Double pounds (##) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from random import *

def main():
    
    #print intro
    printIntro()

    #input num games to be simulated
    totalGames = eval(input("How many dealer hands do you want to simulate for each possible starting card?")) ##

    print ("The percentage of busted games for each possible starting card is as follows." )##

    ## for each possible starting card
    for startCard in range(1,14): ## this loop was not here before
        #simulate the blackjack dealer totalGames times and record how many times the dealer busted
        numBusted = simulateGames(totalGames, startCard) ## we are sending TWO arguments here now!
        #output summary of simulation results
        #print("startcard", startCard)
        #print("numbusted", numBusted)
        #print("totalgames", totalGames)
        print ( "For starting card " + str(startCard) + " bust percentage is "  + str(float(numBusted)/totalGames*100))

def printIntro():
    print ("This is a program that computes how often blackjack dealers bust.")
    print ("You input the number of times you want the simulation to be run.")
    print ("I output the percentage of times the dealer busts, for each initial dealer card. ") ##
    print ()
    
## Simulates the blackjack dealer n times for each possible starting card
## (Fix this function so that it has two parameters, as the call from the main function requires.)
def simulateGames(n,startcard):
    totalBustedGames = 0
    #run n simulations:
    for i in range(n):
        ## Simulate game with the given initial showing card and see if dealer busts
        if dealerBusts(startcard): ## <-- this function call now needs an argument... what should you pass it?
            #add one to the total number of busted games
            totalBustedGames += 1

    #return total number of dealer busts 
    return totalBustedGames

## Deals out one dealer-hand that starts with the given initialCard
# and returns True if dealer busts, False otherwise
def dealerBusts(initialCard): ## The initialcard parameter has been added

    hasAce = False
    total = 0
    ## This is no longer necessarily the default initial value of hasAce,
    ## because the initialcard might be an Ace!
    if initialCard == 1:
        hasAce = True
    ## also think about what to do if the initial card is face card (J, Q, K) or Ace 
    elif initialCard > 10:
        total = 10
    else:
        total = initialCard

    #keep dealing cards until total reaches 17
    while total < 17:
        #new card dealt: generate random number between 1 and 14 to simulate dealing a card
        card = randrange(1,14)

        #adjust value of card if it's an ace or a face card
        if card >= 11:
            card = 10
        elif card == 1:
            card = 11
            hasAce = True
            
        #add value of card to total
        total = total + card

        #if has an Ace card and total is greater than 21
        if hasAce and total > 21:
            #then decrease value of the Ace to 1
            total -= 10
            hasAce = False

    #check if dealer busted
    if total > 21: 
        return True
    else:
        return False

main()
