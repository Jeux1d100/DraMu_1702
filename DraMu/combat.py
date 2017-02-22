#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
from entities.ego import *
from entities.fauna import *
from entities.flora import *
from utilities.util import *
from items.item import *

# ego_alea = (1, 4, 9)
# alter_alea = (2, 5, 10)

# ego_off =  (ego.nerf *3 + ego.fluide *2 + ego.chimie + ego.gaz) + (random.choice(ego_alea)) # Offense
# alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))

# ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
# alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))

# ego_dmg =  (ego.fluide *3 + ego.chimie *2 + ego.nerf + ego.gaz) + (random.choice(ego_alea)) # Dommages
# alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))

# ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
# alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))

# def select_alter():
#     alter = (random.choice(FAUNA))
#     print ("            {} (".format(ego.name) + Colour.GREEN + "{}".format(ego.matorg) + Colour.END + "|" + Colour.GREEN + "{}".format(ego.fougue) + Colour.END + ") vs   {} (".format(alter.name) + Colour.GREEN + "{}".format(alter.matorg) + Colour.END + ")")
#     print (" ")
#     print ("    {}".format(alter.desc))

# def do_combat():
#     # select_alter()
#     while 1:
#         if ego.matorg > 1:
#             ego_attack()
#         else:
#             lose()
#             break

#         if alter.matorg > 1:
#             alter_attack()
#         else:
#             win()
#             break

def in_combat():
    alter = (random.choice(FAUNA))
    ego.dead == False
    alter.dead == False
    while ego.dead == False or alter.dead == False:
    # while ego.matorg > 1 and alter.matorg > 1:
        in_arena()
    # alter = (random.choice(FAUNA))
    out_combat()

def out_combat():
    if ego.matorg < 0:
        do_lose()
    else:
        do_win()


def in_arena():
    # ego.dead == False
    # alter.dead == False
    # while ego.dead == False or alter.dead == False:
        # while True:
        clean()
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print (" ")
        print ("            {} (".format(ego.name) + Colour.GREEN + "{}".format(ego.matorg) + Colour.END + "|" + Colour.GREEN + "{}".format(ego.fougue) + Colour.END + ") vs   {} (".format(alter.name) + Colour.GREEN + "{}".format(alter.matorg) + Colour.END + ")")
        print (" ")
        print ("    {}".format(alter.desc))
        print (" ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                                  ")
        print (Colour.CYAN + "   Actions possibles : " + Colour.END)
        print ("      d - attaque directe    *   -5 fougue                                        ")
        print ("      r - attaque rapide     *   + toucher, -10 fougue                            ")
        print ("      l - attaque lourde     *   - toucher, ++ dégâts, -15 fougue                 ")
        print ("      p - attaque précise    *   +++ toucher, +++ dégâts, -25 fougue              ")
        print ("                                                                                  ")
        print ("      a - attendre           *   +10 fougue                                       ")
        print ("                                                                                  ")
        print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("                                                                                  ")
        print (Colour.DARKCYAN + "   Touche Entrée pour une attaque directe" + Colour.END)
        option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
        # ego.dead = False
        # alter.dead = False
        if option == "":
            do_attack_directe()
        elif option =="d":
            do_attack_directe()
        elif option == "a":
            ego_attack_repos()
        else:
            bad_input()
    
        # elif option == "r":
        #     do_attack_rapide()
        # elif option == "l":
        #     do_attack_lourde()
        # elif option == "x":
        #     do_attack_precise()

def do_attack_directe():
    if ego.matorg < 0:
        ego.matorg = 0
        # ego.dead == True
        print ("")
        option = input(Colour.DARKCYAN + "   Ego Perdu - Touche Entrée pour continuer..." + Colour.END)
        out_combat()
    else:
        ego_attack_directe()
        ego.fougue += ego.regen
    if alter.matorg < 0:
        alter.matorg = 0
        # alter.dead == True
        print ("")
        option = input(Colour.DARKCYAN + "   Alter Perdu - Touche Entrée pour continuer..." + Colour.END)
        out_combat()
    else :
        alter_attack()
        print ("")
        option = input(Colour.DARKCYAN + "   Tour Suivant - Touche Entrée pour continuer..." + Colour.END)



