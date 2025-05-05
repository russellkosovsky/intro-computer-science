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



    
    romneyecon = romneycontents.find("economy")
    

    obamaecon = obamacontents.find("economy")
   
    if romneyecon > obamaecon:
        print("Obama talks about economics sooner in his speach>")

    elif romneyecon < obamaecon:
        print("Romney talks about economics sooner in his speach>")

main()
