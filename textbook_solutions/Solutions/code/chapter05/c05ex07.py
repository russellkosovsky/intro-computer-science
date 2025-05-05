# c05ex07.py
#    Caesar cipher (non-circular)

def main():
    print("Caesar cipher")
    print()

    key = int(input("Enter the key value: "))
    plain = input("Enter the phrase to encode: ")
    cipher = ""
    for letter in plain:
        cipher = cipher + chr(ord(letter) + key)

    print("Encoded message follows:")
    print(cipher)

main()
