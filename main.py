from math import *
from random import randint
from time import sleep
from turtle import *

colormode(255)

a = 100
n = 4

#hideturtle()

def petit_trapezez(a):
    fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    begin_fill()
    forward(a * 2)
    left(120)
    forward(a)
    for i in range(2):
        left(60)
        forward(a)
    end_fill()
    left(120)

def trapeze(a, n):
    if n == 1:
        petit_trapezez(a)
    #elif n > 1:



def rec(n, a):
    if n == 1:
        penup()
        forward(a*2)
        left(120)
        pendown()
        trapeze(a)
    else:
        penup()
        forward((2**n)*a)
        left(120)
        forward((((2 ** n) * a)/2)-a)
        pendown()
        trapeze(a)
        penup()
        left(180)
        forward((((2 ** n) * a) / 2) - a)
        right(180)
        forward((2 ** n) * a)
        left(180)
        pendown()
        rec(n-1, a)



petit_trapezez(a)
sleep(10000)
