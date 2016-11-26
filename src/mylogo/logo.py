'''
Created on 2016-11-21

@author: Sawatari
'''
import star
import leaf
import turtle
import math
from threading import Thread

#create window and turtle
window = turtle.Screen()
window.bgcolor("black")

if __name__ == '__main__':
    for i in range(1, 5):   #draw leafs through multithreading
        t = Thread(target=leaf.draw, args=(i,))
        t.start()  

starlen = (math.sqrt((10**2) * 2) / 2) / math.cos(math.radians(75))
centrstar = turtle.Turtle()
centrstar.color("white", "white")
centrstar.speed(40)
centrstar.right(45)
centrstar.forward(10)
centrstar.right(60)
centrstar.begin_fill()    #begin fill white

for i in range(1, 5):
    star.draw(centrstar, starlen)

centrstar.end_fill()
centrstar.hideturtle()

#tidy up window
window.exitonclick()        