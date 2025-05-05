def main():
    
    print("Please choose an option below.")

    choice = input("(A) List movies \n(B) Determine ticket price \n")



    if choice == "a" or choice == "A":

        print("The current available movies are, Smile, Bros, and The Good House.")

    elif choice == "b" or choice == "B":
        price = 12
    
        print("A movie ticket costs $12.00 but, infants (ages 3 years old or younger) are free, kids (ll years old or younger) cost half-price, and seniors (60 years old or older) cost 3/4 price")

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
    
        
main()
