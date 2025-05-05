# c02ex05.py
#     Table of temperature conversions

# Note: Table alignment is hacked here. Formatted output is covered in
#       Chapter 5.

def main():
    print("Celsius  Fahrenheit")
    print("-------------------")
    print(" 0          32.0")
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print(celsius, "        ", fahrenheit)
    print("100         212.0")

main()
