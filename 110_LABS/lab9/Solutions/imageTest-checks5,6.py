
#imageTest.py
#practice working with Zelle Image objects.

from graphics import *

def main():

    win = GraphWin("the Zelle graphics Image class", 800, 400)
    imgObj = Image(Point(400,200), "camelsLogo.gif")
    imgObj.draw(win)

    #print out some info about our Image object
    imgCenterPt = imgObj.getAnchor()
    print("Image is centered at: (", imgCenterPt.getX(), ",", imgCenterPt.getY(), ")")
    print("Width of image is: ", imgObj.getWidth())
    print("Height of image is:", imgObj.getHeight())
    print("Pixel (0, 0) has rgb values:", imgObj.getPixel(0,0))
    print("Pixel (143, 130) has rgb values:", imgObj.getPixel(143,130))

    #alter the center column of pixels so that they are red
    for y in range(int(imgObj.getHeight())):
        x = int(imgObj.getWidth()/2)
        imgObj.setPixel(x,y,color_rgb(200,0,0))


    #CHECK 6
    #draw red vertical lines all the way across the image
    for x in range(0,imgObj.getWidth(), 25):
        for y in range(imgObj.getHeight()):
            imgObj.setPixel(x, y, color_rgb(255,0,0))   

    #CHECK 7
    #Save modified image into a new file
    imgObj.save("camelsLogoBars.gif")
              
    #Wait for click before closing
    win.getMouse()
    win.close()

main()
