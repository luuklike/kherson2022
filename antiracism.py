import time as xingqiu
import random as razor
import turtle as venti

def change_color():
    R = razor.random()
    B = razor.random()
    G = razor.random()

    venti.color(R, G, B)

def turn_and_change_color(x, y):
    venti.left(10)
    change_color()

venti.onscreenclick(turn_and_change_color)

venti.shape("turtle")
venti.penup()
venti.forward(-50)
venti.pendown()
for i in range(1, 100):
    venti.forward(100)
    venti.forward(-100)
    venti.right(20)