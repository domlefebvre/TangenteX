# -*- coding: Latin-1 -*-
# programme BOAleatoirePI

from random import random

# D�finition d'une liste al�atoire de N points de coordonn�es (x,y)
# compris entre 0.0 et 1.0
N = 10**7
points = [(random(),random()) for _ in range(N)]

# filtrage dans cette liste de tous les points dont la distance au centre
# est inf�rieure ou �gale � 1, c'est � dire qui sont dans le disque
disque = filter(lambda(x,y) : x**2 + y**2 <= 1, points)

# calcul de PI sachant que la probabilit� qu'un point soit sur le disque de
# rayon 1 est �gale � pi/4
PI = 4.0*len(disque)/float(N)
print 'Valeur estimee de PI : ',PI



