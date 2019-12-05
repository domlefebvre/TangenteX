# -*- coding: utf-8 -*-

# programme de calcul d'un champ électrique à partir de la définition d'un
# potentiel par la formule E = -grad(V)
# Dominique Lefebvre
# TangenteX.com
# 28 juillet 2016

from scipy import linspace, meshgrid, sqrt, gradient
from matplotlib.pyplot import quiver

# Définition du potentiel électrostatique créé par une charge q située en A
def Potentiel(q,A,x,y):    
    V = q/((x - A[0])**2 + (y - A[1])**2)
    return V
    
# Définition de la grille de calcul
X = linspace(-1,1,20)
Y = linspace(-1,1,20)
x,y = meshgrid(X,Y)

# Calcul du champ électrique généré par le potentiel V
Ey,Ex = gradient(Potentiel(1,[0,0],x,y))
Ex = -Ex
Ey = -Ey

# tracé du champ électrique (la longueur des flèches est normalisée)
quiver(x,y,Ex/sqrt(Ex**2 + Ey**2),Ey/sqrt(Ex**2 + Ey**2))