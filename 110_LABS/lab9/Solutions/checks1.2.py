from random import *

def main():
    #CHECK 1
    numbers = []
    for i in range(6):
        num = randrange(1,11)
        numbers.append(num)
        
    print(numbers)

    #CHECK 2
    numbers = []
    for i in range(6):
        num = randrange(1,11)
        while num in numbers:
            num = randrange(1,11)
        numbers.append(num)

    print(numbers)

main()
