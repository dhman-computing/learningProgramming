## Question 5.2


# a = int(input("a :"))
# b = int(input("b :"))
# c = int(input("c :"))
# n = int(input("n :"))

# d = a**n + b**n

# if d == c**n and n > 2:
#     print("Holy smokes, Fermat was wrong!")
# elif n <= 2:
#     print("n is greater than or equals to 2")
# else:
#     print("No, that doesn't work.")


## Question 5.3


def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a> b:
        print("yes!")
    else:
        print("no!")
    return 0

# a = int(input("Side 1: "))
# b = int(input("Side 2: "))
# c = int(input("Side 3: "))

# is_triangle(a, b, c)


## Question 5.4


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        print(n, s)
        recurse(n-1, n+s)

# recurse(-1, 0)


## Question 5.5


import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

# pen = turtle.Turtle()

# draw(pen, 10, 5)
# pen.lt(90)
# draw(pen, 10, 5)
# pen.lt(90)
# draw(pen, 10, 5)
# pen.lt(90)
# draw(pen, 10, 5)

# turtle.done()


## Question 5.6


import turtle

def koch(t, len):
    if len < 3:
        t.fd(len)
    else:
        koch(t, len / 3)
        t.lt(60)
        koch(t, len / 3)
        t.rt(120)
        koch(t, len / 3)
        t.lt(60)
        koch(t, len / 3)
    return

pen = turtle.Turtle()

len = 75
koch(pen, len)
pen.rt(120)
koch(pen, len)
pen.rt(120)
koch(pen, len)
pen.rt(120)


turtle.done()