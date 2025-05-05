#randrange & random exercise program
#see random number's uniform distribution behavior

## Needs minor modifications
## Double pounds (##) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from random import *

def main():

    #simulation of rolling two dice
    trials = eval(input("How many die rolls should I simulate? "))

    #dice number accumulator
    counters = []
    for i in range(14):
        counters.append(0)
        
    #loop trials times of roll and keep track of result
    for i in range(trials):
        ## here we used randrange to simulate dice
        ## change this to use random() so that we can check random() uniform distribution behavior
        rollvalue = randrange(1, 7) + randrange(1,7)
        
        counters[rollvalue] = counters[rollvalue] + 1
        
    #print out the result (probability in percentile)
    for i in range(2,13):
        percent = float(counters[i]) / trials * 100
        print("probability for", i, ":", round(percent, 2), '%' )

    
main()
