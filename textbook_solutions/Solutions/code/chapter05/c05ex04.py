# c05ex04.py
#   Acronym builder


def main():
    print("This program builds acronyms")
    phrase = input("Enter a phrase: ")
    acronym = ""
    for word in phrase.split():
        acronym = acronym+word[0]
    acronym = acronym.upper()

    print("The acronym is", acronym)

main()
