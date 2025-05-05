# c07ex05.py
#   Body mass index

def main():
    print("Body Mass Index Calclator\n")

    weight = float(input("Enter your weight (in pounds): "))
    height = float(input("Enter you height (in inches): "))
    bmi = (720 * weight) / height**2

    print("Your BMI is", bmi)
    if bmi < 19:
        print("That's on the low side.")
    elif bmi <= 25:
        print("That's in the healthy range.")
    else:
        print("That's on the high side.")

if __name__ == '__main__':
    main()
    
