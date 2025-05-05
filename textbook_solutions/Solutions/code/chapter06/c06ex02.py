# c06ex02.py
#   Prints lyrics for "The Ants Go Marching".

def verse(number, action):
    print(march(number), hurrah())
    print(march(number), hurrah())
    print(march(number))
    print(littleOne(action))
    refrain()

def march(number):
    return "The ants go marching %s by %s," % (number,number)

def hurrah():
    return "hurrah! hurrah!"

def littleOne(action):
    return "The little one stops to "+action+","

def refrain():
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! " * 3)

def main():
    actions = [ ("one", "suck his thumb"),
                ("two", "tie his shoe"),
                ("three", "climb a tree"),
                ("four", "shut the door"),
                ("five", "take a dive"),
                ("six", "pick up sticks"),
                ("seven", "talk to Kevin"),
                ("eight", "jump the gate"),
                ("nine", "swing on a vine"),
                ("ten", "say 'The End'") ]

    for n,a in actions:
        verse(n,a)
        print()

    input("Press <Enter> to Quit")

main()
