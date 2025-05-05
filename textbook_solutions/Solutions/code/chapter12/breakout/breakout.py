# breakout.py

import math
from random import randrange
from graphics import *

class Ball:

    """A pong-style bouncing ball"""

    def __init__(self, window, center, radius, angle):
        """ create a ball (circle) in the window having the given
        center (a point), radius and angle (the direction of travel in
        degrees).
        """

        #instance variables:
        #    radius (the radius of the ball)
        #    marker (the circle object marking its position)
        #    dx, dy (the x and y components of the ball's direction).
        self.radius = radius

        theta = math.radians(angle)
        self.dx = math.cos(theta)
        self.dy = math.sin(theta)

        self.marker = Circle(center, radius)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(window)

    def getLeadingX(self):
        """return the x coordinate of the most 'forward' horizontal
        point of the ball.
        """
        xc = self.marker.getCenter().getX()
        if self.dx < 0:
            x =  xc - self.radius
        else:
            x = xc + self.radius
        return x
    
    def getLeadingY(self):
        """return the y coordinate of the most 'forward' vertical
        point of the ball.
        """
        yc = self.marker.getCenter().getY()
        if self.dy < 0:
            y = yc - self.radius
        else:
            y = yc + self.radius
        return y

    def move(self, distance):
        """Move the ball distance units in the current direction"""
        self.marker.move(self.dx*distance, self.dy*distance)

    def reflectX(self):
        """Reverse the x direction of the ball."""
        self.dx = -self.dx

    def reflectY(self):
        """Reverse the y direction of the ball."""
        self.dy = -self.dy

    def getCenter(self):
        return self.marker.getCenter()
    

class BoundingBox:

    def __init__(self, xlow, ylow, xhigh, yhigh):
        self.xlow = xlow
        self.xhigh = xhigh
        self.ylow = ylow
        self.yhigh = yhigh

    def isInside(self, x, y):
        return (self.xlow < x < self.xhigh) and (self.ylow < y < self.yhigh)

    def bounce(self, ball):
        center = ball.getCenter()
        hit = False
        if self.isInside(ball.getLeadingX(), center.getY()):
            ball.reflectX()
            hit = True
        if self.isInside(center.getX(), ball.getLeadingY()):
            ball.reflectY()
            hit = True
        return hit

    def slide(self, amt):
        self.xlow += amt
        self.xhigh += amt


class Wall:

    def __init__(self, win, p1, p2):
        color = "gray"
        self.marker = Rectangle(p1,p2)
        self.marker.setFill(color)
        self.marker.setOutline(color)
        self.marker.draw(win)
        self.bbox = BoundingBox(p1.getX(), p1.getY(), p2.getX(), p2.getY())

    def bounce(self, ball):
        return self.bbox.bounce(ball)


class Brick:

    def __init__(self, win, p1, p2, color):
        self.marker = Rectangle(p1,p2)
        self.marker.setFill(color)
        self.marker.setOutline(color)
        self.marker.draw(win)
        self.bbox = BoundingBox(p1.getX(), p1.getY(), p2.getX(), p2.getY())

    def bounce(self, ball):
        hit = self.bbox.bounce(ball)
        if hit:
            self.marker.undraw()
        return hit


class Paddle:

    def __init__(self, win, p1, p2, xmin, xmax):
        color = "orange"
        self.marker = Rectangle(p1,p2)
        self.marker.setFill(color)
        self.marker.setOutline(color)
        self.marker.draw(win)
        self.bbox = BoundingBox(p1.getX(), p1.getY(), p2.getX(), p2.getY())
        self.centerX = self.marker.getCenter().getX()

        
    def bounce(self, ball):
        return self.bbox.bounce(ball)

    def move(self, dx):
        self.marker.move(dx, 0.0)
        self.bbox.slide(dx)

    

class BreakoutGame:

    def __init__(self):
        win = GraphWin("Breakout!", 1024, 768, autoflush=False)
        win.setCoords(-200,-150, 200, 150)
        win.setBackground("black")

        self.walls = [ Wall(win, Point(-200, -140), Point(-180, 120)),
                       Wall(win, Point(180, -140), Point(200, 120)),
                       Wall(win, Point(-200, 100), Point(200, 120)),
                       #Wall(win, Point(-200, -150), Point(200, -130))
                       ]

        bricks = []
        for i in range(30):
            x1 = randrange(-180,140)
            y1 = randrange(0, 80)
            color = color_rgb(randrange(256), randrange(256), randrange(256))
            brick = Brick(win, Point(x1, y1), Point(x1+40, y1+10), color)
            bricks.append(brick)
        self.bricks = bricks
        self.paddle = Paddle(win, Point(-25,-145), Point(25,-140), -180, 180)
                       

        self.win = win
        self.ball = Ball(win, Point(0,-50), 5, 40)

    def run(self):
        ball = self.ball
        self.win.getKey()
        while self.bricks !=[] and ball.getLeadingY() > -150:
            key = self.win.checkKey()
            if key == "Escape":
                break
            self.movePaddle(key)
            self.ball.move(1.5)
            hit = self.paddle.bounce(ball)
            if not hit:
                for wall in self.walls:
                    hit = wall.bounce(ball)
            if not hit:
                for b in self.bricks:
                    if b.bounce(ball):
                        self.bricks.remove(b)
                        break
            update(100)
        self.win.getMouse()
        self.win.close()

    def movePaddle(self, key):
        speed = 10
        if key == 'Left':
            self.paddle.move(-speed)
        elif key == 'Right':
            self.paddle.move(speed)


if __name__ == "__main__":
    game = BreakoutGame()
    game.run()
