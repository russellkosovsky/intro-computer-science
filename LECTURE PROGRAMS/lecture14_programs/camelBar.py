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

    #alter the center column of pixels so that they are red
    #you can use setPixel(x, y, colorvalue) method in Image object
    #to change color of pixel. For colorvalue use color_rgb(r,g,b) function

   # midX = int(imgObj.getWidth()/2)
   # for y in range(imgObj.getHeight()):
   #     imgObj.setPixel(midX, y, color_rgb(255,0,0))


    # draw 10 red lines
    for x in range(0,imgObj.getWidth(), int(imgObj.getWidth()/10)):
        for y in range(imgObj.getHeight()):
            imgObj.setPixel(x,y,color_rgb(255,0,0))




##    for x in range(imgObj.getWidth()):
##
##        for y in range(imgObj.getHeight()):
##
##            imgObj.getPixel(x,y)
##
##            imgObj.setPixel(x, y, 'red')
    

    
    #save changed image to filename, camelsBar.gif
    #you can use save(filename) method in Image object
    #use png image format. i.e. filename as "scamelBar.png"

    imgObj.save('camelBar.png')
    
    win.getMouse()
    win.close()
    
main()
