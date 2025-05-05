# c02ex07.py
#    Future value of amount invested yearly

def main():
    print("This program calculates the future value of a yearly investment")
    print()
    
    payment = eval(input("Enter amount to invest each year: "))
    apr = eval(input("Enter the annualized interest rate: "))
    years = eval(input("Enter the number of years: "))

    principal = 0.0
    for i in range(years):
        principal = (principal + payment) * (1 + apr)

    print("The amount in", years, "years is:", principal)

main()

