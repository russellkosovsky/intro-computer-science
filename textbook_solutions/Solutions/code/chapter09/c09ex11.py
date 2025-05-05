# c09ex11.py
#     Probability of rolling 5 of a kind

from random import randrange

def main():
    print("This program estimates the probability of rolling")
    print("five of a kind on a single roll of 5 dice.\n")

    n = int(input("How many rolls should I simulate? "))
    hits = 0
    for i in range(n):
        if equalRolls(5):
            hits = hits + 1
    print("Estimated prob =", float(hits)/n)


def equalRolls(count):
    # count is number of dice to be rolled (must be >1)
    # returns True if all values turn out the same, False o/w
    first = randrange(1,7)
    for i in range(count-1):
        roll = randrange(1,7)
        if roll != first:
            return False
    # All rolls were equal to the first
    return True

if __name__ == '__main__':
    main()


