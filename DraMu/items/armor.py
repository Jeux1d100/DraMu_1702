#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .item import *

class Armor(Item):
    def __init__(self, name, desc, jtsValue, defense, qtt=1):
        Item.__init__(name, desc, jtsValue, qtt)

        self.defense = defense