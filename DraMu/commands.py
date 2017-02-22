#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sac(player, args):
    for name, item in player.egobag:
        print("{} x{}".format(item.name, item.quantity))

def exit(player, args):
    player.die("Merci d'avoir testé DraMu !")

def do_quit():
    clean()
    sys.exit("Merci d'avoir terté DraMu !")