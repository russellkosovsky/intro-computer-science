# c13ex06.py
#   digits in english

#   global list of words

engDig = ["Zero","One","Two","Three","Four","Five",
          "Six","Seven","Eight","Nine"]

def digitsToWords(num):
    # base case is left most digit
    if num < 10:
        print(engDig[num], end=' ')
    else:
        currentDigit = num % 10
        digitsToWords(num//10)
        print(engDig[currentDigit], end=' ')

def main():
    print()
    print("Let's write out the digits of a number in words")
    print()

    x = int(input("Enter a positive integer: "))

    print()
    print("The digits of",x,"are:")
    digitsToWords(x)
    print()
    print()

main()
