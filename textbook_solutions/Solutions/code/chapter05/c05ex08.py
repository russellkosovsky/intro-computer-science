# c05ex08.py
#    Caesar cipher (circular version)


def main():
    print("Caesar cipher")
    print()

    key = int(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"

    cipher = ""
    for letter in plain:
        pos = chars.find(letter)
        newpos = (pos + key) % len(chars)
        cipher = cipher + chars[newpos]

    print("Encoded message follows:")
    print(cipher)

main()
