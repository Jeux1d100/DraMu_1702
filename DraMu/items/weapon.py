#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import *
import random

class Weapon(Item):
    def __init__(self, name, desc, jtsValue, damage, qtt=1):
        Item.__init__(name, desc, jtsValue, qtt)

        self.minDMG = damage[0] # première valeur d'un tuple, comme (5, 9)
        self.maxDMG = damage[1] # seconde valeur, ici : 9

    def damage(self):
        return random.randint(self.minDMG, self.maxDMG)

# class WeaponEnchanted(Weapon):
#     def __init__(self, name, desc, jtsValue, damage, effects, qtt=1):
#         Weapon.__init__(name, desc, jtsValue, qtt, damage)

#     self.effects = effects

items = [
    Weapon("Dague en verre", "dadadague", 25, (7, 12)),
    Weapon("Laser de la mort", "Un laser qui tue la mort", 500, (99, 999))
]

