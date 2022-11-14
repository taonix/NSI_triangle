from turtle import *
from math import *
from random import randint
import time

colormode(255)  # Configure le mode de codage pour les couleurs
speed(0)  # Défini la vitesse d'execution du programme

def trapeze(a):
    """Fonction qui crée un trapèze

    :param int a: taille du côté d'un triangle (doit être pair)
    :return: Un trapèze
    """

    fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))  # défini la couleur de remplissage
    begin_fill()  # Commence le remplissage

    forward(a)
    left(120)

    forward(a)
    left(60)

    forward(a)
    left(60)

    forward(a)
    left(120)

    forward(a)

    end_fill()  # Fini le remplissage


def dessine_solution(a, n):  # Fonction qui crée la forme finale
    """Fonction qui trace la figure final

    :param int a: taille du côté d'un triangle (doit être pair)
    :param int n: taille de la solution finale
    :return: La solution finale
    """

    milieu = sqrt(((a * (2 ** n)) ** 2) - ((a * (2 ** (n - 1))) ** 2))  # Permet de se positionner au milieu de la base puis à la moitié du côté (Pythagore)

    if n == 1:  # Cas d'arrêt de la fonction récursive qui consiste à se placer et tracer le premier trapeze

        up()
        left(30)

        forward(milieu)
        left(90)

        down()

        # On trace le trapèze
        trapeze(a)

        up()

        left(90)
        forward(milieu)

        right(210)

    else:  # Cas récursif pour positionner et tracer les solutions

        dessine_solution(a, n - 1)  # Crée le premier trapèze base

        up()  # Lève le stylo pour se positioner

        left(30)
        forward(milieu)

        left(90)

        down()  # Positionnement terminé, traçage

        trapeze(a)  # Créer les différents trapèzes

        dessine_solution(a, n - 1)  # traçe le premier trapèze collé à la base
        left(60)  # Se positionne pour le trapèze suivant

        dessine_solution(a, n - 1)  # traçe le deuxième trapèze collé à la base
        left(60)  # Se positionne pour le trapèze suivan

        dessine_solution(a, n - 1)  # traçe le troisième trapèze collé à la base
        right(30)  # Se positionne pour le trapèze suivan

        forward(milieu)
        right(210)  # Se repositionne

dessine_solution(30, 4)
time.sleep(6000)
