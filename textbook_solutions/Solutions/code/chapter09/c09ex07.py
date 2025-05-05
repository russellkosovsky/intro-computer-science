# c09ex07.py
#   Simulation of game of craps.

from random import randrange

def main():
    print("This program estimates the probability of winning at craps.")
    n = int(input("How many games should I simulate? "))
    wins = simNGames(n)
    print("\nThe player wins", wins, "games.")
    print("The estimated probabillity of a win is {0:0.2%}".format(wins/n))


def simNGames(n):
    wins = 0
    for i in range(n):
        if winCraps():
            wins = wins + 1
    return wins

def winCraps():
    roll = rollDice()
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)

def rollForPoint(toMake):
    roll = rollDice()
    while roll != 7 and roll != toMake:
        roll = rollDice()
    return roll == toMake


def rollDice():
    return randrange(1,7) + randrange(1,7)


if __name__ == '__main__':
    main()
