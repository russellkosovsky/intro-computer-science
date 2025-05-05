# this program prints out the first 25 multiples of a specified value and n multiples of a user-specified value, where n is also a user-specified value



###### CHECK 4

def main():
    print("this program will print out the first 25 multiples of a specified value")
    print()
    value = eval(input("Enter a number grater than 0: "))
    for i in range (1, 25):
        multiples = value * i
        print(multiples)
    print("Now you can choose how many multiples.")
    n = eval(input("how many multiples do you want me to print?: "))
    value = eval(input("Enter a number grater than 0: "))
    for i in range (1, n):
        multiples = value * i
        print(multiples)
main()
