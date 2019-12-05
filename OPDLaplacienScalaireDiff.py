# -*- coding: utf-8 -*-

# programme de calcul du laplacien scalaire d'une fonction
# par la méthode des différentielles
# Dominique Lefebvre
# TangenteX.com
# 9 août 2016

from scipy import meshgrid, diff, arange, sqrt
from matplotlib.pyplot import *

# Définition de la fonction scalaire
def Fonction(x,y):
    return sqrt(x**2 + y**2)
    
# Routine de calcul du Laplacien    
def LaplacienScalaire(x,y,F):
    dFx = (diff(F,n=2,axis=1)/hx**2)[:-2,:]
    dFy = (diff(F,n=2,axis=0)/hy**2)[:,:-2]
    return dFx + dFy
    
    
# Définition de la grille de calcul
hx = 0.001
hy = 0.001
X = arange(-2,2,hx)
Y = arange(-2,2,hy)
x,y = meshgrid(X,Y)

# calcul de la fonction
f = Fonction(x,y)

# Calcul du laplacien
delta2 = LaplacienScalaire(x,y,f)

# tracé du laplacien
figure()
title('Laplacien')
pcolormesh(x[:-2,:-2], y[:-2,:-2], delta2, vmin=0, vmax=10)
colorbar()
gca().set_aspect("equal") 
show()