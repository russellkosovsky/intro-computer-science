# c05ex10.py
#   Average word length


def main():
    print("Average word length")
    print()

    phrase = input("Enter a phrase: ")

    # using accumulator loop
    count = 0
    total = 0
    for word in phrase.split():
        total = total + len(word)
        count = count + 1

    print("Average word length", total / count)

main()
