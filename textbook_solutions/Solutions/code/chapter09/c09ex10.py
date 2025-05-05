
#    Monte Carlo estimation of pi

from random import random

def main():
    print("This program estimates the value of pi using")
    print('random "dart" tosses.')
    n = int(input("\nHow many darts should I simulate? "))
    hits = throwDarts(n)
    print("Estimated Number of hits =", hits)
    print("Estimated value of pi =", 4.0 * hits / n)

def throwDarts(n):
    hits = 0
    for i in range(n):
        x = 2 * random() - 1
        y = 2 * random() - 1
        if x * x + y * y <= 1:
            hits = hits + 1
    return hits

if __name__ == '__main__':
    main()
    
