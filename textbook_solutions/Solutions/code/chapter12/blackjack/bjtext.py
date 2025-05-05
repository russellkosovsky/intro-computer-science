# bjtext.py
#    program to play Blackjack with a text-based interface.

from blackjack import BlackjackApp  # import the game logic

class TextInter:

    def __init__(self):
        print("Welcome to the Blackjack table")
        print("You start with $100.")

    def wantToPlay(self):
        print("-"*50)
        x = input("Do you want to try your luck? ")
        return x[0].lower() == 'y'

    def setMoney(self, amount):
        print("You have ${0} dollars.".format(amount))

    def playerCard(self, card):
        print("Player:\t\t\t\t", card)

    def dealerCard(self, card):
        print("Dealer:\t\t", card)

    def message(self, mess):
        print()
        print("************** {0} **************".format(mess).center(50))
        print()

    def clear(self):
        print()

    def close(self):
        print("Thanks for playing!")

    def wantCard(self):
        ans = input("Another card? ")
        return ans.lower()[0] == 'y'

if __name__ == '__main__':
    interface = TextInter()
    app = BlackjackApp(interface)
    app.play()
