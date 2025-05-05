#imageTest.py
#practice working with Zelle Image objects.

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

    # draw 10 red lines
    for x in range(0,imgObj.getWidth(), int(imgObj.getWidth()/20)):
        for y in range(imgObj.getHeight()):
            imgObj.setPixel(x,y,color_rgb(255,0,0))    

    #save changed image to filename, camelsBar.gif
    #you can use save(filename) method in Image object
    #use png image format. i.e. filename as "scamelBar.png"

    imgObj.save('camelsLogoBars.png')
    win.getMouse()
    win.close()
    
main()
