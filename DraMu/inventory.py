#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utilities.util import *
from entities.ego import *

class Item(object):
    def __init__(self, name, desc, jtsValue, qtt=1):
        self.name = name
        self.raw = name.strip().lower()
        self.qtt = qtt # quantity
        self.jtsValue = jtsValue
        self.netValue = qtt * jtsValue

    def recalc(self):
        self.netValue = self.qtt * self.jtsValue

class Container(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.inside = {}

    def __iter__(self):
        return iter(self.inside.items())

    def __len__(self):
        return len(self.inside)

    def __contains__(self, item):
        return item.raw in self.inside

    def __getitem__(self, item):
        return self.inside[item.raw]

    def __setitem__(self, item, jtsValue):
        self.inside[item.raw] = jtsValue
        return self[item]

    def add(self, item, qtt=1):
        if qtt < 0:
            raise ValueError("Quantité négative, utilisez remove()")
        
        if item in self:
            self[item].qtt += qtt
            self[item].recalc()
        else:
            self[item] = item

    def remove(self, item, qtt=1):
        if item not in self:
            raise KeyError("Objet pas dans le contenant")
        if qtt < 0:
            raise ValueError("Quantité négative, utilisez add()")

        if self[item].qtt <= qtt:
            del self.inside[item.raw]
        else:
            self[item].qtt -= qtt
            self[item].recalc()

egobag = Container("Sac", "Un sac en peau")

fleur_rouge = Item("Fleur Rouge", "Une fleur de couleur rouge", 3)
rubujo = Item("Rubujo", "", 20)
jeton = Item("Jeton", "", 1, 1200)

egobag.add(fleur_rouge)
egobag.add(jeton)

# print (rubujo in egobag)
# print (jeton in egobag)

# print(len(egobag))

# for name, item in egobag:
#     print (item.name, item.qtt)

def in_sac():
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.YELLOW + "    Contenu du sac" + Colour.END)
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    for name, item in ego.egobag:
        print("   {} x{}".format(item.name, item.qtt))
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def purchase(*items):
    for item in items:
        if item.jtsValue > egobag[jeton].qtt:
            print ("   Il vous manque {} jetons.".format(item.jtsValue))
        else:
            egobag.remove(jeton, item.jtsValue)
            egobag.add(item)
            print ("   Vous achetez l'objet {} pour {} JTS.".format(item.name, item.jtsValue))

def loot(*items):
    for item in items:
        alterbag.remove(item)
        egobag.add(item)
        print ("   Vous trouvez ceci : {}".format(item.name))

# print ("")
# print (egobag[jeton].qtt)
# purchase(rubujo, fleur_rouge)
# print (egobag[jeton].qtt)