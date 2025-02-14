#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(cat, sides):
    for s in range(sides):
        cat.forward(60)
        cat.right(360/sides)
        
        
def fillCorner(dog, corner):
    drawSquare(dog, 120)
    
    if corner == 1:
        dog.begin_fill()
        drawSquare(dog, 60)
        dog.end_fill()
    elif corner == 2:
        dog.forward(60)
        dog.begin_fill()
        drawSquare(dog, 60)
        dog.end_fill()
    elif corner == 3:
        dog.left(270)
        dog.forward(60)
        dog.left(90)
        dog.begin_fill()
        drawSquare(dog, 60)
        dog.end_fill()
    elif corner == 4:
        dog.forward(120)
        dog.left(270)
        dog.forward(120)
        dog.right(90)
        dog.begin_fill()
        drawSquare(dog, 60)
        dog.end_fill()
        
def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
