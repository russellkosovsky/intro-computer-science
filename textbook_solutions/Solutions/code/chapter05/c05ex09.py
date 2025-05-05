# c05ex09.py
#    Count words in sentence


def main():
    print("Word counter")
    print()

    phrase = input("Enter a phrase: ")

    # using accumulator loop
    count = 0
    for i in phrase.split():
        count = count + 1

    # alternatives: count = len(phrase.split())
    #               count = phrase.count(" ") + 1

    print("Number of words:", count)

main()
