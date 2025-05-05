# c11ex10.py
#    Sieve of Eratosthenes

def sieve(n):
    # initially, all values are in the sieve of candidates
    candidates = list(range(2,n+1))
    primes = []
    while candidates != []:
        # remove first item, it's prime
        newPrime = candidates[0]
        primes.append(newPrime)


        # create new candidate list of all the non-divisble candidates
        cands2 = []
        for c in candidates:
            if c % newPrime != 0:
                cands2.append(c)
        candidates = cands2
        # alt: candidates = [c for c in candidates if c%newPrime != 0]
    return primes

def main():
    print("Sieve of Eratosthenes\n")
    n = int(input("Enter upper limit: "))
    primes = sieve(n)
    for p in primes:
        print(p)

        
if __name__ == '__main__':
    main()
