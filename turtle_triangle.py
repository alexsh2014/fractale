import math
from math import *
from turtle import *

TWO_PI = 2*math.pi

TRIANGLE = 3
QUADRILATRE = 4
PENTAGONE = 5
OCTOGONE = 6
REDUCTION = 0.5
TAILLE_PINCEAU_ROUGE = 5
TAILLE_PINCEAU_VERT = 7
TAILLE_PINCEAU_BLEU = 9

speed(2000)


# fonction qui retourne les coordonnes dans le plan
# d'un point sur un cercle rayon d'angle angle
def calculCoordooneesPolaires(angle, rayon):
    x = math.cos(angle*TWO_PI)*rayon
    y = math.sin(angle*TWO_PI)*rayon
    return x, y

# fonction recursive qui pour chaque point, trace un polygione de N cotes
# nbOccurences est la profondeur de recursivité
# dans ce cas, elle indique le nb de fois que le segment va etre découpé
# on utilise la geometrie: les points sont le centre de cercles
# et pour chaque cercle, on se deplace de 2PI/N pour voir les N points du polygone :
# 1 cote = 1 corde du cercle


def fractal(nbCotes, x, y, nbOccurences, rayon):

    # test des parametres
    if nbCotes < 3:
        nbCotes = TRIANGLE

    # pour eviter de planter le PC avec trop de calculs
    if nbOccurences > 8:
        nbOccurences = 7

    if rayon > 600:
        rayon = 600

    # calcul de l'angle entre 2 points à relier pour le cote du polygone
    deltaAngle = 1/nbCotes

    # la recurisivte va se faire sur chacun des cotés du polygone
    for i in range(nbCotes):
        if i == 1:
            pencolor("red")
            pensize(TAILLE_PINCEAU_ROUGE)
        elif i == 2:
            pencolor("blue")
            pensize(TAILLE_PINCEAU_BLEU)
        else:
            pencolor("green")
            pensize(TAILLE_PINCEAU_VERT)

        # calcul de l'angle du point i (i*2PI/nbcotes)
        newAngle = i/nbCotes
        if nbOccurences-1 > 0:
            # on réduit la taille de nos cotés
            newRayon = rayon*REDUCTION
            # calcul coordonnees x,y du nouveau centre du rayon
            # on transforme les coordonees polaires en coordonnes plan
            # (trigonométrie)
            newCircleCenter = calculCoordooneesPolaires(newAngle, newRayon)

            # on calcule les points suivant en appelant la fonction recursivement
            # ile ne faut pas oublier de réduire nbOccurences de 1 pour éviter la boucle infinie !!
            fractal(
                nbCotes, newCircleCenter[0] + x, newCircleCenter[1] + y, nbOccurences - 1, newRayon)
        else:
            # une fois les cercles calculés pour 1 coté, on les trace
            # On cherche les coordonnes des deux points de la corde du cercle
            p1 = calculCoordooneesPolaires(newAngle - deltaAngle, rayon)
            p2 = calculCoordooneesPolaires(newAngle, rayon)
            # on trace les cordes. On relie les deux points P1 et P2
            penup()
            goto(p1[0] + x, p1[1] + y)
            pendown()
            goto(p2[0] + x, p2[1] + y)
            penup()


fractal(TRIANGLE, 0, 0, 8, 600)

exitonclick()
