# Program Assignment 4
# Russell Kosovsky

myWin = GraphWin('Word Cloud', 700, 700)
background = Rectangle(Point(0, 0), Point(600, 600))
background.setFill('sky blue')
background.draw(myWin)

def main():
    print_intro()
    use_file()
    process_stopwords()
    remove_junk(Stopwords, File)
    analysis(counts)
    end_menu()

# draw myWin and display a nice opening screen with intro and instructions
def print_intro():


# determine what file to use based on users input (on myWin with text/entry objects ect.)
def use_file():
    return contents, key


# open stopwords file and use .split so its a list of each stopword
def process_stopwords(contents, key):
    return stopwords, File


# remove all the special characters from the file then the split words from users file into a list and loop through it to remove the stopwords
def remove_junk(stopwords):
    return counts


# for formatting (from zelle chapter 11.7.3)
def byFreq(pair):
    return pair[1]

# display formatted analysis of n most frequent words and draw them on myWin randomly
def analysis(counts, file):


# give option to run program again or exit
def end_menu():







