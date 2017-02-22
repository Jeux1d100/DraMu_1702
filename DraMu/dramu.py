#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Main game file

import sys
import os
from entities.ego import *
from entities.fauna import *
from entities.flora import *
from utilities.util import *
from items.item import *
from locations.place import *

# def savegame():
#     import pickle
#     data = {ego.name, ego.nerf, ego.fluide, ego.chimie, ego.gaz, ego.matorg, ego.fougue}

#     with open('savefile', 'w') as f:
#         pickle.dump(data, f)

# def loadgame():
#     import pickle
#     data = {ego.name, ego.nerf, ego.fluide, ego.chimie, ego.gaz, ego.matorg, ego.fougue}

#     with open('savefile') as f:
#         data = pickle.load(f)


def main():
    gui_start()
    while not ego.dead:
        in_e11()

def tagoj(): # passage du temps
    ego.turn += 3

def gui_start():
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      ,------.                 ,--.   ,--.        ")
    print ("      |  .-.  \ ,--.--. ,--,--.|   `.'   |,--.,--.")
    print ("      |  |  \  :|  .--'' ,-.  ||  |'.'|  ||  ||  |")
    print ("      |  '--'  /|  |   \ '-'  ||  |   |  |'  ''  '")
    print ("      `-------' `--'    `--`--'`--'   `--' `----' ")
    print (Colour.YELLOW + "          d r a m a t u r g i e   m u t a n t e" + Colour.END)
    print ("                                                                           ")
    print ("   v1702_01 | Développé par Tchey | http://jeux1d100.net")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      Vous êtes une entité singulière, et étrangère à cette planète sur laquelle votre capsule")
    print ("   vient de vous écraser. Destiné à servir de curieux amusement pour un seigneur des étoiles,")
    print ("   voici peut-être l'opportunité d'assumer la liberté pour la première fois.")
    print ("                                                                           ")
    print ("      Après avoir littéralement suinté hors des débris, vous avez glissé votre masse informe")
    print ("   jusqu'à une cavité située dans un escarpement rocheux. La terre environnante semble désolée.")
    print ("   Pourtant, vous percevez les restes d'une civilisation autrefois probablement glorieuse,")
    print ("   en témoignent les ruines qui entourent la capsule.")
    print ("                                                                           ")
    print ("      Terre désolée, mais non désertée. Au loin, dans la direction où l'unique soleil jaune pâle")
    print ("   entame escalade l'horizon pour émenger, il semble y avoir un village fortifié, fait d'un amoncellement")
    print ("   hétérogène d'éléments de récupération. De l'autre côté, le ciel encore sombre dévoile avec peine")
    print ("   les reliefs d'une forêt, et plus loin, de hauts sommets imprenables.")
    print ("                                                                           ")
    print ("       Au sud s'étalent les ruines de la civilisation, tandis qu'au nord collines et amas rocheux")
    print ("   se perdent dans un horizon montagneux.")
    print ("                                                                           ")
    print ("      Qui sait ce que réserve l'avenir ? Vous pourriez ne pas voir l'aube prochaine, ou")
    print ("   tout aussi bien dominer cette planète et ses habitants primitifs dans un futur lointain...")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print ("      c - continuer la partie sauvegardée                                  ")
    print ("      n - nouvelle partie                                                  ")
    print ("                                                                           ")
    print ("      ? - aide                                                             ")
    print ("                                                                           ")
    print ("      q - quitter                                                          ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                                                                           ")
    print (Colour.DARKCYAN + "   Touche Entrée pour commencer une nouvelle partie" + Colour.END)
    option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
    if option =="":
        ego_name()
    elif option =="n":
        ego_name()
    elif option =="q":
        do_quit()
    elif option =="?":
        in_aide()
    elif option =="c":
        loadgame("Test")
    else:
        bad_input()

# def ego_name():
#     clean()
#     print ("Nom")
#     print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print ("                                                                           ")
#     print ("      Choisissez votre nom. Vous accéderez ensuite à la création de l'ego. ")
#     print ("                                                                           ")
#     print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print ("                                                                           ")
#     print (Colour.DARKCYAN + "   Touche Entrée pour le nom par défaut (Vakog)" + Colour.END)
#     ego.name = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()
#     while not ego.name :
#         ego.name = "Vakog"
#     clean()

