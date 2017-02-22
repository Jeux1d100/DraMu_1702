#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .character import *
from items.container import *
from utilities.util import *

class Ego(Character):
    def __init__(self, name, nerf, fluide, chimie, gaz):
        Character.__init__(self, name)

        self.nerf = nerf
        self.fluide = fluide
        self.chimie = chimie
        self.gaz = gaz

        self.maxmatorg = (nerf*nerf + fluide*fluide + chimie*chimie + gaz*gaz)
        self.matorg = self.maxmatorg

        self.maxfougue = (self.nerf + self.gaz)*10
        self.fougue = self.maxfougue
        self.regen = (self.fluide + self.chimie)

        self.egobag = Container("Sac")
        self.turnfragment = 3
        self.turn = self.turnfragment*1

    # def die(self):
    #     self.matorg < 0
    #     self.dead = True
    #     input()

ego = Ego("", 3, 3, 3, 3)

# def savegame():
#     import pickle
#     data = {"ego.name" : ego.name}
#     # , ego.nerf, ego.fluide, ego.chimie, ego.gaz, ego.matorg, ego.fougue

#     with open('savefile', 'w') as f:
#         pickle.dump(data, f)

# def loadgame():
#     import pickle
#     with open('savefile') as f:
#         data = pickle.load(f)

def savegame(filename):
    import pickle
    data = {"ego.name" : ego.name,
            "ego.nerf" : ego.nerf,
            "ego.fluide" : ego.fluide,
            "ego.chimie" : ego.chimie,
            "ego.gaz" : ego.gaz,
            "ego.matorg" : ego.matorg,
            "ego.fougue" : ego.fougue
            }

    with open(filename,'wb') as myfile:
        pickle.dump(data,myfile)
 
def loadgame(filename):
    import pickle
    with open(filename,'rb') as myfile:
        data = pickle.load(myfile)
    ego.name = data["ego.name"]
    ego.nerf = data["ego.nerf"]
    ego.fluide = data["ego.fluide"]
    ego.chimie = data["ego.chimie"]
    ego.gaz = data["ego.gaz"]
    ego.matorg = data["ego.matorg"]
    ego.fougue = data["ego.fougue"]

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
    ego.name = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END)
    while not ego.name :
        ego.name = "Vakog"
    clean()

# class Ego(character):
#     def __init__(self, name):
#         self.name = name
#         self.maxhealth = 100
#         self.health = self.maxhealth
#         self.baseattack = 10
#         self.curweap = None

# class Player(character):
#     def __init__(self, name):
#         self.name = name # Nom de l'ego (avatar du joueur)

#         self.nerf = 2 # Cerveau (Action + Agilité)          # a3 + b2 + c 1 + d1 + (a*a or b*b or c*c or d*d) = 7+1 mini à 21+9 maxi
#         self.fluide = 2 # Cœur (Puissance + Résistance)     # Augmenter de 1pt = N+F+C+G+1 matorg
#         self.chimie = 2 # Glande (Pouvoir + Cohésion)       # if matorg = 0 =>, n or f or c or g -= 1
#         self.gaz = 2 # Poumon (Endurance + Résérve)

#         self.maxfougue = (self.nerf + self.gaz)*10 # 
#         self.fougue = self.maxfougue
#         self.regen = (self.fluide + self.chimie) #

#         # self.baseattack = 5 # Attaque de base de l'ego
#         # self.curweap = "Aucune" # Arme équipée, qui s'ajoute à baseattack

#         self.jeto = 1000 # total de Jetons, monnaie du DraMu
#         self.abo = 100 # total d'abonnés, ressource
#         self.safeabo = 1
#         self.matorg = 50 # actuelle Matière Organique, ressource vitale
#         self.maxmatorg = 100

#         self.rubujo = 0 # Total de Rubujoj (déchets), ressource
#         self.serum = 3 # Total de sérum, potion de soin et autre drogues
#         self.inventory = json.load(open("inventory.txt"))

    # def attack(self):
    #     attack = self.baseattack
    #     if self.curweap == "Mains Nues":
    #         attack += 0
    #     return attack

    # def do_attack():
    #     avatar_attack = 5
    #     challenger_attack = 2
    #     mutantversus.select_challenger
    #     challenger.health -= avatar_attack
    #     if challenger.health < 0:
    #         os.system("clear")
    #         win()
    #     else:
    #         ego.health -= challenger_attack
    #         print ("      L'adversaire vous blesse pour %i dégâts !" % challenger_attack)
    #     if ego.health < 0:
    #         lose()
    #     else:
    #         do_attack()

