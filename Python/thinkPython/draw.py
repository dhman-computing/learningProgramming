# Exercise for the CHAPTER 4 - Case Study: Interface Design

import turtle
from math import pi, sin

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def polygon(t, n, l):
    angle = 360/n
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def circle(t, r):
    perimeter = 2 * pi * r
    n = int(perimeter / 5)
    l = perimeter / n
    for i in range(n):
        t.fd(l)
        t.lt(360/n)

def arc_r(t, r, ang):
    perimeter = 2 * pi * r * ang / 360
    n = int(perimeter / 1)
    l = perimeter / n
    for i in range(n):
        t.fd(l)
        t.lt(ang/n)

def arc_l(t, r, len):
    # len = 2 * pi * r * ang / 360
    ang = len * 360 / (2 * pi * r)
    n = int(len / 5)
    l = len / n
    for i in range(n):
        t.fd(l)
        t.lt(ang/n)

# def flower(t, n, r):
    # ang = 360 / n
    # r = len / (2 * sin (ang * 180 / pi))
    # arc_l(t, r, len)
    # t.rt(ang)
    # arc_l(t, r, len)
    # t.lt(180)
    # t.lt(90)
    # t_ang = 360 / n

    # for i in range(n):
    #     t.fd(len)
    #     t.pu()
    #     t.lt(180)
    #     t.fd(len)
    #     t.lt(180)
    #     # print(360 / (n + 1))
    #     t.lt(t_ang)
    #     t.pd()
    
    # t.rt(t_ang / 2)
    # r = len / (2 * sin (t_ang * 180 / pi / 2))
    # arc_l(t, r, len)
    # t.lt(t_ang / 2)
    # t.fd(len)

def petal_r(t, r, ang):
    t.lt(90)
    t.rt(ang / 2)
    arc_r(t, r, ang)
    t.rt(180)
    t.rt(ang)
    arc_r(t, r, ang)

def flower_r(t, r, n):
    for i in range(n):
        petal_r(t, r, 360 / n)
        t.rt(180 + 360 / n)

def flower_l(t, l, n):
    r = l / (2 * sin (360 / n * 180 / pi / 2))
    flower_r(t, r, n)

pen0 = turtle.Turtle()
pen1 = turtle.Turtle()

# pen0.ht()
# pen1.ht()

# polygon(pen, 5, 100)
# circle(pen,100)
# arc_r(pen, 100, 360)
# arc_l(pen, 100, 2 * pi * 100)
# petal_r(pen, 100, 60)

# pen1.lt(90)
# pen1.fd(100)
# flower_r(pen0, 100, 3)
# flower_l(pen0, 100, 5)

turtle.done()
# turtle.exitonclick()