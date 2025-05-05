
#imageTest.py
#practice working with Zelle Image objects.

## Needs minor modifications
## Double pounds (##) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from graphics import *

def main():
    win = GraphWin("the Zelle graphics Image class", 800, 400)
    
    imgObj = Image(Point(400,200), "camelsLogo.png")
    imgObj.draw(win)

    #print out some info about our Image object
    imgCenterPt = imgObj.getAnchor()
    print("Image is centered at: (", imgCenterPt.getX(), ",", imgCenterPt.getY(), ")")
    print("Width of image is: ", imgObj.getWidth())
    print("Height of image is:", imgObj.getHeight())
    print("Pixel (0, 0) has rgb values:", imgObj.getPixel(0,0))
    print("Pixel (143, 130) has rgb values:", imgObj.getPixel(143,130))

    ##alter the center column of pixels so that they are red
    ##instead of drawing one red vertical line, change below code to draw multiple lines
    for y in range(imgObj.getHeight()):
        x = int(imgObj.getWidth()/2)
        imgObj.setPixel(x,y,color_rgb(255,0,0))

    imgObj.save("camelsBars.png")
    
    win.getMouse()
    win.close()
    
main()
