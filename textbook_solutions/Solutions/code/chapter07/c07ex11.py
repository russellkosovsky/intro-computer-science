# c07ex11.py
#     Leap year determination

def isLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def main():
    print("This program calculates whether a year is a leap year.\n")
    year = int(input("Enter a year: "))
    if isLeap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
        
if __name__ == '__main__':
    main()
