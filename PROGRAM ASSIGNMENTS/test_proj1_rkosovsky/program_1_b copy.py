# file: program_1_b.py
# program used to convert a group of people’s heights from English to metric and then find the group’s average height
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

# Write a program that someone would use to convert a group of people’s heights
# from English to metric and then find the group’s average height.  First,
# prompt the user for the number of people whose heights s/he wishes to
# average.  Convert each height given by the user from feet and inches to meters
# (or centimeters). Finally, output the average height in meters (or centimeters)
# as well as in feet and inches.


def main():
    print("This program is used to convert a group of people’s heights from English to metric and then find the group’s average height. ")
    ppl = eval(input("How many people are in your group? "))
    total = 0
    for i in range(ppl):
        n = i+1   #for printing person nuber 1,2,3 ect. 
        print("Person " + str(n))
        ft,inc = eval(input("Enter height in feet and inches, separated by a comma: "))
        ft_to_in = (ft * 12 + inc)
        in_to_m = (ft_to_in * 0.0254)
        print("Height of person " + str(n) + " in feet and inches: ", end=""), print(ft,inc)
        print("Height of person " + str(n) + " in meters: ", end =""), print(round(in_to_m, 2))
        # round to 2 decimal places so its easier to read
        # took me so long to figure out how to print the (in_to_m and ft,inc) variables because I was trying to concoctinate them with (+) and it didnt work because they are not strings.
        total = total + in_to_m
        #I eventually figured out that this line (above) had to be inside the loop so that it will repeat and add to the total each time.
    avrg_m = total / ppl
    avrg_in = (total / 0.0254) / ppl
    avrg_ft = int(avrg_in / 12)
    # int so its a whole number
    avrg_in_2 = int(avrg_in % 12)
    # int so its a whole number
    print("the average height of this groups in meters:", round(avrg_m, 2),"meters")
    # round to 2 decimal places so its easier to read
    print("the average height of this group in feet and inches:", avrg_ft, "feet", avrg_in_2, "inches")
    
main()        

