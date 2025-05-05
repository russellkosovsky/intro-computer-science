# file: bonus_check_a.py
# program that that starts with a principal of $1000, asks the user for the interest rate (using the input command),
# and then tells the user how much money she would have at the end of one year if the interest rate were compounded
# yearly, monthly, daily, and also try hourly!

print("This program tells the you how much money you would have at the end of one year if the interest rate were compounded if your starting principal is $1000")
def yearly():
    principal = 1000
    interestRate = eval(input("What is the interest rate? "))
    principal = principal*(1+interestRate)
    print()
    print("After one year, you will have $", principal, "dollars!")
    print()
    
yearly()

def monthly():
    print("Monthly coumpound")
    print()
    principal = 1000
    interestRate = eval(input("What is the interest rate? "))
    for i in range(12):
        principal = principal*(1+interestRate/12.0)
    print()
    print("After one year of monthly compound, you will have $", principal, "dollars!")
    print()

def daily():
    print("Daily coumpound")
    print()
    principal = 1000
    interestRate = eval(input("What is the interest rate? "))
    for i in range(360):
        principal = principal*(1+interestRate/360)
    print()
    print("After one year of daily compound, you will have $", principal, "dollars!")
    print()

def hourly():
    print("Hourly coumpound")
    print()
    principal = 1000
    interestRate = eval(input("What is the interest rate? "))
    for i in range(8760):
        principal = principal*(1+interestRate/8760)
    print()
    print("After one year or hourly compound, you will have $", principal, "dollars!")
    print()

    
cont = input("Would you like to know how much money you would have at the end of one year if the interest rate were compounded monthly, daily, and hourly? ")

if cont == "yes":
    print()
    monthly()
    daily()
    hourly()
else:
    print()
    print("Ok, see you later.")


    
# principal = principal*(1+interestRate)
# yearly

# principal = principal*(1+interestRate/12.0)
# monthly

# for i in range(360):
#     principal = principal*(1+interestRate/360)
# daily

# for i in range(8760):
#     principal = principal*(1+interestRate/8760) 
# hourly
    
