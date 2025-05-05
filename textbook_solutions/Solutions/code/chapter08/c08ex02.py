# c08ex02.py
#   Windchill Table

def windChill(t, v):
    if v > 3:
        chill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    else:
        chill = t
    return chill

def main():

    # Print table headings
    print("Wind Chill Table\n\n")
    print("Temperature".center(70))
    print("MPH|", end=' ')
    temps = list(range(-20,61,10))
    for t in temps:
        print("{0:5}".format(t), end=' ')
    print("\n---+" + 55 * '-')

    # Print lines in table
    for vel in range(0,51,5):
        print("{0:3}|".format(vel), end=' ')
        for temp in temps:
            print("{0:5.0f}".format(windChill(temp, vel)), end=' ')
        print()
    print()

main()
