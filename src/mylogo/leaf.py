'''
Created on 2016-11-26

@author: Sawatari
'''
import math
import turtle

def setangle(leaf, ang, curlong, tolong, adjust):
    addlength = math.sqrt((1.5**2) * 2) * math.tan(math.radians(90 - ang))
    leaf.left(180 - ang)
    leaf.forward(curlong + tolong * adjust)
    leaf.right(45)
    leaf.forward(1.5)
    leaf.right(90)
    leaf.forward(1.5)
    leaf.right(45)
    leaf.forward(curlong + addlength + tolong * adjust)

    leaf.right(180 - (2 * (ang)))
    leaf.forward(curlong + addlength + tolong * adjust)
    leaf.right(45)
    leaf.forward(1.5)
    leaf.right(90)
    leaf.forward(1.5)
    leaf.right(45)
    leaf.forward(curlong + tolong * adjust)

    leaf.right(ang)
    leaf.forward(8)
    return

def printleaf(leaf):    
    leaf.right(180)
    setangle(leaf, 50, 10, 0, 1)

    for i in range(1,7):    #55
        tolong = i * 3
        setangle(leaf, 55, 10, tolong, 1.4)        
    for i in range(1,6):    #60
        curlong = 10 + 6 * 3 * 1.4
        tolong = i * 3
        setangle(leaf, 60, curlong, tolong, 1)
    for i in range(1,6):    #65
        curlong = 10 + 6 * 3 * 1.4 + 5 * 3
        tolong = i * 3
        setangle(leaf, 65, curlong, tolong, 0.4)             
    return

def draw(i):
    angle = 45 + (i - 1) * 90
    leaf = turtle.Turtle()
    leaf.color("white", "black") #paintbrush color, filling color
    leaf.speed(40)
    #draw stalk
    leaf.pensize(2)
    leaf.right(angle)    #turn left 90 degrees(right straight is default)
    leaf.forward(160)    #straight lengths
    #draw leafs
    leaf.pensize(1)
    printleaf(leaf)
    #hide the turtle
    leaf.hideturtle()    #hide the arrow
    return