def ego_attack_directe():
    print ("Ego attaque directe :")
    # Tout est sur le modèle a*3 + b*2 + c + d + alea. abcd changent d'ordre selon les situations.
    cmbt_ftg = 5 # fatigue de combat, réduit la fougue
    ego_alea = (1, 4, 9)
    alter_alea = (2, 5, 10)
    ego_off =  (ego.nerf *3 + ego.fluide *2 + ego.chimie + ego.gaz) + (random.choice(ego_alea)) # Offense
    alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))
    ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
    alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
    ego_dmg =  (ego.fluide *3 + ego.chimie *2 + ego.nerf + ego.gaz) + (random.choice(ego_alea)) # Dommages
    alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))
    ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
    alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
    # L'ego attaque toujours en premier. Si ego_offense >= alter_def, alors l'ego réussi son attaque. Autrement, l'alter attaque.
    # Si ego_dmg >= alter_res, alors l'ego blesse l'alter. Ensuite c'est au tour de l'alter, et boucle jusqu'à élimination d'un protagoniste.

    print ("")
    ego.fougue -= cmbt_ftg
    print (ego.fougue)
    if ego.fougue > 1:
        if ego_off >= alter_def:
            if (ego_dmg - alter_res) < 1:
                alter.matorg -= 0
                print ("      Vous touchez et n'infligez " + Colour.PURPLE + "aucun dégâts " + Colour.END + "({} vs {}, {} vs {}) !".format(ego_off, alter_def, ego_dmg, alter_res))
            else:
                alter.matorg -= (ego_dmg - alter_res)
                print ("      Vous touchez et infligez " + Colour.GREEN + "{} dégâts ".format(ego_dmg - alter_res) + Colour.END + "à l'alter ({} vs {}, {} vs {}).".format(ego_off, alter_def, ego_dmg, alter_res))
        else:
            print ("      Vous " + Colour.PURPLE + "ratez " + Colour.END + "votre coup ({} vs {}) !".format(ego_off, alter_def))
    else :
        print ("      Trop fatigué")

def alter_attack():
    print ("Alter :")
    # Tout est sur le modèle a*3 + b*2 + c + d + alea. abcd changent d'ordre selon les situations.
    ego_alea = (1, 4, 9)
    alter_alea = (2, 5, 10)
    ego_off =  (ego.nerf *3 + ego.fluide *2 + ego.chimie + ego.gaz) + (random.choice(ego_alea)) # Offense
    alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))
    ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
    alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
    ego_dmg =  (ego.fluide *3 + ego.chimie *2 + ego.nerf + ego.gaz) + (random.choice(ego_alea)) # Dommages
    alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))
    ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
    alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
    # L'ego attaque toujours en premier. Si ego_offense >= alter_def, alors l'ego réussi son attaque. Autrement, l'alter attaque.
    # Si ego_dmg >= alter_res, alors l'ego blesse l'alter. Ensuite c'est au tour de l'alter, et boucle jusqu'à élimination d'un protagoniste.

    if alter_off > ego_def :
        if  (alter_dmg - ego_res) < 1 :
            ego.matorg -= 0
            print ("        Le coup de l'alter est " + Colour.LPURPLE + "sans effet " + Colour.END + "sur vous ({} vs {}, {} vs {}).".format(alter_off, ego_def, alter_dmg, ego_res))
        else :
            ego.matorg -= (alter_dmg - ego_res)
            print ("        L'alter vous blesse pour " + Colour.RED + "{} dégâts.".format(alter_dmg - ego_res) + Colour.END + "({} vs {}, {} vs {}).".format(alter_off, ego_def, alter_dmg, ego_res))

    else :
        print ("        L'alter " + Colour.LPURPLE + "rate " + Colour.END + "son attaque ({} vs {}).".format(alter_off, ego_def))

