# hangman.py
from random import randrange
import string

class HangmanApp:

    'Implements a hangman game with a "pluggable" interface'

    def __init__(self, interface):
        self.interface = interface
        self.words = self.getWordList("words.txt")
        
    def getWordList(self, file):
        'Reads words from file and RETURNS them in a randomized list'
        file = open("words.txt", "r")
        words = []
        for line in file.readlines():
            word = string.strip(line) #Takes out all unnecessary white space.
            words.append(string.upper(word))
        for done in range(len(words)):
            pos = randrange(done, len(words))
            words[done], words[pos] = words[pos], words[done]
        return words
    
    def run(self):
        # Interactive loop to play multiple games of hangman
        playAgain = True
        while playAgain:
            word = self.words.pop(0)
            self.playGame(word)
            if self.words != []:
                playAgain = self.interface.askPlayAgain()
            else:
                self.interface.outOfWords()
                playAgain = False
        self.interface.closing()


    def playGame(self, word):
        'Plays a single game of hangman with word as the secret' 
        misses = 0
        hword = HangmanWord(word)
        self.interface.reset()
        self.interface.showWord(hword.getText())
        while not hword.isComplete() and misses < 7:
            letter = self.interface.getGuess()
            hit = hword.guess(letter)
            if hit:
                self.interface.showWord(hword.getText())
            else:
                misses = misses + 1
                self.interface.showMiss(misses)
        if hword.isComplete():
            self.interface.showWin()
        else:
            self.interface.showLoss(word)


class HangmanWord:
    
    def __init__(self, secret):
        self.secret = secret
        self.guesses = []
            
    def getText(self):
        # Get the letter that the user guesses.
        result = ""
        for ch in self.secret:
            if ch in self.guesses:
                #Insert the guessed letter.
                result = result + ch
            else:
                #Insert an underscore for the letter.
                result = result + '_'         
        return result
    
    def guess(self, letter):
        if letter in self.guesses:
            return 0
        self.guesses.append(letter)
        return letter in self.secret

    def isComplete(self):
        result = self.getText()
        if '_' in result:
            return 0
        else:
            return 1

class TextInterface:

    'Minimal text interface for the hangman game'

    def __init__(self):
        print "Welcome to Hangman"

    def askPlayAgain(self):
        ans = raw_input("Do you want to try another word? ")
        return ans[0] in "Yy"

    def reset(self):
        pass

    def showWord(self, word):
        print "WORD:", word

    def getGuess(self):
        lett = raw_input("Enter a letter: ")
        return lett

    def showMiss(self, num):
        print "Nope. You have", 7-num, "chances left."

    def showWin(self):
        print "Congratulations, you win!"

    def showLoss(self, word):
        print "I'm sorry, you're out of chances"
        print "The word was", word

    def outOfWords(self):
        print "Well, that's all the words I have!"

    def closing(self):
        print "Thanks for playing. Goodbye!"
    
def textMain():
    #'Testing function for the text-based version of hangman'
    interface = TextInterface()
    HangmanApp(interface).run()    

if __name__ == '__main__':
    textMain()

