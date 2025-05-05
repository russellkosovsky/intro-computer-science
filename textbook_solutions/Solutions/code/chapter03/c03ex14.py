# c03ex14.py
#    Average of numbers entered by the user.

def main():
    print("Program to calculate average")
    print()

    n = int(input("How many numbers do you have? "))
    total = 0
    for i in range(n):
        num = float(input("Enter a number: "))
        total = total + num

    print()
    print("The average of the numbers is:", total/n)

main()

