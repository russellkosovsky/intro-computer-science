# Program Assignment 4
# Russell Kosovsky

def main():
    myWin = GraphWin('Word Cloud', 700, 700)
    background = Rectangle(Point(0, 0), Point(600, 600))
    background.setFill('sky blue')
    background.draw(myWin)
    print_intro(myWin)
    use_file(myWin)
    process_stopwords()
    remove_junk(Stopwords, File)
    analysis(counts, myWin)
    end_menu(myWin)

# draw myWin and display a nice opening screen with intro and instructions
def print_intro(myWin):


# determine what file to use based on users input (on myWin with text/entry objects ect.)
def use_file(myWin):
    return contents
    return key


# open stopwords file and use .split so its a list of each stopword
def process_stopwords():
    return stopwords


# remove all the special characters from the file then the split words from users file into a list and loop through it to remove the stopwords
def remove_junk(Stopwords, File):
    return counts


# for formatting (from zelle chapter 11.7.3)
def byFreq(pair):
    return pair[1]

# display formatted analysis of n most frequent words and draw them on myWin randomly
def analysis(counts,myWin):


# give option to run program again or exit
def end_menu(myWin):




