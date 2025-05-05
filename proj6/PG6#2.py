#Charlie Riegel / Pierce Blaeser
#Anagrams Programming Assignment
#Tuesday, April 29th 

#This code allows users to solve world jumbles by entering a scrambled word.
#It finds valid English words using a dictionary file and displays
#the results in a GUI.
#It has a splash screen and instructions, recursive anagram generation,
#and GUI buttons for solve and quit. 




from graphics import *
from time import sleep

#Loads a list of valid words from a file
class Dictionary:
    def __init__(self, filename):
        self.words = set()
        with open(filename, 'r') as file:
            for line in file:
                self.words.add(line.strip().lower())  #Stores words in lowercase

    def isvalidword(self, word):
        return word.lower() in self.words  #Checks if a word is valid

#Recursively generates all permutations of a string (anagrams)
class AnagramGenerator:
    def generate(self, s):
        if s == "":
            return [s]  #Base case: returns list with empty string
        else:
            ans = []
            for w in self.generate(s[1:]):  #Recursive call
                for pos in range(len(w) + 1):  #Insert character at all positions
                    ans.append(w[:pos] + s[0] + w[pos:])
            return ans #Return list of all anagrams 

#Main GUI class that handles displaying the interface and user interaction
class WordJumbleGUI:
    def __init__(self, dictionaryfile):
        self.dictionary = Dictionary(dictionaryfile)#Load the dictionary 
        self.anagramgenerator = AnagramGenerator() #Create anagram generator
        self.win = GraphWin("Word Jumble Solver", 600, 400)#Creat GUI
        self.win.setBackground("lightblue")
        self.showsplashscreen() #Splash screen
        self.showinstructions()#Instructions 
        self.setupinterface()

    def showsplashscreen(self):
        splash = Image(Point(300, 200), "splash.gif")
        splash.draw(self.win)
        sleep(2)
        splash.undraw()

    def showinstructions(self):
        self.win.setBackground("white")#White background

        title = Text(Point(300, 50), "Welcome to the Word Jumble Solver!")
        title.setSize(20)
        title.setStyle("bold")
        title.draw(self.win)

#Instruction lines displayed one below the other
        y = 110

#First instruction
        txt1 = Text(Point(300, y), "This program helps you solve word jumbles"\
                    " ""by finding valid English words.")
        txt1.setSize(14)
        txt1.draw(self.win)

        y += 30 # Move down by 30 pixels per line 
        txt3 = Text(Point(300, y), "How to use it:")
        txt3.setSize(14)
        txt3.draw(self.win)

        y += 30
        txt4 = Text(Point(300, y), "- Enter a scrambled word between 3 and 7"\
                    " ""letters.")
        txt4.setSize(14)
        txt4.draw(self.win)

        y += 30
        txt5 = Text(Point(300, y), "- Click 'Solve' to see valid anagrams.")
        txt5.setSize(14)
        txt5.draw(self.win)

        y += 30
        txt6 = Text(Point(300, y), "- Click 'Quit' to close the program.")
        txt6.setSize(14)
        txt6.draw(self.win)

        y += 30
        txt8 = Text(Point(300, y), "Click anywhere to begin.")
        txt8.setSize(14)
        txt8.draw(self.win)

        self.win.getMouse() #Wait for mouse click
        self.win.delete("all") #Clear screen

    def setupinterface(self):
        self.win.setBackground("lightblue") #Set background for main interface 

        #Title text 
        self.title = Text(Point(300, 40), "Word Jumble Solver")
        self.title.setSize(24)
        self.title.setStyle("bold")
        self.title.draw(self.win)

        #Instruction label 
        self.instruction = Text(Point(300, 80), "Enter a scrambled word (3-7 letters):")
        self.instruction.setSize(14)
        self.instruction.draw(self.win)

        #Input box 
        self.inputbox = Entry(Point(300, 120), 20)
        self.inputbox.setSize(14)
        self.inputbox.draw(self.win)

        #Solve button
        self.solvebutton = Rectangle(Point(250, 160), Point(350, 200))
        self.solvebutton.setFill("white")
        self.solvebutton.draw(self.win)
        self.solvetext = Text(Point(300, 180), "Solve")
        self.solvetext.draw(self.win)

        #Output display 
        self.outputtext = Text(Point(300, 280), "")
        self.outputtext.setSize(14)
        self.outputtext.draw(self.win)


        #Quit button 
        self.quitbutton = Rectangle(Point(250, 320), Point(350, 360))
        self.quitbutton.setFill("pink")
        self.quitbutton.draw(self.win)
        self.quittext = Text(Point(300, 340), "Quit")
        self.quittext.draw(self.win)

        self.mainloop() #Start interaction loop
        
    #Waits for mouse click and return which button was clicked 
    def getmouseclick(self):
        while True:
            click = self.win.getMouse() #Wait for mouse click
            if self.isinside(click, self.solvebutton): #If click on solve 
                return "solve"
            elif self.isinside(click, self.quitbutton):#If click on quit 
                return "quit"

    #Checks if a point is inside a rectangle 
    def isinside(self, point, rect):
        p1 = rect.getP1()
        p2 = rect.getP2()
        return p1.getX() <= point.getX() <= p2.getX() and p1.getY() <= \
               point.getY() <= p2.getY()

    #Validates input, finds anagrams, and displays valid results 
    def displayanagrams(self, scrambled):
        scrambled = scrambled.lower() #Convert to lowercase for consistency 
        
        #Input validation using character comparison 
        if not (3 <= len(scrambled) <= 7) or not all('a' <= c <= 'z' for c in \
                                                     scrambled):
            self.outputtext.setText("Invalid input. Please enter 3–7 letters"\
                                    " " "only.")
            return
        #Generate anagrams 
        rawanagrams = self.anagramgenerator.generate(scrambled)
        #Filter to valid ENglish words using dictionary 
        validwords = sorted(set([word for word in rawanagrams if \
                                 self.dictionary.isvalidword(word)]))

        #Display the result 
        if validwords:
            self.outputtext.setText("Valid words:\n" + ", ".join(validwords))
        else:
            self.outputtext.setText("No valid words found.")

            
    #Main loop to handle solve and quit actions 
    def mainloop(self):
        while True:
            action = self.getmouseclick() #wait for user interaction 
            if action == "solve":
                userinput = self.inputbox.getText().strip() #Get user input
                self.displayanagrams(userinput) #show anagram results 
            elif action == "quit":
                self.win.close()
                break

# Launches the Word Jumble GUI
def main():
    gui = WordJumbleGUI("2of12.txt")

if __name__ == "__main__":
    main()
