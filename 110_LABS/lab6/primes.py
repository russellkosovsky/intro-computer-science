#Print out the prime numbers between 1 and a user inputted value.
#A number is prime when it is greater than 1 and divisible only by 1 and itself.
#I.e., when it doesn't have any divisors other than 1 and itself.

def main():
    playAgain = "y"
    while playAgain == "y":
        #prompt user for positive integer, n
        n = int(input("Enter a positive integer --> "))
        print ("The primes between 1 and", n, "are: ")
        #for each integer i between 1 and n
        for i in range(2,n+1):
            #check if the integer has any factors other than 1 and itself
            if isPrime(i):
                print(i)
        playAgain = input("Would you like to play again?  (y/n) --> ")

#returns True if num is prime, returns False otherwise
def isPrime(num):
    #for each integer j between 2 and num-1
    for j in range(2,num):
        #check if num is divisible by it
        if divisible(num,j):
	    #as soon as this line executes, the function is over
            return False
    return True

#returns True if numerator is divisible by denominator
def divisible(numerator, denominator):
    if numerator % denominator == 0:
        return True
    else:
        return False





main()
