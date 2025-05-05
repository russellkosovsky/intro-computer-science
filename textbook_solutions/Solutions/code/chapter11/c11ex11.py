# c11ex11.py

def main():
    fname = input("Enter file to censor: ")
    infile = open(fname, 'r')
    
    fname = input("Enter file for censored output: ")
    outfile = open(fname, 'w')

    for line in infile:
        words = []
        for word in line.split():
            if len(word) == 4:
                words.append("****")
            else:
                words.append(word)
        newLine = " ".join(words)
        print(newLine, file=outfile)

    infile.close()
    outfile.close()
    print("Censored file written to", fname)

main()


