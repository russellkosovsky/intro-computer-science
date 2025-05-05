


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



    
    romneyecon = romneycontents.count("econ")
    print("Romney talks about economics,", romneyecon, "times")

    obamaecon = obamacontents.count("econ")
    print("Obama talks about economics,", obamaecon, "times")

    if romneyecon > obamaecon:
        print("Romney talks about economics more in his speech")
    elif romneyecon < obamaecon:
        print("Obama talks about economics more in his speech")
    else:
        print("They both spoke the samw ammount of time about economics")

    chancer = romneyecon / len(romneywords)

    print("In Romney's speech, there is a", chancer, "chance that any given word will be economy")

    chanceo = obamaecon / len(obamawords)

    print("In Obama's speech, there is a", chanceo, "chance that any given word will be economy")

    if chancer > chanceo:
        print("Romney mentions the economy more frequently")
    elif chancer < chanceo:
        print("Obama mentions the economy more frequently")
    
main()

