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

    # turn white pixels to pink
    for x in range(imgObj.getWidth()):
        for y in range(imgObj.getHeight()):
            #print(imgObj.getPixel(x,y))
            [r,g,b] = imgObj.getPixel(x,y)
            if r > 220 and g > 220 and b > 220:
                imgObj.setPixel(x, y, color_rgb(255, 255, 0))

    # make camel pink
    for x in range(imgObj.getWidth()):
        for y in range(imgObj.getHeight()):
            #print(imgObj.getPixel(x,y))
            [r,g,b] = imgObj.getPixel(x,y)
            if b > r:
                # keep g and b to retain shading/texture
                imgObj.setPixel(x, y, color_rgb(255, g, b))

    #save changed image to filename, camelsBar.png you can use save(filename) method in Image object
    imgObj.save('camelBar.png')
    win.getMouse()
    win.close()
    
main()

