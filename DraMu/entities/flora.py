#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from .character import *
from utilities.util import *

# Fatigue = nerf + gaz
# Regen = fluide + chimie

class Colour:
    BLACK = "\033[98m"
    LGREY = "\033[97m"
    LPURPLE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

class Flora(Character):
    def __init__(self, name, desc, nerf, fluide, chimie, gaz):
        Character.__init__(self, name)

        self.name = name
        self.desc = desc

        self.nerf = nerf
        self.fluide = fluide
        self.chimie = chimie
        self.gaz = gaz

        self.maxmatorg = (nerf*nerf + fluide*fluide + chimie*chimie + gaz*gaz)
        self.matorg = self.maxmatorg

        self.baseattack = 1

magnoliale = Flora("Magnoliale", "* Plante verte à fleur blanche.", 1, 1, 1, 1)
liliale = Flora("Liliale", "* Petite fleur mauve.", 1, 1, 1, 1)
zingiberale = Flora("Zingiberale", "* Une grosse grappe rouge au milieu de larges feuilles vertes.", 1, 1, 1, 1)
proteale = Flora("Proteale", "* Une petite touffe pourpre hirsute.", 1, 1, 1, 1)
gunnerale = Flora("Gunnerale", "* Imposant bouquet aux larges feuilles sur longues tiges.", 1, 1, 1, 1)
cucurbitale = Flora("Cucurbitale", "* Un cœur jaune éclatant.", 1, 1, 1, 1)
zygophyllale = Flora("Zygophyllale", "* Quelques timides fleurs rouges posées sur de longs bras feuillues.", 1, 1, 1, 1)
geraniale = Flora("Geraniale", "* Petite fleur violette.", 1, 1, 1, 1)
malvale = Flora("Malvale", "* Grande fleur mauve au cœur sombre.", 1, 1, 1, 1)
myrtale = Flora("Myrtale", "* Des mèches écarlates s'échappent d'une pigne.", 1, 1, 1, 1)
ericale = Flora("Ericale", "* Un dense bouquet de fleurs roses et blanches.", 1, 1, 1, 1)
asterale = Flora("Asterale", "* Fleur à cœur jaune et multiples pétales mauves.", 1, 1, 1, 1)
oxalidale = Flora("Oxalidale", "* Fleur blanche tombante, aux veines sombres.", 1, 1, 1, 1)



FLORA = (asterale, cucurbitale, ericale, geraniale, gunnerale, liliale, magnoliale, malvale, myrtale, oxalidale, proteale, zingiberale, zygophyllale)

def in_flora():
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.YELLOW + "    Catalogue de la flore" + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    for i in FLORA:
        print ("   {} ".format(i.name) + Colour.LPURPLE + "{}".format(i.desc) + Colour.END)
        print ("      matorg : " + Colour.RED + "{}".format(i.matorg) + Colour.END + " (n{} f{} c{} g{})".format(i.nerf, i.fluide,i.chimie, i.gaz))
        print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)