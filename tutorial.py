import cv2 as cv
import numpy as np
import random

# Define how many iterations to run
iterationCount = 1000

# Define the size of the canvas
canvas = np.zeros((720, 1280, 3), np.uint8)

# Create a random color
def randomColor():
    return [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

# Draw a random rectangle in the canvas
def drawReactangle():
    cv.rectangle(canvas,[random.randint(0,1280), random.randint(0,720)], [random.randint(0,1280), random.randint(0,720)], randomColor(), random.randint(1,50))

# Draw a random circle in the canvas
def drawCircle():
    cv.circle(canvas, [random.randint(0,1280), random.randint(0,720)], random.randint(0,512), randomColor(), random.randint(1,50))

# Draw a random ellipse in the canvas
def drawEllipse():
    cv.ellipse(canvas, [random.randint(0,1280), random.randint(0,720)], [random.randint(0,1280), random.randint(0,720)], random.randint(0,360), random.randint(0,360), random.randint(0,360), randomColor(), random.randint(1,50))

# Defining a switch statement like thing (thanks python for being like this)
drawOptions = {0: drawReactangle, 1: drawCircle, 2: drawEllipse}

# For each iteration create a random shape
for x in range(iterationCount):
    # Determine what shape should be created
    shape = random.randint(0,2)
    drawOptions[shape]()

# Show the canvas until the user hits "esc"
while True:
    cv.imshow('Canvas', canvas)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()