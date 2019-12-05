# -*- coding: utf-8 -*-

# programme de calcul du rotationnel d'un champ
# Dominique Lefebvre
# TangenteX.com
# 5 août 2016

from scipy import meshgrid, diff, arange, sin, cos, pi
from matplotlib.pyplot import *
#from mpl_toolkits.mplot3d import Axes3D



# Définition du champ
def Champ(x,y):
#   Champ à rotationnel non nul
#    Ex = -sin(y)
 #   Ey = cos(x)
#    Ex = x*x*0.5
#    Ey = -x*y
#   champ à rotationnel nul
    Ex = -x
    Ey = y
    return Ex,Ey
    
# Calcul du rotationnel
def Rotationnel(x,y,Fx,Fy):
    dFx = (diff(Fx,axis=0)/hy)[:,:-1]
    dFy = (diff(Fy,axis=1)/hx)[:-1,:]
    return dFy - dFx
    
# Définition de la grille de calcul
hx = 0.3
hy = 0.3
X = arange(-2,2,hx)
Y = arange(-2,2,hy)
x,y = meshgrid(X,Y)

# Calcul du champ
Ex, Ey = Champ(x,y)

# calcul du rotationnel du champ
Rk = Rotationnel(x,y,Ex,Ey)

# tracé du champ électrique
#quiver(x,y,Ex,Ey)
figure()
title('rotationnel')
pcolormesh(x, y, Rk, vmin=-2, vmax=2)
colorbar()
gca().set_aspect("equal") 
show()
