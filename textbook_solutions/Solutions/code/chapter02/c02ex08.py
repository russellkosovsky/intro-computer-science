# c02ex08.py
#    Future value with multiple compounding periods

def main():
    print("This program calculates the future value of an investment.")
    print()
    
    principal = eval(input("Enter the initial principal: "))
    rate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years: "))

    for i in range(years * periods):
        principal = principal * (1 + rate/periods)

    print("The amount in", years, "years is:", principal)

main()
