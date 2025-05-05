# c05ex13.py
#    Batch Caesar cipher
#    Input file format: first line is key value;
#                       remaining lines are text to encode.


def main():
    print("Batch Caesar cipher")
    print()

    inName = input("Enter name of the input file: ")
    infile = open(inName,'r')
    key = int(infile.readline())

    outName = input("Enter name of output file: ")
    outfile = open(outName, 'w')
    

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    for line in infile:
        for letter in line[:-1]:
            pos = chars.find(letter)
            newpos = (pos + key) % len(chars)
            print(chars[newpos], file=outfile, end="")
        print(file=outfile)

    infile.close()
    outfile.close()
    print("Done")

main()
