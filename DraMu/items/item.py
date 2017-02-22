#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name, desc, jtsValue, qtt=1):
        self.name = name
        self.raw = name.strip().lower()
        self.qtt = qtt # Quantity
        self.jtsValue = jtsValue
        self.netValue = qtt * jtsValue

    def recalc(self):
        self.netValue = self.qtt * self.jtsValue

fleur_rouge = Item("Fleur Rouge", "Une fleur de couleur rouge", 3)
rubujo = Item("Rubujo", "", 20)
jeton = Item("Jeton", "", 1, 1200)

