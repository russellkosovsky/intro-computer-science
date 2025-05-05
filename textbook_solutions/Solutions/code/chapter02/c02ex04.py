# c02ex04.py
#   Loop to perform 5 temperature conversions

def main():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print()

main()
