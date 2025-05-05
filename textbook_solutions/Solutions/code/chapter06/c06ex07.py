# c06ex07.py

def fibo(n):
    curr, prev = 1,1
    for i in range(n-2):
        curr, prev = curr+prev, curr
    return curr

def main():
    print("Nth Fibonacci number\n")
    n = int(input("Enter n: "))
    print("The Fibonacci value is", fibo(n))

main()
