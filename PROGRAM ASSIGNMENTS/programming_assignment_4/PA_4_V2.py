# Program Assignment 4
# Russell Kosovsky

def main():
    myWin = GraphWin('Word Cloud', 700, 700)
    background = Rectangle(Point(0, 0), Point(600, 600))
    background.setFill('sky blue')
    background.draw(myWin)
    print_intro()
    file = use_file()
    stopwords = process_stopwords()
    clean_file = remove_junk(Stopwords, File)
    analysis()
    end_menu()







