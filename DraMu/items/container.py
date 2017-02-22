#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Container(object):
    def __init__(self, name):
        self.name = name
        self.description = ""
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

