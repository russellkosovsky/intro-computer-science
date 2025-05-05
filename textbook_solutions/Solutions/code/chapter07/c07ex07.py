# c07ex07.py
#    Babysitter pay
#    This is a subtle problem with many possible solutions


def main():
    print("Babysitting Calculator\n")
    print("Enter times using 24 hour format (e.g. 8 pm is 20:00)")
    sHours, sMins = input("Starting time (hh:mm): ").split(":")
    eHours, eMins = input("Ending time (hh:mm): ").split(":")

    # convert to hours since midnight
    start = int(sHours) + float(sMins)/60.0
    end = int(eHours) + float(eMins)/60.0

    if end < start: # correct for rollover at midnight
        end = end + 24

    bedtime = 21.0
    # calculate pre and post bedtime hours
    if start < bedtime:
        if end < bedtime:
            primeHours = end - start
            extraHours = 0.0
        else:
            primeHours = bedtime - start
            extraHours = end - bedtime
    else:
        primeHours = 0.0
        extraHours = end - start

    pay = 2.50 * primeHours + 1.75 * extraHours
    print("Total payment due: ${0:0.2f}".format(pay))

if __name__ == '__main__':
    main()

