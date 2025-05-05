

###### CHECK 2/3


import math

def main():
    print("This program inputs prices for the small and the large pizzas at Two Wives, then calculates and compares the price per square inch for each")
    small10 = eval(input("How much does a small pizza cost? "))
    large14 = eval(input("How much does a large pizza cost? "))

    smallarea = math.pi * (5 ** 2)
    largearea = math.pi * (7 ** 2)

    print("small area", smallarea)

    

    small_inches = smallarea / small10
    large_inches = largearea / large14
    
    
    small_priceper = small10 / smallarea
    large_priceper = large14 / largearea

    print("A small pizza gets you", round(small_inches, 2), "square inches of pizza per $1.00.")
    print("On the other hand, a large pizza gets you", round(large_inches, 2), "square inches of pizza per $1.00")
    
    
    print("This means that a small pizza costs", round(small_priceper, 2) , "cents per square inch while a large piza only costs", round(large_priceper, 2) , "cents per square inch")

main()
