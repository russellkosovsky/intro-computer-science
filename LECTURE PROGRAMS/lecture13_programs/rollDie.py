# randrange exercise program
# see random number's uniform distribution behavior

from random import *

def main():

    # first let's try a few times of rolling a die
    print('\n\n== rolling a die six times =========')
    for i in range(6):
        print(randrange(1, 7), end=' ')

    # test seed
    print('\n\n== seed with 0 =============')
    seed(0)
    for i in range(6):
        print(randrange(1, 7), end=' ')
    # let's roll a die many times and compute probability

    print('\n\n== random uniformity test =======')
    # a list to accumulate die numbers. 7 int for indexing convinience
    counters = []
    for i in range(7):
        counters.append(0)

    trials = eval(input("how many rolls do you want to simulate? "))

    for i in range(trials):

        val = randrange(1,7)

        counters[val] = counters[val] + 1

    for i in range(1,7):

        probability = counters[i] / trials

        print("probability of rolling number", str(i), ":", str(probability))

    # comment back in below line to take a user input
    # trials = eval(input("How many die rolls should I simulate? "))

    # loop trials times of roll and keep track of result
    # remember you will need to use an accumulator concept here

    # print out the result (probability)
    # format the output nicely. i.e. A roll of 1: 20.0%
        
main()
