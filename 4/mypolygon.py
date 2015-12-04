# encoding: utf-8

import turtle
import math
# from math import math.pi

# bob = turtle.Turtle()
# # turtle.mainloop()
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)
# 
# turtle.mainloop()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    '''画多边形

    parm t: turtle实例
    parm length: 边长
    parm n: 边数
    '''
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    '''画圆，分360度画，每度画一次

    parm t: turtle
    parm r: 半径
    '''
    steps = 360
    step_angle = 360 / steps
    perimeter = 2 * math.pi * r
    step_length = perimeter / steps

    for i in range(steps):
        t.fd(step_length)
        t.lt(step_angle)


def circle_2(t, r):
    perimeter = 2 * math.pi * r
    n = 360
    length = perimeter / n
    polygon(t, length, n)


def arc(t, r, angle):
    '''画弧

    parm t: turtle
    parm r: 半径
    parm angle: 弧的角
    '''
    perimeter = 2 * math.pi * r
    lengths = perimeter * angle / 360.0
    # steps = 100
    # step_angle = int(angle / steps) + 1
    steps = int(angle)
    step_angle = 1
    step_length = lengths / steps
    for i in range(steps):
        t.fd(step_length)
        t.lt(step_angle)


def arc_2(t, r, angle):
    perimeter = 2 * math.pi * r
    step_length = perimeter / 360
    for i in range(angle):
        t.fd(step_length)
        t.lt(1)

if __name__ == "__main__":
    bob = turtle.Turtle()
    # square(bob, 50)
    # polygon(bob, 100, 8)
    # circle(bob, 100)
    # circle_2(bob, 100)
    arc(bob, 100, 90)
    # arc_2(bob, 100, 90)
    turtle.mainloop()
