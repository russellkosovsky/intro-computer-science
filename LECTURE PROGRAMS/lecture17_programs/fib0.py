#lecture 18 exercise: Fibonacci numbers
#Fib numbers are 1, 1, 2, 3, 5, 8, 13, …
#fib(n) is sum of two previous Fibonacci numbers

#from our previous example: iterative version
def Fib0(n):

    #fib(1), fib(2) is 1
    if n < 3:
        return 1

    #variables to keep track of three continuous fib numbers
    numA, numB, numC = 1, 1, 0

    #we already have first two numbers. so start interaction index from 2
    for i in range(2, n):
        numC = numA + numB
        numA = numB
        numB = numC

    return numC
    


#recursive verison of fibonacci function
def Fib(n):
    #sum of two previous nums: Fib(n-2) & Fib(n-1)

    ###base case: n is 1 or 2


    ###recursive case


    ####dummy: comment out this after completion of your code
    return 0


print(Fib0(7))
