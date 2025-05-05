# c11ex06.py
#    Algorithm to shuffle a list (simulates random.shuffle)

from random import randrange

def shuffle(lst):
    for i in range(len(lst)):
        j = randrange(i,len(lst))
        lst[i], lst[j] = lst[j], lst[i]

def main():
    lst1 = list(range(30))
    shuffle(lst1)
    print("This should be in random order.")
    print(lst1)
    
if __name__ == '__main__':
    main()
