# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 21:38:37 2016

@author: nikolz
"""
import turtle

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)
       
def draw_circle(x, y, z):
    gotoxy(x, y)
    turtle.circle(z)

turtle.speed(1)     
draw_line(-160, -100, -160, 80)
draw_line(-160, 80, -80, 80)
draw_line(-160, 40, -120, 80)
draw_line(-100, 80, -100, 40)
draw_circle(-100, 0, 20)
draw_line(-100, 0, -100, -50)
draw_line(-100, -10, -120, -20)
draw_line(-100, -10, -80, -20)
draw_line(-100, -50, -120, -60)
draw_line(-100, -50, -80, -60)

gotoxy(-200, 250)
turtle.write('zagadayte chislo ot 1 do 100')

