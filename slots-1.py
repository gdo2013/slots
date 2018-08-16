# slots.py
# Homework #5-- Cats and Dogs
# Author: Donald Zepeda
# Date: 8/6
# Make a slot machine!

#functions
def square(upper_left, lower_right):
    #make it so that a square appears in the right place whenever the choice variables == 1
    r = (slots[i].get('upper_left'), slots[i].get('lower_right'))
    r.setFill('chocolate')
    r.draw(win)
    return r
    
def circle(center):
    #make it so that a circle appears in the right place whenever the choice variables == 0
    c = (slots[i].get('center'))
    c.setFill('yellow')
    c.draw(win)
    return c

def triangle(point_1, point_2, point_3):
    #make it so that a triangle appears in the right place whenever the choice variables == 2
    t = (slots[i].get('point_1'), slots[i].get('point_2'), slots[i].get('point_3'))
    t.setFill('cyan')
    t.draw(win)
    return t

import random
from graphics import *
win = GraphWin("Window Title",400,200) # parameters are x and y coordinates

# set up the slots
Rectangle(Point(30,20), Point(145,100)).draw(win)
Rectangle(Point(145,20), Point(260,100)).draw(win)
Rectangle(Point(260,20), Point(375,100)).draw(win)

#make the button
po1 =Point(145,120)
po2 = Point(260,170)
o = Oval(po1, po2)
o.draw(win)

slots = {
    0: {
        'upper_left': Point(68,40),
        'lower_right': Point(106,70),
        'center': Point(87.5, 60),
        'point_1': Point(68,40),
        'point_2': Point(106,40),
        'point_3': Point(87,70)
        
        },
    1: {
        'upper_left': Point(183,40),
        'lower_right': Point(221,70),
        'center': Point(202.5, 60),
        'point_1': Point(183,40),
        'point_2': Point(221,40),
        'point_3': Point(202,70)

        },
    2: {
        'upper_left': Point(298,40),
        'lower_right': Point(336,70),
        'center': Point(317.5, 60),
        'point_1': Point(298,40),
        'point_2': Point(336,40),
        'point_3': Point(317,70)

        }
        
    }

Text(Point(202.5,145), "Play").draw(win)

#make it click-interactive only within the button
while True:
    mouse = win.getMouse()
    chosen = []
    if 145 < mouse.x < 260 and 120 < mouse.y < 170:
        for i in range(3):
            choice = random.randrange(3)
            print(choice)
            chosen.append(choice)
            if choice == 1:
                r = Rectangle(square(slots[0].get('upper_left'), slots[0].get('lower_right')))
                r.setFill('chocolate')
                r.draw(win)
                continue
            if choice == 0:
                c = Circle(circle(slots[0].get('center')), 20)
                c.setFill('yellow')
                c.draw(win)
                continue
            if choice == 2:
                t = Polygon(triangle(slots[0].get('point_1'), slots[0].get('point_2'), slots[0].get('point_3')))
                t.setFill('cyan')
                t.draw(win)
                continue
            if chosen[1] == 1:
                r = Rectangle(square(slots[1].get('upper_left'), slots[1].get('lower_right')))
                r.setFill('chocolate')
                r.draw(win)
                continue
            if chosen[1] == 0:
                c = Circle(circle(slots[1].get('center')), 20)
                c.setFill('yellow')
                c.draw(win)
                continue
            if chosen[1] == 2:
                t = Polygon(triangle(slots[1].get('point_1'), slots[1].get('point_2'), slots[1].get('point_3')))
                t.setFill('cyan')
                t.draw(win)
                continue
            if chosen[2] == 1:
                r = Rectangle(square(slots[2].get('upper_left'), slots[2].get('lower_right')))
                r.setFill('chocolate')
                r.draw(win)
                continue
            if chosen[2] == 0:
                c = Circle(circle(slots[2].get('center')), 20)
                c.setFill('yellow')
                c.draw(win)
                continue
            if chosen[2] == 2:
                t = Polygon(triangle(slots[2].get('point_1'), slots[2].get('point_2'), slots[2].get('point_3')))
                t.setFill('cyan')
                t.draw(win)
            
            
        o.setFill("black")
        break
if chosen(0)==chosen(1)==chosen(2):
    print("Winner!")
    Text(Point(87.5,150), "Winner!").draw(win)
    Text(Point(317.5,150), "Winner!").draw(win)
    success = Text(Point(202.5,145), "Winner!")
    success.setFill("yellow")
    success.draw(win)
else:
    lose = Text(Point(202.5,145), "Sorrrrry")
    lose.setFill("white")
    lose.draw(win)
