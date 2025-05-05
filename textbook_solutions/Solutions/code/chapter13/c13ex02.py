# c13ex02.py
# Counting the recursive calls to fib using
# a FibCounter class.

class FibCounter:
    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count

    def fib(self,n):
        self.count = self.count + 1
        if n <3:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
    def resetCount(self):
        self.count = 0


def main():
    print()
    print("Let's count the recursive calls for Fibonacci numbers!")
    print()

    FC = FibCounter()

    n = int(input("Computing the n-th Fibonacci number. Enter n. "))

    answer = FC.fib(n)
    count = FC.getCount()

    print()
    print("Fib({0}) is {1} and used {2} function calls.".format(n,answer,count))
    print()

main()
