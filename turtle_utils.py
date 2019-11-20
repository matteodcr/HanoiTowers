from turtle import *

def tourner_droite():
    right(90)

def tourner_gauche():
    left(90)

def rect(cote_a, cote_b):
    for i in range(0,2):
        forward(cote_a)
        tourner_gauche()
        forward(cote_b)
        tourner_gauche()