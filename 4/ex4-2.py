# encoding: utf-8

import turtle
import math

from mypolygon import polygon

def pie(t, length, n):
    '''

    parm t: turtle
    parm length: 半径
    parm n: 三角形个数
    '''
    angle_vertex = 360.0 / n
    angle_base = (180.0 - angle_vertex) / 2 

    length_base = 2 * length * math.sin(angle_vertex * math.pi / 360)

    for i in range(n):
        t.rt(angle_vertex/2)
        t.fd(length)
        t.lt(180.0 - angle_base)
        t.fd(length_base)
        t.lt(180.0 - angle_base)
        t.fd(length)
        t.left(180.0 - 3 * angle_vertex / 2)

    t.pu()
    t.fd(length*2 + 10)
    t.pd()


bob = turtle.Turtle()
bob.pu()
bob.bk(130)
bob.pd()

pie(bob, 100, 5)
pie(bob, 100, 6)
pie(bob, 100, 7)

bob.hideturtle()
turtle.mainloop()
