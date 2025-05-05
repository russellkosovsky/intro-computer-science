# c13ex07.py
# An empirical comparision of the reccursive
# and the iterative binomial coefficient calculations

import time

def recBinom(n,k):
    # PRE:  n, k >= 1    
    # first base case  n < k
    if n < k:
        return 0
    elif k == 1:
        return n
    else:
        return recBinom(n-1,k)+recBinom(n-1,k-1)

def iterBinom(n,k):
    # PRE: n, k >= 1

    answer = 1
    #use symmetry to minizmize loop count
    k = min(k, n-k)
    for i in range(k):
        answer = answer*(n-i)//(i+1)
    return answer

def main():
    print()
    print("Let's compare two algorithms for C(n,k)")
    print()

    n = int(input("What is n? ( n >= 1 please) "))
    k = int(input("What is k? ( k >= 1 please) "))
    print()
    print("Please be patient the recursive algorithm can take time")
    print()

    # calculate the number of repetitions based on n
    # repeat the calculation so that the clock time isn't 
    # zero for both calculations
    if n < 10:
        repeats = 200
    elif n < 15:
        repeats = 20
    elif n <=20 :
        repeats = 10
    else:
        repeats = 2
        
    start = time.clock()
    for i in range(repeats):
        rb = recBinom(n,k)
    end = time.clock()
    recTime = end-start

    start = time.clock()
    for i in range(repeats):
        ib = iterBinom(n,k)
    end = time.clock()
    iterTime = end-start
 
    print("C({0},{1}) is {2}".format(n,k,rb))
    print("computed recursively",repeats,"times took",recTime,"seconds")
    print()
    print("C({0},{1}) is {2}".format(n,k,ib))
    print("computed iteratively",repeats,"times took",iterTime,"seconds")
    print()
    
main()
                            