# def ego_attack_rapide(): # +off (*3 *3 *3 *2), -dmg (*2 *1 *1 *1)
#     cmbt_ftg = 10 # fatigue de combat, réduit la fougue
#     ego_alea = (1, 4, 9)
#     alter_alea = (2, 5, 10)
#     ego_off =  (ego.nerf *3 + ego.fluide *3 + ego.chimie *3 + ego.gaz *2) + (random.choice(ego_alea)) # Offense
#     alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))
#     ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
#     alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
#     ego_dmg =  (ego.fluide *2 + ego.chimie *1 + ego.nerf + ego.gaz) + (random.choice(ego_alea)) # Dommages
#     alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))
#     ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
#     alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))

#     # L'ego attaque toujours en premier. Si ego_offense >= alter_def, alors l'ego réussi son attaque. Autrement, l'alter attaque.
#     # Si ego_dmg >= alter_res, alors l'ego blesse l'alter. Ensuite c'est au tour de l'alter, et boucle jusqu'à élimination d'un protagoniste.

#     ego.fougue -= cmbt_ftg
#     print ("")
#     if ego.fougue >= 0 :
#         if ego_off > alter_def:
#             if (ego_dmg - alter_res) < 1:
#                 alter.matorg -= 0
#                 print ("      Vous frappez trop rapidement et n'infligez " + Colour.PURPLE + "aucun dégât " + Colour.END + "({} vs {}, {} vs {}) !".format(ego_off, alter_def, ego_dmg, alter_res))
#             else:
#                 alter.matorg -= (ego_dmg - alter_res)
#                 print ("      Vous frappez vivement l'alter et lui infligez " + Colour.GREEN + "{} dégâts ".format(ego_dmg - alter_res) + Colour.END + "({} vs {}, {} vs {}).".format(ego_off, alter_def, ego_dmg, alter_res))
#             if alter.matorg < 1:
#                 alter.matorg == 0
#                 print ("")
#                 option = input(Colour.DARKCYAN + "   Touche Entrée pour le tour suivant -> " + Colour.END).lower()
#                 win()
#             else :
#                 alter_attack()
#         else:
#             print ("      Votre empressement vous fait " + Colour.PURPLE + "rater " + Colour.END + "votre cible ({} vs {}) !".format(ego_off, alter_def))
#             alter_attack()
#     else :
#         print ("      Trop fatigué")
#         alter_attack()

# def ego_attack_lourde(): # -off (*2 *1 *1 *1), +dmg (*3 *3 *3 *2)
#     cmbt_ftg = 15 # fatigue de combat, réduit la fougue
#     ego_alea = (1, 4, 9)
#     alter_alea = (2, 5, 10)
#     ego_off =  (ego.nerf *2 + ego.fluide *1 + ego.chimie + ego.gaz) + (random.choice(ego_alea)) # Offense
#     alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))
#     ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
#     alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
#     ego_dmg =  (ego.fluide *3 + ego.chimie *3 + ego.nerf *3 + ego.gaz *2) + (random.choice(ego_alea)) # Dommages
#     alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))
#     ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
#     alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))

