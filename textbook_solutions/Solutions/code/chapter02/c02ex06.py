# c02ex06.py
#    Future value with number of years as an input.

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The amount in", years, "years is:", principal)

main()
