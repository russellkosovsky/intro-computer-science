# file: bonus_check_d.py



##### CHECK 6


def main():
    total = 0
    print("This program adds up all numbers from 1 to 1000")
    for i in range(1,1001):
        total= total + i

    print(total)
        
    total = 0
    n = eval(input("What number do you to add up to?: "))
    for i in range(1,n+1):
        total= total + i

    print(total)


main()
