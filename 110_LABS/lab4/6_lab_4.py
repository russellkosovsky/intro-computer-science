def listmovies():
    print("The current available movies are, Smile, Bros, and The Good House.")


def ticketprice():
    regprice = 12
    matineeprice = 10
    print("A movie ticket costs $12.00 for a regular screeing and $10.oo for matinee screeining. Infants (ages 3 years old or younger) are free, kids (ll years old or younger) cost half-price, and seniors (60 years old or older) cost 3/4 price")

    screening = input("Are you interested in \n(A) a matinee screening \n(B) regular screening\n")

    if screening == "a" or choice == "A":
        age = eval(input("How old are you? "))

        if age <= 3:
            print("Your ticket is free!")
        elif age <= 11 and age > 3:
            matineeprice = price / 2
            print("Your ticket is", matineeprice, "dollars")
        elif age >= 60:
            matineeprice = matineeprice * .75
            print("Your ticket is", matineeprice, "dollars")
        else:
            print("Your ticket is", matineeprice, "dollars")
        
    elif screening == "b" or choice == "B":
        age = eval(input("How old are you? "))

        if age <= 3:
            print("Your ticket is free!")
        elif age <= 11 and age > 3:
            price = price / 2
            print("Your ticket is", price, "dollars")
        elif age >= 60:
            price = price * .75
            print("Your ticket is", price, "dollars")
        else:
            print("Your ticket is", price, "dollars")
    

def main():
    
    print("Please choose an option below.")

    choice = input("(A) List movies \n(B) Determine ticket price \n")

    if choice == "a" or choice == "A":
        listmovies()
        
    elif choice == "b" or choice == "B":
        ticketprice()


main()
