#c08ex03.py
#    Years for investment to double

def main():
    print("Number of years for an investment to double.\n")

    apr = float(input("What is the annual interest rate? "))
    principal = 1
    years = 0
    while principal < 2:
        principal = principal*(1+apr)
        years = years + 1

    print("Years to double:", years)

if __name__ == '__main__':
    main()
