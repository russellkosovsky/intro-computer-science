# c08ex04.py
#    Syracuse sequence
#    Note: Let me know if you find a starting value that doesn't go to 1 :-).

def main():
    print("This program outputs a Syracuse sequence\n")
    n = int(input("Enter the initial value (an int >= 1): "))
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    print(1)

if __name__ == '__main__':
    main()
