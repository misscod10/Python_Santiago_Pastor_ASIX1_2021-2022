#!/usr/bin/python
"""
    turtle_square.py
    Demostració de l'ús de Turtle dibuixant un quadrat
"""
import turtle
import math
tortuga = turtle.Pen()
tortuga.color('red')
tortuga.forward(100)
tortuga.left(90)
tortuga.color('blue')
tortuga.forward(100)
tortuga.left(90)
tortuga.color('red')
tortuga.forward(100)
tortuga.left(90)
tortuga.color('blue')
tortuga.forward(100)
tortuga.left(135)
tortuga.color('green')
tortuga.forward(math.sqrt((100**2)+(100**2)))
input()
