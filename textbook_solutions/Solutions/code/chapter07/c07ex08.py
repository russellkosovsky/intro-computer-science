# c07ex08.py
#   Eligibility for Congress
#   Note: This solution does not use Boolean operators, since
#         they are introduced in Chapter 8.

def main():
    print("Congressional Eligibility\n")
    age = int(input("Enter your age: "))
    residency = int(input("Enter years of residency: "))
    if age >= 30:
        if residency >= 9:
            print("You are eligible for the Senate and the House.")
        elif residency >= 7:
            print("You are eligible only for the House.")
        else:
            print("You are not eligible for Congress.")
    elif age >= 25:
        if residency >= 7:
            print("You are eligible only for the House.")
        else:
            print("You are not eligible for Congress.")
    else:
        print("You are not eligible for Congress.")

if __name__ == '__main__':
    main()
