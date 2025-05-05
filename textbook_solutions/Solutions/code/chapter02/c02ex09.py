# c02ex09.py
#    Fahrenheit to Celsius conversion


def main():
    print("The program converts temperatures from Fahrenheit to Celsius")
    print()
    
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5.0 / 9.0 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius")

main()
