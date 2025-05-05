
from graphics import *

def main():
    win = GraphWin("Image Processing", 800, 600)

    flowers = Image(Point(200,300), "pink.gif")
    flowers.draw(win)

    noFlowers = Image(Point(600,300), flowers.getWidth(), flowers.getHeight())
    noFlowers.draw(win)

    #CHECK 8
    for x in range(flowers.getWidth()):
        for y in range(flowers.getHeight()):
            [r,g,b] = flowers.getPixel(x,y)
            if r < g: 
                noFlowers.setPixel(x,y,color_rgb(r,g,b))
                win.update()

    #Save noFlowers into nopink.gif
    noFlowers.save("nopink.gif")

    #Wait for a mouse click before closing win
    win.getMouse()
    win.close()

main()
