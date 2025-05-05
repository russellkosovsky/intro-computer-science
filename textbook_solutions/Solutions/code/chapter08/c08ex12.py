# c08ex12.py
#    Batch heating/colling degree-days


def main():
    print("Heating and Cooling degree-day calculation.")
    fname = input("Enter name of file with average temperature data: ")
    infile = open(fname, 'r')

    heating = 0.0
    cooling = 0.0
    for line in infile:
        temp = float(line)
        heating = heating + max(0, 60-temp)
        cooling = cooling + max(0, temp-80)
    infile.close()

    print("\nTotal heating degree-days", heating)
    print("Total cooling degree-days", cooling)

if __name__ == '__main__':
    main()

    
    
