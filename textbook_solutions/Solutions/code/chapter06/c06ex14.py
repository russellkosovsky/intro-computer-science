# c06ex14.py
#    sum of squares from file

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def sumList(nums):
    total = 0
    for n in nums:
        total = total + n
    return total

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2

def main():
    print("Program to find sum of squares from numbers in a file")
    fname = input("Enter filename: ")
    data = open(fname,'r').readlines()
    toNumbers(data)
    squareEach(data)
    print("Sum of squares:", sumList(data))

main()
