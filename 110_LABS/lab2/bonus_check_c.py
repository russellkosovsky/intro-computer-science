# file: bonus_check_c.py
# a program that prints out a count-down of the natural numbers starting from 10 and a user-specified value



####### check 5


def main():
    print("This program prints out a count-down of the natural numbers starting from 10")
    for i in range(10,0,-1):
        print(i)
    n = eval(input("What number do you want to cound down from?: "))
    for i in range(n,0,-1):
        print(i)

main()
