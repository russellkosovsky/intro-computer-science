# c07ex12.py
#    Date validator

from c07ex11 import isLeap

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isValidDate(month, day, year):
    if 1 <= month <=12:
        # month OK, check day
        
        # determine last day of month
        if month == 2:
            if isLeap(year):
                lastDay = 29
            else:
                lastDay = 28
        else:
            lastDay = DAYS_IN_MONTH[month]

        # if day is also good, return True
        if 1 <= day <= lastDay:
            return True
        
    # did not validate
    return False 
    

def main():
    print("Date Validator\n")
    month, day, year = input("Enter a date (mm/dd/yyyy): ").split("/")
    if isValidDate(int(month), int(day), int(year)):
        print("The date is valid.")
    else:
        print("The date is invalid.")

if __name__ == '__main__':
    main()
