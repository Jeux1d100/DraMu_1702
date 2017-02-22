#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from entities.player import *
from utilities.util import *

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

def gui_start():
    clean()
    print ("Menu")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.YELLOW + "    DraMu 1702_01 | Développé par Tchey | http://jeux1d100.net" + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      c - continuer la partie sauvegardée                                  ")
    print ("      n - nouvelle partie                                                  ")
    print ("                                                                           ")
    print ("      h - aide                                                             ")
    print ("                                                                           ")
    print ("      q - quitter                                                          ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour commencer une nouvelle partie" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    if option =="n":
        ego_name()
    elif option =="q":
        sys.exit()
    elif option =="h":
        pass
    elif option =="":
        pass
    else:
        pass

def ego_name():
    clean()
    print ("Nom")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Choisissez votre nom. Vous accéderez ensuite à la création de l'ego. ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour le nom par défaut (Vakog)" + Colour.END)
    ego.name = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    while not ego.name :
        ego.name = "Vakog"
    print ("Vous êtes {}".format(ego.name))
    pass