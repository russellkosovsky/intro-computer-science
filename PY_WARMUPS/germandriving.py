

def main():
    # conversion factor: miles per kilometer
    MPK = 0.6214
    # input speed from user in kph
    speed = int(input("what is your speed in km/h? "))
    # calculate speed in mph
    mph = speed * MPK
    # output answer
    print("your speed in miles per hour is", mph,".")

main()