def turn_more(): # A VOIR A VOIR A VOIR A VOIR !!!
    # years = int((ego.turn*24*7*52)/8736)
    # months = ego.turn*24*7
    # hours, remainder = divmod(ego.turn, 3600)
    # print ("{} {} {}".format(years, months, hours))
    # # result: 3:43:40
    print ("{}".format(ego.turn))

# def in_antre():
#     clean()
#     while True:
#         # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[0][1][1]):
#         #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
#         # for indice, description in sorted(ego.inventory.items(), key=lambda x: x[1][1][1]):
#         #     print ("      {0:} - {1:10} JTS {2:} ({3:})".format(indice, description[0], description[1], description[2]))
#         print ("Antre")
#         print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print ("                                                                           ")
#         print ("      Vous êtes {}, le zum' du jour.".format(ego.name))
#         print ("      Matorg " + Colour.GREEN + "{} ".format(ego.matorg) + Colour.END + "| " + Colour.GREEN + "{} ".format(ego.fougue) + Colour.END + "Fougue")
#         print ("                                                                           ")
#         print ("      Temps : {} heure(s), {} jour(s), {} saison(s), {} année(s)".format(ego.turn, int(ego.turn/24), int(ego.turn/(24*90)), int(ego.turn/(24*90*4))))
#         turn_more()
#         print ("                                                                           ")
#         print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print ("                                                                           ")
#         print ("      c - combattre dans l'arène " + Colour.LPURPLE + "* l'organisation décline toute responsabilité en cas de sinistre" + Colour.END)
#         print ("      b - entrer dans la boutique " + Colour.LPURPLE + "* matériel non certifié" + Colour.END)
#         print ("      m - développer une mutation " + Colour.LPURPLE + "* science expérimentale, résultats non garantis" + Colour.END)
#         print ("      x - préparer une expédition " + Colour.LPURPLE + "* selon les dernières observations en date du [NO DATA]" + Colour.END)
#         print ("      i - consulter l'inventaire " + Colour.LPURPLE + "* synchronisation aux serveurs sous réserve" + Colour.END)
#         print ("      f - catalogue de la faune " + Colour.LPURPLE + "* régimes alimentaires en étude" + Colour.END)
#         print ("      o - catalogue de la flore " + Colour.LPURPLE + "* risques allérgènes non documentés" + Colour.END)
#         print ("                                                                           ")
#         print ("      ? - ouvrir une page d'aide " + Colour.LPURPLE + "* sources anonymes, informations non contractuelles" + Colour.END)
#         print ("                                                                           ")
#         print ("      q - quitter DraMu " + Colour.LPURPLE + "* assistance psychomédicale à la charge de l'utilisateur" + Colour.END)
#         print ("                                                                           ")
#         print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         print ("                                                                           ")
#         print (Colour.DARKCYAN + "   Touche Entrée pour combattre dans l'arène" + Colour.END)
#         option = input(Colour.DARKCYAN + "   Votre choix -> " + Colour.END).lower()

#         if option == "":
#             pass
#         #     if ego.jeto >= taxe :
#         #         ego.jeto -= taxe
#         #         select_challenger()
#         #     else :
#         #         option = input(Colour.DARKCYAN + "   Vous ne pouvez pas vous acquitter de la taxe universelle d'organisation. " + Colour.END).lower()
#         #         in_antre()
#         # elif option == "c":
#         #     if ego.jeto >= taxe :
#         #         ego.jeto -= taxe
#         #         select_challenger()
#         #     else :
#         #         option = input(Colour.DARKCYAN + "   Vous ne pouvez pas vous acquitter de la taxe universelle d'organisation. " + Colour.END).lower()
#         #         in_antre()
#         # elif option == "b":
#         #     go_shop()
#         # elif option == "m":
#         #     go_mutation_prepare()
#         # elif option == "x":
#         #     go_expedition_prepare()
#         elif option == "i":
#             sac()
#             clean()
#             continue
#         elif option == "f":
#             go_fauna()
#             tagoj()
#             clean()
#             continue
#         elif option == "o":
#             go_flora()
#             tagoj()
#             clean()
#             continue
#         # elif option == "?":
#         #     go_help()
#         elif option == "q": #arrêter le programme et sortir
#             do_quit()
#         else:
#             print("      Ce choix n'est pas valide")



if __name__ == '__main__':
	main()