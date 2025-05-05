# c05ex12.py
#    Future value with formatted table.

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    years = int(input("Enter the number of years: "))

    print("Year   Value")
    print("--------------")
    for i in range(years+1):
        print("{0:3}   ${1:7.2f}".format(i, principal))
        principal = principal * (1 + apr)

main()
