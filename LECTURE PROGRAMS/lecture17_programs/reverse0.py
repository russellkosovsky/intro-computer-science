#lecture 18 exercise: reverse string


#iterative version
def reverse0(aString):

    aReverse = ""
    for i in range(len(aString)-1, -1, -1):
        aReverse += aString[i]  #shortcut to aReverse = aReverse + aString[i]

    return aReverse
    


#recursive verison of reverse function
def reverse(aString):

    ###base case: aString is empty


    ###recursive case


    ####dummy: comment out this after completion of your code
    return ""


print(reverse0("hello"))
