# -*- coding: utf-8 -*-

# programme de calcul de la divergence d'un champ
# Dominique Lefebvre
# TangenteX.com
# 5 août 2016

from scipy import meshgrid, diff, arange
from matplotlib.pyplot import *

# Définition du champ
def Champ(x,y):
    Ex = x*x*0.5
    Ey = x*y
    return Ex,Ey
    
# Calcul de la divergence
def Divergence(Fx,Fy):
    div = (diff(Fx,axis=1)/hx)[:-1,:] + (diff(Fy,axis=0)/hy)[:,:-1]
    return div

    
# Définition de la grille de calcul
hx = 0.01
hy = 0.01
X = arange(-2.,2.,hx)
Y = arange(-2.,2.,hy)
x,y = meshgrid(X,Y)

# Calcul du champ
Ex, Ey = Champ(x,y)

# calcul de la divergence du champ
divE = Divergence(Ex,Ey)

# tracé de la divergence
figure()
title("divergence")
pcolormesh(x, y, divE, vmin=-10, vmax=10)
colorbar()
gca().set_aspect("equal") 
show()
