#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Character(object):
    def __init__(self, name):
        self.name = name
        self.description = None

        self.nerf = 0 # Cerveau (Action + Agilité)          # a3 + b2 + c 1 + d1 + (a*a or b*b or c*c or d*d) = 7+1 mini à 21+9 maxi
        self.fluide = 0 # Cœur (Puissance + Résistance)     # Augmenter de 1pt = N+F+C+G+1 matorg
        self.chimie = 0 # Glande (Pouvoir + Cohésion)       # if matorg = 0 =>, n or f or c or g -= 1
        self.gaz = 0 # Poumon (Endurance + Résérve)

        self.maxfougue = (self.nerf + self.gaz)*10 # fougue = fatigue, endurance...
        self.fougue = self.maxfougue
        self.regen = (self.fluide + self.chimie) #

        self.maxmatorg = 50 # Matière Organique, ressource vitale, points de vie
        self.matorg = self.maxmatorg 

        self.dead = False

    def update(self):
        if self.matorg < 0:
            self.matorg = 0
            self.dead = True