# c13ex01.py
# a program that traces the fib function

# The answer to the question is that fib(10) calls
# fib(3) 21 times

def fib(n):
    print("Computing fib(%d)"%n)
    if n<3:
        return_value = 1
    else:
        return_value = fib(n-1)+fib(n-2)

    print("Leaving fib({0}) returning {1}".format(n,return_value))
    return return_value

def main():
    print()
    print("Let's trace the function that computes Fibonacci numbers")
    print()
    
    n = int(input("Computing the n-th Fibonacci number. Enter n. "))
    f = fib(n)
    
    print()
    print("Fib({0}) is {1}".format(n,f))
    print()

main()
