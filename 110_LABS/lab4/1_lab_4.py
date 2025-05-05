

def main():
    
    obamaspeech = open("ObamaSpeech2012.txt", "r", encoding = "utf-8")
    romneyspeech = open("RomneySpeech2012.txt", "r", encoding = "utf-8")

    obamacontents = obamaspeech.read().lower()
    romneycontents = romneyspeech.read().lower()

    obamawords = obamacontents.split()
    romneywords = romneycontents.split()


    obamawordcount = len(obamawords)
    romneywordcount = len(romneywords)
    
    print("Obama's speech has,",obamawordcount, "words")
    print("Romney's speech has,",romneywordcount, "words")


    if obamawordcount > romneywordcount:
        print("Obama's speech has more words")
    else:
        print("Romney's speech has more words")


    romneyecon = romneycontents.count("economy")
    obamaecon = obamacontents.count("economy")

    print("Romney talks about economics,", romneyecon, "times")
    print("Obama talks about economics,", obamaecon, "times")

    if romneyecon > obamaecon:
        print("Romney talks about economics more in his speech")
    elif romneyecon < obamaecon:
        print("Obama talks about economics more in his speech")
    else:
        print("They both spoke the samw ammount of time about economics")
        
main()
