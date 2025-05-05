# c07ex06.py
#    Speeding tickets

def main():
    print("Speeding fine calculator\n")
    limit = float(input("Enter the speed limit "))
    speed = float(input("Enter the clocked speed "))

    if speed <= limit:
        print("Legal")
    else:
        fine = 50 + 5*(speed - limit)
        if speed > 90:
            fine = fine + 200
        print("Fine ${0:0.2f}".format(fine))

if __name__ == "__main__":
    main()

