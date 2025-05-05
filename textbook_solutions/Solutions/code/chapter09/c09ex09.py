# c09ex08.py
#    Simulation to Blackjack dealer to estimate bust probability.

from random import randrange

def main():
    print("Simulation of a Blackjack dealer.\n")
    n = int(input("How many trials for each start value? "))
    print("\nStart  Prob of Bust")
    print("-------------------")
    for start in range(1,11):
        busts = simulateHands(n, start)
        print("{0:5}  {1:7.2f}".format(start, busts/n))

def simulateHands(n, start):                              
    busts = 0
    for i in range(n):
        points = dealHand(start)
        if points > 21:
            busts = busts + 1
    return busts

def dealHand(start):
    total = start
    haveAce = (start == 1)
    while total < 17:
        card = randrange(1,14)
        if card == 1: 
        	haveAce = True
        total = total + BJValue(card)
        if haveAce:
            total = adjustForAce(total)
    return total
    
def BJValue(card):
    if card > 10:
        return 10
    else:
        return card

def adjustForAce(total):
    if 16 < total + 10 < 22:
        return total + 10
    else:
        return total

if __name__ == '__main__':
    main()
