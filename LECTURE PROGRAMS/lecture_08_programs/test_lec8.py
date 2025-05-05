
from graphics import *

myWin = GraphWin('Fun!', 400,400)


for i in range(100, 301):
    pt = Point(i,200)
    pt.draw(myWin)

myWin.getMouse()
myWin.close()
