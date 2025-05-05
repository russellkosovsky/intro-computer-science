
from PIL import Image

# Open the image file
im = Image.open('image.jpg')

# Rotate the image 90 degrees clockwise
im_rotated = im.rotate(90)

# Save the rotated image
im_rotated.save('image_rotated.jpg')

##def main():
##    win= win = GraphWin('buttons', 600,600)
##    win.setBackground('green3')
##    image = Image(Point(300, 300), "img/" + "wheel2.png")
##    image.draw(win)
##    
##    win.getMouse()
##
## 
## 
##
##
##
##    
##
##    
##main()
