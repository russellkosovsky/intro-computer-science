# Recursively find the largest number of a list

def newmax(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], newmax(list[1:]))

def main():
    print("This program finds the largest number in a list of numbers")
    print("enter list of numbers in the python list format. \nEX: [23, 45, 32, 99, 10, 4]")
    myList = eval(input(""))
    print("The largest number is ", newmax(myList))

main()
