# c07ex10.py
#    Easter calculation for 1900-2099

def main():
    print("Easter Calculator for 1900-2099\n")

    year = int(input("Enter the year: "))
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d +5)%7

        day = 22 + d + e

        # This could also be a multi-way decision
        if year in [1954, 1981, 2049, 2076]:
            day = day - 7
            
        if day > 31:
            print("Easter is on April", day-31)
        else:
            print("Easter is on March", day)
    else:
        print("That's not a year between 1900 and 2099.")

if __name__ == '__main__':
    main()


