from graphics import*
from math import cos, sin, pi
from turtle import*
from PIL import Image

def main():
   

    image = Image.open("img/" + "wheel2.png")

# Rotate the image
    image = image.rotate(90)

# Save the rotated image
    image.save('rotated_image.jpg')

      
main()
