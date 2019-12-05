# -*- coding: utf-8 -*-

# programme de calcul du laplacien scalaire d'une fonction
# par la méthode des différences finies
# Dominique Lefebvre
# TangenteX.com
# 9 août 2016

from scipy import meshgrid, arange, sqrt
from matplotlib.pyplot import *

# Définition de la fonction scalaire
def Fonction(x,y):
    return sqrt(x**2 + y**2)
    
# Routine de calcul du Laplacien    
def LaplacienScalaire(V,dx,dy):
    lap = (V[0:-2,1:-1] + V[2:,1:-1] + V[1:-1,0:-2] + V[1:-1,2:] - 4*V[1:-1,1:-1])/(dx*dy)    
    return lap
    
    
# Définition de la grille de calcul
hx = 0.01
hy = 0.01
X = arange(-2,2,hx)
Y = arange(-2,2,hy)
x,y = meshgrid(X,Y)

# calcul de la fonction
f = Fonction(x,y)

# Calcul du laplacien
delta2 = LaplacienScalaire(f,hx,hy)

# tracé du laplacien
figure()
title('Laplacien')
pcolormesh(x[:-2,:-2], y[:-2,:-2], delta2, vmin=0, vmax=10)
colorbar()
gca().set_aspect("equal") 
show()
