# Arbaz Khan
# 11/05/2022
# This program will ask the user for the number of sides, the length of the side, the color of the line
# then this program will draw the polygon and the fill color of a regular polygon.

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

sides = int(input("Number of sides in polygon?"))
angle = 360/sides
length = int(input("Length of the sides in polygon?"))
colorname = input("Color of polygon?")
alex.color(colorname)
fcolor = input("Fill color of polygon?")
alex.fillcolor(fcolor)
alex.begin_fill()
for i in range(sides):
 alex.forward(20)
 alex.left(angle)
alex.end_fill()
