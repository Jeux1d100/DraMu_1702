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

class Fauna(Character):
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


muscae = Fauna("Muscae", "* Une mouche grosse comme une main.", 1, 1, 1, 1)
rodentia = Fauna("Rodentia", "* Un lapin aux oreilles percées.", 2, 1, 1, 1)
caninae = Fauna("Caninae", "* Un chien sauvage, affaibli par la faim et la maladie.", 2, 2, 1, 1)
casuariidae = Fauna("Casuariidae", "* Cet imposant oiseau, dont le bec et les longues pattes griffues\n      sont mortels, ne sait pas voler.", 2, 2, 2, 2)
biours = Fauna("BiOurs", "* Cet ours...", 3, 2, 2, 2)
crocaillou = Fauna("Crocaillou", "* Vu de loin, on dirait bien un rocher, et pourtant, il bouge.", 3, 2, 3, 2)
proboscidae = Fauna("Proboscidae", "* Un animal énorme, aussi gras que musclé, avec deux formidables\n      trompes sur la face.", 5, 5, 5, 5)

FAUNA = (muscae, rodentia, caninae, casuariidae, biours, crocaillou, proboscidae)
alter = (random.choice(FAUNA))

def in_fauna():
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.YELLOW + "    Catalogue de la faune" + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    for i in FAUNA:
        print ("   {} ".format(i.name) + Colour.LPURPLE + "{}".format(i.desc) + Colour.END)
        print ("      matorg : " + Colour.RED + "{}".format(i.matorg) + Colour.END + " (n{} f{} c{} g{})".format(i.nerf, i.fluide,i.chimie, i.gaz))
        print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def alea_fauna():

    # for i in FAUNA:
    #     print ("   {} ".format(i.name))
    alea_result = random.randint(1, 20)

    if alea_result in (1, 2, 3):
        fauna = ("      {} ".format(muscae.name) + Colour.LPURPLE + "{}".format(muscae.desc) + Colour.END)
    elif alea_result in (4, 5, 6):
        fauna = ("      {} ".format(rodentia.name) + Colour.LPURPLE + "{}".format(rodentia.desc) + Colour.END)
    elif alea_result in (7, 8, 9):
        fauna = ("      {} ".format(caninae.name) + Colour.LPURPLE + "{}".format(caninae.desc) + Colour.END)
    elif alea_result in (10, 11):
        fauna = ("      {} ".format(casuariidae.name) + Colour.LPURPLE + "{}".format(casuariidae.desc) + Colour.END)
    elif alea_result in (12, 13):
        fauna = ("      {} ".format(biours.name) + Colour.LPURPLE + "{}".format(biours.desc) + Colour.END)
    elif alea_result == (14):
        fauna = ("      {} ".format(crocaillou.name) + Colour.LPURPLE + "{}".format(crocaillou.desc) + Colour.END)
    elif alea_result == (15):
        fauna = ("      {} ".format(proboscidae.name) + Colour.LPURPLE + "{}".format(proboscidae.desc) + Colour.END)
    else:
        fauna = ("      Quelques insectes" + Colour.LPURPLE + " * Sans incidence." + Colour.END)
    print ("      Vous dérangez un spécimen de la faune locale : (1d20 = {})".format(alea_result))
    print (fauna)

# num_to_select = 2 # set the number to select here.
# list_of_random_items = random.sample(BESTIARY, num_to_select)
# first_random_item = list_of_random_items[0]
# second_random_item = list_of_random_items[1]

# def choix_bestiary():
#     global adversaire
#     # for i in bestiary.BESTIARY:
#     #     print ("oui !")
#     adversaire_type = random.randint(1, 99)
#     if adversaire_type in range(1, 29):
#         adversaire = bestiary.lutin_active
#     if adversaire_type in range(30, 49):
#         adversaire = bestiary.gobelin_active
#     if adversaire_type in range(50, 64):
#         adversaire = bestiary.orc_active
#     if adversaire_type in range(65, 89):
#         adversaire = bestiary.ogre_active
#     if adversaire_type in range(90, 99):
#         adversaire = bestiary.troll_active
#     ui_attaq()
