from turtle import *
from random import randint
colormode(255)
speed(0)
def random_color():
    red= randint(0,255)
    green= randint(0,255)
    blue= randint(0,255)
    color(red , green ,blue)
    
def random_pos():
    penup()   
    x=randint(-600,600)
    y=randint(-400,400) 
    goto(x ,y)
    pendown()

def rectangle():
    length=randint(100,200)
    width=randint(100,200)
    begin_fill()
    for a in range(2):
        fd(length)
        rt(90)
        fd(width)
        rt(90)
    end_fill()

def circle():
    size=randint(20,120)
    dot(size)

def generate():
    for shape in range(60):
        random_color()
        random_pos()
        rectangle()
        random_pos()
        random_color()
        circle()
        random_pos()
        random_color()