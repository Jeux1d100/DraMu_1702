#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Colour:
    BLACK = "\033[98m"
    LGREY = "\033[97m"
    LPURPLE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def bad_input(chronos=0.5):
    import time
    print("   Ce choix n'est pas valide")
    time.sleep(chronos)

def pause(chronos=1):
    import time
    time.sleep(chronos)

def clean(lines=8):
    import os

    if os.name == "posix" :
        os.system("clear")
        print("")
    elif os.name in ("nt", "dos", "ce"):
        os.system("CLS")
        print("")
    else:
        print("\n" * lines)
        print("")

def yes_or_no(prompt="(O/N) ?"):
    while 1:
        answer = input(prompt)
        answer = answer.strip()
        answer = answer.lower()

        oui = ["oui", "o"]
        non = ["non", "n"]

        if answer in oui:
            return True
        elif answer in non:
            return False
        else:
            continue
            
    return False

def do_quit():
    import sys
    clean()
    print("")
    sys.exit("   Merci d'avoir testé DraMu !\n")

def in_aide():
    clean()
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    print ("      Page d'aide                                                          ")
    print ("")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    print (Colour.YELLOW + "      Vocabulaire et termes employés                       " + Colour.END)
    print ("                                                                           ")
    print ("        Zum', rubujo... sont des mots en langue espéranto (http://esperanto-france.org/)     ")
    print ("        Zumo = bourdonnement, utilisé au ici au sens de ""buzz sur internet""  ")
    print ("        Rubujo = dêchet, rebu, poubelle. Utilisé pour nommer une ressource, des bidules de récupération...")
    print ("                                                                           ")
    print (Colour.YELLOW + "      Règles du jeu                                        " + Colour.END)
    print ("                                                                           ")
    print ("        Combattez dans l'arène pour gagner des abonnés et des jetons.      ")
    print ("        A chaque victoire, vous assimilez la matorg de l'alter,       ")
    print ("        ce qui permet de régénérer. A chaque défaite, vous en perdez.      ")
    print ("                                                                           ")
    print ("        Si vous n'avez plus de matorg, mais que vous êtes populaire,       ")
    print ("        certains abonnés se sacrifient pour vous permettre de vivre.       ")
    print ("                                                                           ")
    print ("        Si vous n'avez ni matorg, ni abonnés, c'est la fin du zum',        ")
    print ("        il est temps de laisser la place à un nouveau mutant.              ")
    print ("                                                                           ")
    print ("        Jetons, rubujoj, mutations... feront l'objet de prochaines         ")
    print ("        mises à jour.                                                      ")
    print ("                                                                           ")
    print ("                                                       - en construction - ")
    print ("                                                                           ")
    print ("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("")
    option = input(Colour.DARKCYAN + "   Touche Entrée pour continuer..." + Colour.END)

def dra_mu():

    print ("   ####    #####   #####   #   #   #   #")
    print ("   #   #   #   #   #   #   ## ##   #   #")
    print ("   #   #   #####   #####   ## ##   #   #")
    print ("   #   #   #  #    #   #   # # #   #   #")
    print ("   ####    #   #   #   #   #   #   #####")
    print("")
    print ("   @@@@    @@@@@   @@@@@   @   @   @   @")
    print ("   @   @   @   @   @   @   @@ @@   @   @")
    print ("   @   @   @@@@@   @@@@@   @@ @@   @   @")
    print ("   @   @   @  @    @   @   @ @ @   @   @")
    print ("   @@@@    @   @   @   @   @   @   @@@@@")
    print("")
    print ("   ++++    +++++   +++++   +   +   +   +")
    print ("   +   +   +   +   +   +   ++ ++   +   +")
    print ("   +   +   +++++   +++++   ++ ++   +   +")
    print ("   +   +   +  +    +   +   + + +   +   +")
    print ("   ++++    +   +   +   +   +   +   +++++")
    print("")
    print ("   ~~~~    ~~~~~   ~~~~~   ~   ~   ~   ~")
    print ("   ~   ~   ~   ~   ~   ~   ~~ ~~   ~   ~")
    print ("   ~   ~   ~~~~~   ~~~~~   ~~ ~~   ~   ~")
    print ("   ~   ~   ~  ~    ~   ~   ~ ~ ~   ~   ~")
    print ("   ~~~~    ~   ~   ~   ~   ~   ~   ~~~~~")
    print("")
    print ("   ||||    |||||   |||||   |   |   |   |")
    print ("   |   |   |   |   |   |   || ||   |   |")
    print ("   |   |   |||||   |||||   || ||   |   |")
    print ("   |   |   |  |    |   |   | | |   |   |")
    print ("   ||||    |   |   |   |   |   |   |||||")
    print("")
    print ("   ====    =====   =====   =   =   =   =")
    print ("   =   =   =   =   =   =   == ==   =   =")
    print ("   =   =   =====   =====   == ==   =   =")
    print ("   =   =   =  =    =   =   = = =   =   =")
    print ("   ====    =   =   =   =   =   =   =====")
    print("")
    print ("   ****    *****   *****   *   *   *   *")
    print ("   *   *   *   *   *   *   ** **   *   *")
    print ("   *   *   *****   *****   ** **   *   *")
    print ("   *   *   *  *    *   *   * * *   *   *")
    print ("   ****    *   *   *   *   *   *   *****")
    print("")
    print ("      XXXX     XXXXX     XXX     X   X    X   X")
    print ("      X   X    X   X    X   X    XX XX    X   X")
    print ("      X   X    XXXXX    XXXXX    XX XX    X   X")
    print ("      X   X    X  X     X   X    X X X    X   X")
    print ("      XXXX     X   X    X   X    X   X    XXXXX")
    print("")
    print ("   ,------.                 ,--.   ,--.        ")
    print ("   |  .-.  \ ,--.--. ,--,--.|   `.'   |,--.,--.")
    print ("   |  |  \  :|  .--'' ,-.  ||  |'.'|  ||  ||  |")
    print ("   |  '--'  /|  |   \ '-'  ||  |   |  |'  ''  '")
    print ("   `-------' `--'    `--`--'`--'   `--' `----' ")



                                             

                                             

