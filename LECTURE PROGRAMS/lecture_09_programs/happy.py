#print out happy birthday lyrics for James 


def happy():
    print("Happy birthday to you!")

def happysong(n):
    happy()
    happy()
    print("Happy birthday dear,",n)
    happy()

def main():
    name = input("Who is celebrating a birthday? ")
    happysong(name)

main()
