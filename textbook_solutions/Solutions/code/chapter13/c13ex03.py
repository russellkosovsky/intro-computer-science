# c13ex03.py
# A recursive palindrome checker
#

def isPalindrome(s):
    # The base case
    if len(s) < 2:
        return True

    elif not s[0].isalpha():
        # ignore s[0] if non-letter
        return isPalindrome(s[1:])

    elif not s[-1].isalpha():
        # ignore s[-1] if non-letter
        return isPalindrome(s[:-1])

    elif s[0].lower() != s[-1].lower():
        #false if 1st and last don't match
        return False

    else:
        # if first and last match then delete 1st and last 
        # and test middle section
        return isPalindrome(s[1:-1])

def main():
    print()
    print(" Let's test a string to see if it is a palindrome.")
    print(" I'll ignore spaces, punctuation and case differences.")
    print()

    theString = input("Enter a string to test: ")
    print()
    
    if isPalindrome(theString):
        print("That IS a palindrome.")
    else:
        print("That is NOT a palindrome.")
    print()

main()
