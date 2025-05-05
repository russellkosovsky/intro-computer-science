# Recursively find the largest number of a list

def MAX(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], MAX(list[1:]))

def main():
    print("Let's find the maximum element of a list of numbers")
    print("enter a list of numbers in the python list format. \nEX: [23, 45, 32, 99, 10, 4]")
    myList = eval(input(""))
    print("The largest element is ", MAX(myList))

main()
