# -*- coding: Latin-1 -*-
# programme BOAleatoirePI

from random import random

# Définition d'une liste aléatoire de N points de coordonnées (x,y)
# compris entre 0.0 et 1.0
N = 10**7
points = [(random(),random()) for _ in range(N)]

# filtrage dans cette liste de tous les points dont la distance au centre
# est inférieure ou égale à 1, c'est à dire qui sont dans le disque
disque = filter(lambda(x,y) : x**2 + y**2 <= 1, points)

# calcul de PI sachant que la probabilité qu'un point soit sur le disque de
# rayon 1 est égale à pi/4
PI = 4.0*len(disque)/float(N)
print 'Valeur estimee de PI : ',PI



