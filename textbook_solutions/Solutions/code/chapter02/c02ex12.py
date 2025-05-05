# c02ex12.py
# An interactive calculator (up to 100 expressions)

def main():
    print("Welcome to the Interactive Python Calculator")
    for i in range(100):
        result = eval(input("> "))
        print(result)

main()
