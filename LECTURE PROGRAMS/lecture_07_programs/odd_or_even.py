# odd or even program

def main():
    num = eval(input("Enter a number: "))
    num = num % 2
    if num == 1:
        print("It is an odd number.")
    else:
        print("It is an even number.")
        
main()
