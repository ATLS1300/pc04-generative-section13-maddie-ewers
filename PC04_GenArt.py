#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:28:48 2021

@author: maddieewers
"""

"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: MADDIE EWERS

********* HEY, READ THIS FIRST **********

This code will show 7 lines that make up a square shape. 
These 7 lines will then be drawn with an option of 3 different color palletes (Green. Blue, or Purple) by using the random library. 
Running the the code will make the graphic appear in 1 of the 3 color palettes.
Run the code multiple times and a different pallete should appear to make up the image.
"""

import turtle
import math, random


turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 800 # width of panel
h = 800# height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

bluePalette=[(0,51,51), (0,102,102), (0,153,153), (0,204,204), (0,255,255),(51,255,255),(153,255,255)]
greenPalette=[(0,102,0),(0,153,0),(0,204,0),(0,255,0),(102,255,102),(153,255,153),(204,255,204)]
pinkPalette=[(102,0,102),(153,0,153),(204,0,204),(255,0,255),(255,102,255),(255,153,225),(255,204,255)]
allPalettes=[bluePalette,greenPalette,pinkPalette]
pickedPalette=random.choice(allPalettes) # randomly will choose 1 of my 3 palettes to draw with
lineSquare=turtle.Turtle()
lineSquare.pensize(20)
startY=300
num=7
lineSquare.up()
lineSquare.hideturtle()
for i in range(num): # this loop creates the 1st series of 7 lines that make up a square 
    lineSquare.color(pickedPalette[i])
    lineSquare.goto(-300,startY)
    lineSquare.down()
    lineSquare.forward(600)
    lineSquare.up()
    startY-=100
lineSquare.up()
startY=300

    
   
   
    
    
    
    
    
    
    
    
    
    