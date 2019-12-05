# -*- coding: utf-8 -*-

# programme de tracé d'un champ vectoriel - exemple du champ électrique
# créé par une charge unitaire positive
# Dominique Lefebvre
# TangenteX.com
# 28 juillet 2016

from scipy import linspace, meshgrid, sqrt
from matplotlib.pyplot import quiver

# Définition du champ électrique créé par une charge q
def ChampElectrique(q,A,x,y):
    Ex = q*(x - A[0])/((x - A[0])**2 + (y - A[1])**2)**(1.5)
    Ey = q*(y - A[1])/((x - A[0])**2 + (y - A[1])**2)**(1.5)
    return Ex,Ey
    
# Définition de la grille de calcul
X = linspace(-1,1,20)
Y = linspace(-1,1,20)
x,y = meshgrid(X,Y)

# Calcul du champ électrique produit par une charge q unitaire positive située
# en A = [0,0]
Ex, Ey = ChampElectrique(1,[0,0],x,y)

# tracé du champ électrique (la longueur des flèches est normalisée)
quiver(x,y,Ex/sqrt(Ex**2 + Ey**2),Ey/sqrt(Ex**2 + Ey**2))