# file: program_1_b.py
# A program used to calculate whether or not the user is in a caloric surplus or a caloric deficit and by how many calories.
# This program is intended for people who know how to track calories and already have set goals for gaining weight or losing weight.
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

def main():

    print("This is a program that will calculate whether you are in a caloric surplus or a caloric deficit and by how many calories.")
    print()

    # tell user we will start with resting metabolic rate
    print("Lets start by figuring out your resting metobolic rate, or how many calories your bodily functioning burns naturally everyday.")

    # assign variable for users gender
    gender = input("Please enter your gender. (male or female) ")
    # assign variable for users weight
    weight = eval(input("Please enter your weight in pounds. "))
    # assign variable for users height
    height = eval(input("Please enter your height in inches. "))
    # assign variable for users age
    age = eval(input("Please enter your age in years. "))

    # calculte resting metabolic rate based on gender (https://www.builtlean.com/how-to-calculate-your-calorie-burn/)
    # I used if statement because the equation is different for men and woman and that was the only way that i could figure out how to differentiate and almost have 2 paths.
    if gender == "male":
        mrmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 - age)
        print("Your daily resting metobolic rate is,",round(mrmr), "calories.")

    else:
        frmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
        print("Your daily resting metobolic rate is,",round(frmr), "calories.")

    # tell user we will look at their calories for the day
    print("Now lets examine your calorie intake and how many calories you have burned.")

    # assign variable for users calories burned
    burned = eval(input("How many calories have you burned today from your activity? "))

    # figure out users calories eaten at each meal by using a loop
    # this loop uses a list with each item being a meal where the users can input their calorie intake
    # it also uses an accumulator and sets totalintake at zero then adds the calories of each meal from the list to the total and then the total is used below to calculate the final results
    total_intake = 0
    
    for i in ["Breakfast", "Lunch", "Dinner", "Snacks"]:
        intake_per = int(input("How many calories did you consume for "+i+"? "))
        total_intake = total_intake + intake_per
        
    intake = total_intake

    if gender == "male" :
        result = intake - (mrmr + burned)
        if result > 0 :
            print("You are in a caloric surplus of:", round(result), "calories, and are on track to gain weight.")
        else:
            print("You are in a caloric deficit of:", round(abs(result)), "calories, and are on track to lose weight.")

    else: # gender is female
        result = intake - (frmr + burned)
        if result > frmr + 0 :
            print("You are in a caloric surplus of:", round(result), "calories, and are on track to gain weight.")
        else:
            result < frmr + burned
            print("You are in a caloric deficit of:", round(abs(result)), "calories, and are on track to lose weight.")
     
main()
# run program
