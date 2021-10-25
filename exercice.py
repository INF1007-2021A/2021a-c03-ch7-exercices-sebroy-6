#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
from exercice_ch6 import frequence
from turtle import *


# TODO: Définissez vos fonction ici

def volume_masse_ellipsoide(a=1, b=1, c=1, masse_volumique=1):
    V = (4 / 3)*math.pi * a * b * c
    masse = masse_volumique * V
    return V, masse


def draw_tree(pen_size=6, length=8, angle=30):  # Revoir avec le prof pour savoir comment simplifier la construction du code #3
    # Starting sequence
    penup()
    goto(0, -250)
    pendown()
    left(90)
    length *= 10
    color("BROWN")
    # Starts drawing
    draw_branche(pen_size, length, angle)
    done()

def draw_branche(pen_size, length, angle):  # It goes directly to the deepest node and, when the first (rigth)
    # and second (left) draw_branche(), it goes backwards once and does the second (left) draw_brach() (does this for every node
    # in the tree
    if length > 0 and pen_size > 0:
        pensize(pen_size)
        forward(length)
        right(angle)
        draw_branche(pen_size - 1, length - 10, angle - 5)  # Lignes 36 a 40 : Je n'arrive pas à visualiser le processus
        left(angle * 2)
        draw_branche(pen_size - 1, length - 10, angle - 5)
        right(angle)
        backward(length)


def valide(chaine: str) -> bool:
    for i in range(len(chaine)):
        if chaine[i] not in ["a", "t", "g", "c"]:
            return False
    return True

def saisie(chaine):
    while not valide(chaine):
        print("votre saisie n'est pas valide")
        print("Veuillez saisir une saisie valide:")
        chaine = input()

    return str(chaine)

def proportion():
    print("chaine D'ADN :")
    chaine = saisie(input())

    print("séquence D'ADN :")
    sequence = saisie(input())

    fois_dans_la_chaine = 0

    for i in range(len(chaine)-1):
        if sequence == str(chaine[i] + chaine[i + 1]):
            fois_dans_la_chaine += 1

    return (fois_dans_la_chaine / len(chaine)) * 100, sequence



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    print("Exercice #1:", volume_masse_ellipsoide(10, 8, 6))  # Exercice 1


    most_frequent_letter = lambda texte: list(frequence(texte))[list(frequence(texte).values())
        .index(max(list(frequence(texte).values())))]

    print("Exercice #2:", most_frequent_letter("hello world"))  # Exercice 2

    #draw_tree(6, 10, 30)  # Exercice 3

    rapport, chaine = proportion()
    print("Exercice #4 :", "Il y a {}% de \"{}\"".format(round(rapport, 2), chaine))


