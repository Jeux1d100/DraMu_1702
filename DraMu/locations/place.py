#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utilities.util import *
from entities.ego import *
from entities.fauna import *
from entities.flora import *
from inventory import *
from combat import *

class Place(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

        self.nord = None
        self.sud = None
        self.est = None
        self.ouest = None

    def connect(self, nord=None, sud=None, est=None, ouest=None):
        self.nord = nord
        if nord:
            nord.sud = self
        self.sud = sud
        if sud:
            sud.nord = self
        self.est = est
        if est:
            est.ouest = self
        self.ouest = ouest
        if ouest:
            ouest.est = self

d10 = Place("Forêt", "* Une forêt jeune, à la végétation aérée.")
d11 = Place("Collines", "Des collines et amas rochers.")
d12 = Place("Lac", "* Un lac aux reflets clairs accueille les eaux descendues des glaciers visibles au loin.")

e10 = Place("Forêt", "* Une forêt jeune, à la végétation aérée.")
e11 = Place("Antre", "* Une cavité creusée par une explosion d'une force inouïe, il y a bien longtemps.")
e12 = Place("Village", "* Une palissade de tôles et de débris divers protège ce qui semble être un village.")

f10 = Place("Montagnes", "* Une grandiose chaîne montagneuse condamne le regard à l'extase.")
f11 = Place("Ruines", "* Les ruines d'une civilisation autrefois florissante.")
f12 = Place("Ruines", "* Une prairie sauvage s'offre aux vents.")

rien = Place("Rien", "* Il n'y a rien d'intéressant dans cette direction...")

def in_d10():
    while True:
        clean()
        d10.connect(rien, e10, d11, rien)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes dans une forêt à flanc de montagne.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(d10.nord.name) + Colour.LPURPLE + "{}".format(d10.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(d10.sud.name) + Colour.LPURPLE + "{}".format(d10.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(d10.est.name) + Colour.LPURPLE + "{}".format(d10.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(d10.ouest.name) + Colour.LPURPLE + "{}".format(d10.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            bad_input()
        elif option == "s":
            in_e10()
        elif option == "e":
            in_d11()
        elif option =="o":
            bad_input()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_d11():
    while True:
        clean()
        d11.connect(rien, e11, d12, d10)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Des collines.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(d11.nord.name) + Colour.LPURPLE + "{}".format(d11.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(d11.sud.name) + Colour.LPURPLE + "{}".format(d11.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(d11.est.name) + Colour.LPURPLE + "{}".format(d11.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(d11.ouest.name) + Colour.LPURPLE + "{}".format(d11.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            bad_input()
        elif option == "s":
            in_e11()
        elif option == "e":
            in_d12()
        elif option =="o":
            in_d10()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_d12():
    while True:
        clean()
        d12.connect(rien, e12, rien, e11)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Un lac.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(d12.nord.name) + Colour.LPURPLE + "{}".format(d12.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(d12.sud.name) + Colour.LPURPLE + "{}".format(d12.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(d12.est.name) + Colour.LPURPLE + "{}".format(d12.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(d12.ouest.name) + Colour.LPURPLE + "{}".format(d12.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            bad_input()
        elif option == "s":
            in_e12()
        elif option == "e":
            bad_input()
        elif option =="o":
            in_d11()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_e10():
    while True:
        clean()
        e10.connect(d10, f10, e11, rien)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes dans une forêt avec une magnifique description.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(e10.nord.name) + Colour.LPURPLE + "{}".format(e10.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(e10.sud.name) + Colour.LPURPLE + "{}".format(e10.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(e10.est.name) + Colour.LPURPLE + "{}".format(e10.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(e10.ouest.name) + Colour.LPURPLE + "{}".format(e10.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("      x                                                                     ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_d10()
        elif option == "s":
            in_f10()
        elif option == "e":
            in_e11()
        elif option == "o":
            bad_input()
        elif option == "x":
            bad_input()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_e11():
    while True:
        clean()
        e11.connect(nord=d11, sud=f11, est=e12, ouest=e10)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes {}".format(ego.name))
        print ("      Matorg " + Colour.GREEN + "{} ".format(ego.matorg) + Colour.END + "| " + Colour.GREEN + "{} ".format(ego.fougue) + Colour.END + "Fougue")
        print ("                                                                           ")
        print ("      Temps : {} heure(s), {} jour(s), {} saison(s), {} année(s)".format(ego.turn, int(ego.turn/24), int(ego.turn/(24*90)), int(ego.turn/(24*90*4))))
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      m - développer une mutation ")
        print ("      x - préparer une expédition ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(e11.nord.name) + Colour.LPURPLE + "{}".format(e11.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(e11.sud.name) + Colour.LPURPLE + "{}".format(e11.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(e11.est.name) + Colour.LPURPLE + "{}".format(e11.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(e11.ouest.name) + Colour.LPURPLE + "{}".format(e11.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("      y - sauver                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "m":
            bad_input()
        elif option == "x":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_d11()
        elif option == "s":
            in_f11()
        elif option == "e":
            in_e12()
        elif option =="o":
            explored == False
            in_e10()
        elif option == "?":
            in_aide()
        elif option == "y":
            savegame("Test")
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_e12():
    while True:
        clean()
        e12.connect(d12, f12, rien, e11)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Vous êtes dans un village.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      c - combattre dans l'arène")
        print ("      b - entrer dans la boutique")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(e12.nord.name) + Colour.LPURPLE + "{}".format(e12.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(e12.sud.name) + Colour.LPURPLE + "{}".format(e12.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(e12.est.name) + Colour.LPURPLE + "{}".format(e12.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(e12.ouest.name) + Colour.LPURPLE + "{}".format(e12.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "":
            in_combat()
            alter = None
            continue
        elif option == "c":
            in_combat()
            continue
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_d12()
        elif option == "s":
            in_f12()
        elif option == "e":
            bad_input()
        elif option =="o":
            in_e11()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_f10():
    while True:
        clean()
        f10.connect(e10, rien, f11, rien)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Une longue falaise barre l'accès aux montagnes.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(f10.nord.name) + Colour.LPURPLE + "{}".format(f10.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(f10.sud.name) + Colour.LPURPLE + "{}".format(f10.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(f10.est.name) + Colour.LPURPLE + "{}".format(f10.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(f10.ouest.name) + Colour.LPURPLE + "{}".format(f10.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_e10()
        elif option == "s":
            bad_input()
        elif option == "e":
            in_f11()
        elif option =="o":
            bad_input()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_f11():
    while True:
        clean()
        f11.connect(e11, rien, f12, f10)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Science sans conscience n'est que ruine de l'âme.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(f11.nord.name) + Colour.LPURPLE + "{}".format(f11.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(f11.sud.name) + Colour.LPURPLE + "{}".format(f11.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(f11.est.name) + Colour.LPURPLE + "{}".format(f11.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(f11.ouest.name) + Colour.LPURPLE + "{}".format(f11.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_e11()
        elif option == "s":
            bad_input()
        elif option == "e":
            in_f12()
        elif option =="o":
            in_f10()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()

def in_f12():
    while True:
        clean()
        f12.connect(e12, rien, rien, f11)
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print ("      Les ruines de la civilisation continuent au sud du village.")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Rencontres : " + Colour.END)
        print ("      !!!")
        alea_fauna()
        print ("      !!!")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Spécificités du lieu : " + Colour.END)
        print ("      ")
        print ("      ")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      i - consulter l'inventaire")
        print ("      f - catalogue de la faune")
        print ("      p - catalogue de la flore")
        print ("                                                                           ")
        print (Colour.CYAN + "   Voyager : " + Colour.END)
        print ("      n - Au nord : {} ".format(f12.nord.name) + Colour.LPURPLE + "{}".format(f12.nord.desc) + Colour.END)
        print ("      s - Au sud : {} ".format(f12.sud.name) + Colour.LPURPLE + "{}".format(f12.sud.desc) + Colour.END)
        print ("      e - À l'est : {} ".format(f12.est.name) + Colour.LPURPLE + "{}".format(f12.est.desc) + Colour.END)
        print ("      o - À l'ouest : {} ".format(f12.ouest.name) + Colour.LPURPLE + "{}".format(f12.ouest.desc) + Colour.END)
        print ("                                                                           ")
        print (Colour.CYAN + "   Autres : " + Colour.END)
        print ("      ? - ouvrir une page d'aide ")
        print ("      q - quitter DraMu")
        print ("                                                                           ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                           ")
        print (Colour.DARKCYAN + "   Tapez la lettre correpondant à votre action, puis Entrée" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        if option == "c":
            bad_input()
        elif option == "b":
            bad_input()
        elif option == "i":
            in_sac()
            clean()
            continue
        elif option == "f":
            in_fauna()
            clean()
            continue
        elif option == "p":
            in_flora()
            clean()
            continue
        elif option == "n":
            in_e12()
        elif option == "s":
            bad_input()
        elif option == "e":
            bad_input()
        elif option =="o":
            in_f11()
        elif option == "?":
            in_aide()
        elif option == "q": #arrêter le programme et sortir
            do_quit()
        else:
            bad_input()