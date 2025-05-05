# c08ex01.py
#    Nth fibonacci number

def main():
    print("This program calculates the nth Fibonacci value.\n")

    n = int(input("Enter the value of n: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr

    print("The nth Fibonacci number is", curr)

if __name__ == '__main__':
    main()
