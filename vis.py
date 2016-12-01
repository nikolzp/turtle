# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 21:38:37 2016

@author: nikolz
"""
import turtle
import random
import sys

x = random.randint(0,100)
print (x)

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
    
def draw_gibbet(step):
    if step == 1:
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        draw_line(-160, 40, -120, 80)
    elif step == 4:    
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        draw_circle(-100, 0, 20)
    elif step == 6:
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        draw_line(-100, -50, -80, -60)

turtle.speed(0) 
turtle.color('green')    

ansver = turtle.textinput("Play", "y/n")
if ansver == "n":
    sys.exit(3)

gotoxy(-200, 250)
turtle.write('Игра виселица zagadayte chislo ot 1 do 100', font=('Arial', 20))

hits = ansver == "y"

tryCount = 0

while True:
    number = turtle.numinput("Try", "Number", 0, 0, 100)
    
    if hits:
        gotoxy(-110, 180 - 12 * tryCount)
        turtle.color('blue')
        if number > x:
            turtle.write("namber меньше" + str(number))
        else:
            turtle.write("namber больше" + str(number))
    
    if number == x:
        gotoxy(-150, 170)
        turtle.color('blue')
        turtle.write("Bingo", font=('Arial', 50))
        break
    else:
        gotoxy(-150, 200)
        turtle.color('blue')
        turtle.write("No")
        tryCount += 1
        draw_gibbet(tryCount)
        
        if tryCount == 10:
            gotoxy(-150, 200)
            turtle.color('blue')
            turtle.write("You loss")
            break




