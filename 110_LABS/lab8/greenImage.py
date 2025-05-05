#modify image to only show greener pixels from the original image

## Needs minor modifications
## Double pounds (##) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from graphics import *

def main():

    #create window
    win = GraphWin("image processing", 800, 600)

    #create image object with pink flower (this image is 362x547 pixels)
    #so, set the centr point about half way left
    flowers  = Image(Point(200,300), "pink.gif")
    flowers.draw(win)

    #create empty image objec with the same dimension as pink.gif
    #draw this empty image on the right size of window
    noFlowers = Image(Point(600,300), flowers.getWidth(), flowers.getHeight())
    noFlowers.draw(win)

    for x in range(flowers.getWidth()):
        for y in range(flowers.getHeight()):
            #print(imgObj.getPixel(x,y))
            [r,g,b] = flowers.getPixel(x,y)
            if g > r:
                noFlowers.setPixel(x, y, color_rgb(r, g, b))
                #win.update()

    for x in range(flowers.getWidth()):
        for y in range(flowers.getHeight()):
            #print(imgObj.getPixel(x,y))
            [r,g,b] = flowers.getPixel(x,y)
            if g > r:
                pass
                #print('test')
            else:
                # keep g and b to retain shading/texture
                noFlowers.setPixel(x, y, color_rgb(0, g, 0))


    #wait for mous click and close window
    win.getMouse()
    win.close()

    #before finishing up the program, save the modified image as nopink.gif
    noFlowers.save("nopink.gif")


main()