#     # L'ego attaque toujours en premier. Si ego_offense >= alter_def, alors l'ego réussi son attaque. Autrement, l'alter attaque.
#     # Si ego_dmg >= alter_res, alors l'ego blesse l'alter. Ensuite c'est au tour de l'alter, et boucle jusqu'à élimination d'un protagoniste.
#     print ("")
#     ego.fougue -= cmbt_ftg
#     if ego.fougue >= 0 :
#         if ego_off > alter_def:
#             if (ego_dmg - alter_res) < 1:
#                 alter.matorg -= 0
#                 print ("      Bien trop maladroite, votre attaque n'inflige " + Colour.PURPLE + "aucun dégât " + Colour.END + "({} vs {}, {} vs {}) !".format(ego_off, alter_def, ego_dmg, alter_res))
#             else:
#                 alter.matorg -= (ego_dmg - alter_res)
#                 print ("      Vous écrasez votre alter et lui infligez " + Colour.GREEN + "{} dégâts ".format(ego_dmg - alter_res) + Colour.END + "({} vs {}, {} vs {}).".format(ego_off, alter_def, ego_dmg, alter_res))
#             if alter.matorg < 1:
#                 alter.matorg == 0
#                 print ("")
#                 option = input(Colour.DARKCYAN + "   Touche Entrée pour le tour suivant -> " + Colour.END).lower()
#                 win()
#             else :
#                 alter_attack()
#         else:
#             print ("      Votre balourdise vous fait " + Colour.PURPLE + "rater " + Colour.END + "votre ennemi ({} vs {}) !".format(ego_off, alter_def))
#             alter_attack()
#     else :
#         print ("      Trop fatigué")
#         alter_attack()

# def ego_attack_precise(): # +++off (*3 *3 *3 *3), +++dmg (*3 *3 *3 *3)
#     cmbt_ftg = 25 # fatigue de combat, réduit la fougue
#     ego_alea = (1, 4, 9)
#     alter_alea = (2, 5, 10)
#     ego_off =  (ego.nerf *3 + ego.fluide *3 + ego.chimie *3 + ego.gaz *3) + (random.choice(ego_alea)) # Offense
#     alter_off = (alter.nerf *3 + alter.fluide *2 + alter.chimie + alter.gaz) + (random.choice(alter_alea))
#     ego_def = (ego.chimie *3 + ego.gaz * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Défense
#     alter_def = (alter.chimie *3 + alter.gaz *2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))
#     ego_dmg =  (ego.fluide *3 + ego.chimie *3 + ego.nerf *3 + ego.gaz *3) + (random.choice(ego_alea)) # Dommages
#     alter_dmg = (alter.fluide *3 + alter.chimie *2 + alter.nerf + alter.gaz) + (random.choice(alter_alea))
#     ego_res = (ego.gaz *3 + ego.chimie * 2 + ego.nerf + ego.fluide) + (random.choice(ego_alea)) # Résistance
#     alter_res = (alter.gaz *3 + alter.chimie * 2 + alter.nerf + alter.fluide) + (random.choice(alter_alea))

#     # L'ego attaque toujours en premier. Si ego_offense >= alter_def, alors l'ego réussi son attaque. Autrement, l'alter attaque.
#     # Si ego_dmg >= alter_res, alors l'ego blesse l'alter. Ensuite c'est au tour de l'alter, et boucle jusqu'à élimination d'un protagoniste.
#     print ("")
#     ego.fougue -= cmbt_ftg
#     if ego.fougue >= 0 :
#         if ego_off > alter_def:
#             if (ego_dmg - alter_res) < 1:
#                 alter.matorg -= 0
#                 print ("      textextexte " + Colour.PURPLE + "aucun dégât " + Colour.END + "({} vs {}, {} vs {}) !".format(ego_off, alter_def, ego_dmg, alter_res))
#             else:
#                 alter.matorg -= (ego_dmg - alter_res)
#                 print ("      Un hurlement précède le choc que vous infligez à l'alter, qui encaisse " + Colour.GREEN + "{} dégâts ".format(ego_dmg - alter_res) + Colour.END + "({} vs {}, {} vs {}).".format(ego_off, alter_def, ego_dmg, alter_res))
#             if alter.matorg < 1:
#                 alter.matorg == 0
#                 print ("")
#                 option = input(Colour.DARKCYAN + "   Touche Entrée pour le tour suivant -> " + Colour.END).lower()
#                 win()
#             else :
#                 alter_attack()
#         else:
#             print ("      textextexte " + Colour.PURPLE + "rater " + Colour.END + "votre ennemi ({} vs {}) !".format(ego_off, alter_def))
#             alter_attack()
#     else :
#         print ("      Trop fatigué")
#         alter_attack()

