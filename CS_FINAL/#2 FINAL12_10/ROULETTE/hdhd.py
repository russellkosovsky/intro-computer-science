import random
import time
from graphics import *
from math import*

# Create the window
win = GraphWin("Roulette", 400, 400)

# Draw the roulette wheel
wheel = Circle(Point(200,200), 150)
wheel.setFill("white")
wheel.draw(win)

# Draw the black and red slots on the wheel
for i in range(0, 36):
  angle = i * 10
  x = 200 + 130 * sin(radians(angle))
  y = 200 - 130 * cos(radians(angle))
  
  slot = Circle(Point(x,y), 20)
  if i % 2 == 0:
    slot.setFill("black")
  else:
    slot.setFill("red")
  slot.draw(win)

# Get the user's bet
bet = input("Enter your bet (red, black, or a number): ")

# Spin the wheel
winning_number = random.randint(0, 36)
wheel.move(5,5)
time.sleep(1)
wheel.move(-5,-5)
time.sleep(1)
wheel.move(3,3)
time.sleep(1)
wheel.move(-3,-3)
time.sleep(1)

# Check if the user won
if winning_number == 0:
  result = "green"
elif winning_number % 2 == 0:
  result = "black"
else:
  result = "red"

if bet == result:
  print("You win!")
else:
  print("You lose!")

# Wait for the user to close the window
win.getMouse()
win.close()
