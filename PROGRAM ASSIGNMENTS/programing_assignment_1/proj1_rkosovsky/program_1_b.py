# file: program_1_b.py
# program used to convert a group of people’s heights from English to metric and then find the group’s average height
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

def main():

    print("This program is used to convert a group of people’s heights from English measurements to metric measurments and then to find the group’s average height. ")

    # assign variable for how many people are in the group. the number is inputted by the user
    ppl = eval(input("How many people are in your group? "))

    total = 0 # accumulator

    for i in range(ppl):
        n = i+1   #for printing person nuber 1,2,3 ect. 
        print("Person " + str(n))

        ft,inc = eval(input("Enter height in feet and inches, separated by a comma: "))
        ft_to_in = (ft * 12 + inc)
        in_to_m = (ft_to_in * 0.0254)

        # round to 2 decimal places so its easier to read
        print("The height of person " + str(n) + " in feet and inches is: ", end=""), print(ft,inc)
        print("The height of person " + str(n) + " in meters is: ", end =""), print(round(in_to_m, 2))

        # extracts the persons data outside the loop to be used later for average
        total = total + in_to_m
        
    avrg_m = total / ppl
    avrg_in = (total / 0.0254) / ppl

    avrg_ft = int(avrg_in / 12) # int so its a whole number
    avrg_in_2 = int(avrg_in % 12) # int so its a whole number

    # round to 2 decimal places so its easier to read
    print("The average height of this group in meters is:", round(avrg_m, 2),"meters")
    
    print()

    print("The average height of this group in feet and inches:", avrg_ft, "feet", avrg_in_2, "inches")

# run program 
main()


