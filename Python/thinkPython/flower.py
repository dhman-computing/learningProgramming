# Exercise for the CHAPTER 4 - Case Study: Interface Design

import turtle
from math import pi, sin

def arc_l(t, l, ang):
    theta = ang / 2
    theta_r = theta / 180 * pi
    r = l / 2 / sin(theta_r)
    perimeter = 2 * pi * r * ang / 360
    n = int(perimeter / 1)
    l = perimeter / n
    for i in range(n):
        t.fd(l)
        t.lt(ang/n)

def petal(t, l, ang):
    t.rt(ang / 2)
    arc_l(t, l, ang)
    t.lt(180 - ang)
    arc_l(t, l, ang)

def flower(t, l, n):
    ang = 360 / n
    for i in range(n):
        petal(t, l, ang)
        t.lt(ang / 2 + 180)

def spine(t, l, n):
    for i in range(n):
        t.pd()
        t.fd(l)
        t.pu()
        t.bk(l)
        t.lt(360 / n)

def complete_flower(t0, t1, l, n):
    spine(t1, l , n)
    flower(t0, l, n)

def double_flower(t0, t1, t2, t3, l, n):
    ang = 360 / n
    t2.lt(ang / 2)
    t3.lt(ang / 2)
    spine(t1, l , n)
    spine(t2, l , n)
    flower(t0, l, n)
    flower(t3, l, n)


pen = []
pen.append(turtle.Turtle())
pen.append(turtle.Turtle())
pen.append(turtle.Turtle())
pen.append(turtle.Turtle())
ang = 120
l = 120
n = 6

# pen[0].rt(ang/2)
# arc_l(pen[0], l, ang)
# petal(pen[0], l, ang)

# pen[1].fd(l) 
# complete_flower(pen[0], pen[1], l, n)
double_flower(pen[0], pen[1], pen[2], pen[3], l, n)

for i in range(len(pen)):
    pen[i].ht()

turtle.done()