def ego_attack_repos(): # pas d'attaque, regen fougue
    cmbt_ftg = -10 # consommation négative, donc gain
    ego.fougue -= cmbt_ftg
    ego.fougue += ego.regen   
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    print ("      Vous laissez agir l'alter, le temps de récupérer votre fougue.")
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                                  ")
    alter_attack()
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def do_flee():
    flee_dmg = random.randint(2, 8)
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    print ("      Vous fuyez le combat ! L'alter trouve l'opportunité de vous frapper dans le dos,")
    print ("      et vous blesse pour " + Colour.RED + "{} dégâts".format(flee_dmg) + Colour.END + ".")
    print ("      Vous retournez au village, pour panser plaies et honneur.")
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                                  ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def do_win():
    ego.fougue = ego.maxfougue
    alter.matorg = alter.maxmatorg
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    print ("      Vous gagnez le combat !")
    print ("      Les acclamations de la foule vous vivifient, et votre fougue retrouve son maximum.")
    print ("      Vous retournez au village, prêt pour de nouvelles aventures.")
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                                  ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def do_lose():
    ego.matorg = int(ego.matorg/2)
    ego.fougue = ego.regen
    alter.matorg = alter.maxmatorg
    clean()
    print (ego.matorg)
    print (ego.fougue)
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (" ")
    print ("      Vous perdez le combat !")
    print ("      Vous êtes évacué de l'arène puis jeté dans un trou nauséabond qui sert à canaliser")
    print ("      les eaux usées. Les insectes commencent déjà leurs assauts, et c'est avec peine que")
    print ("      vous rampez jusqu'aux portes du village.")
    print (" ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                                  ")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)
    


# def go_arena():
    # # os.system("clear")
    # print ("Arène")

    # # Au début du tour de l'alter, l'ego regen fougue
    # while ego.fougue < 0 :
    #     ego.fougue = 0
    # if ego.fougue + ego.regen > ego.maxfougue :
    #     ego.fougue = ego.maxfougue
    # else :
    #     ego.fougue += ego.regen

    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print (" ")
    # print ("            {} (".format(ego.name) + Colour.GREEN + "{}".format(ego.matorg) + Colour.END + "|" + Colour.GREEN + "{}".format(ego.fougue) + Colour.END + ") vs   {} (".format(alter.name) + Colour.GREEN + "{}".format(alter.matorg) + Colour.END + ")")
    # print (" ")
    # print ("    {}                                                              ".format(alter.description))
    # print (" ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                                  ")
    # print ("      s - attaque simple     *   -5 fougue                                        ")
    # print ("      r - attaque rapide     *   + toucher, -10 fougue                  ")
    # print ("      l - attaque lourde     *   - toucher, ++ dégâts, -15 fougue       ")
    # print ("      x - attaque précise    *   +++ toucher, +++ dégâts, -25 fougue    ")
    # print ("                                                                                  ")
    # print ("      a - attendre           *   +10 fougue                                       ")
    # print ("                                                                                  ")
    # print ("      f - fuir et abandonner le combat                                            ")
    # print ("                                                                                  ")
    # print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print ("                                                                                  ")
    # print (Colour.DARKCYAN + "   Touche Entrée pour une attaque simple" + Colour.END)
    # option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    # if option == "s":
    #     ego_attack_simple()
    # elif option == "r":
    #     ego_attack_quick()
    # elif option == "l":
    #     ego_attack_heavy()
    # elif option == "x":
    #     ego_attack_sniper()
    # elif option == "a":
    #     ego_attack_wait()
    # elif option =="":
    #     ego_attack_simple()
    # elif option == "f":
    #     do_flee()
    # else:
    #     print("      Ce choix n'est pas valide")
    #     time.sleep(1)
    #     os.system("clear")
    #     go_arena()