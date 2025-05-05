# c11ex16.py
#    Implementation of StatSet, an object that manages a collection
#    of numbers and calculates some simple statistics

class StatSet:

    def __init__(self):
        # all the data is stored in a list
        self.data = []
        # running sum and count kept as each number is added
        self.sum = 0.0
        self.n = 0
        
    def addNumber(self, x):
        # adds x to the data in this StatSet
        self.data.append(x)
        self.n = self.n + 1
        self.sum = self.sum + x

    def count(self):
        # Returns the number of values in the set
        return self.n

    def min(self):
        # Returns the smallest value
        return min(self.data)

    def max(self):
        # Returns the largest value
        return max(self.data)

    def mean(self):
        # Returns the mean
        return self.sum / self.n

    def stdDev(self):
        # Returns the standard deviation
        n = self.n
        xbar = self.sum / n
        sumDevSq = 0.0
        for x in self.data:
            sumDevSq = (x-xbar)**2
        return (sumDevSq / (self.n-1)) ** 0.5
    
    def median(self):
        # Returns the median value
        data = self.data
        n = self.n
        data.sort()
        mid = n / 2
        if n % 2 == 0:
            return (data[mid]+data[mid-1])/2.0
        else:
            return data[mid]


def test():
    print("This program calculates simple statistics.\n")
    s = StatSet()
    while True:
        xStr = input("Enter a number (blank to quit): ")
        if xStr == "": break  # loop exit
        s.addNumber(float(xStr))
    print("count", s.count())
    print("mean", s.mean())
    print("median", s.median())
    print("standard deviation", s.stdDev())
    print("min", s.min())
    print("max", s.max())

if __name__ == "__main__":
    test()
    
    
