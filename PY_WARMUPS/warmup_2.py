# file: warmup_2.py
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)
#
# program that prompts the user for his/her height in inches
# and feet and then outputs his/her height in total inches.

print("This program converts your height from feet and inches to inches.")

def main():
    
    feet, inches = eval(input("Enter height in feet and inches, separated by a comma: "))
    
    feet_to_inches = (feet * 12)

    total_inches = feet_to_inches + inches
    
    print("Your height in inches is, " , total_inches)

main()
