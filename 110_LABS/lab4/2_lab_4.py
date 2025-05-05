
def main():
    obamaspeech = open("ObamaSpeech2012.txt", "r", encoding = "utf-8")

    romneyspeech = open("RomneySpeech2012.txt", "r", encoding = "utf-8")

    obamacontents = obamaspeech.read().lower()

    obamawords = obamacontents.split()

    romneycontents = romneyspeech.read().lower()

    romneywords = romneycontents.split()


    obamawordcount = len(obamawords)
    print("Obama's speech has,",obamawordcount, "words")

    romneywordcount = len(romneywords)
    print("Romney's speech has,",romneywordcount, "words")

    if obamawordcount > romneywordcount:
        print("Obama's speech has more words")
    else:
        print("Romney's speech has more words")


    userword = input("What word would you like to search?")
    
    romneysearch = romneycontents.count(userword)
    print("Romney talks about", userword, romneysearch, "times")

    obamasearch = obamacontents.count(userword)
    print("Obama talks about", userword, obamasearch, "times")

    if romneysearch > obamasearch:
        print("Romney talks about", userword, "more in his speech")
    elif romneysearch < obamasearch:
        print("Obama talks about", userword, "more in his speech")
    else:
        print("They both spoke the samw ammount of time about economics")
        
main()

