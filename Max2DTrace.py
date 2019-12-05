#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Tracé de la fonction de diffraction
  Illustration de RechercheMax2D
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "23 octobre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import arange, meshgrid,pi, sinc,fabs
from matplotlib.pylab import figure, contour, title
from matplotlib.cm import spectral_r, binary
from mpl_toolkits.mplot3d import Axes3D ;


# déclaration du domaine d'étude
xmin = -pi; xmax = pi
ymin = -pi; ymax = pi

    
# définition de la fonction à tracer
def Fonction(x,y):
    z = fabs(sinc(x)*sinc(y))    
    return z

# fonction de définition du domaine d'affichage
def DomaineAff():
    deltaX = 0.1;deltaY = 0.1
    x = arange(xmin, xmax, deltaX)
    y = arange(ymin, ymax, deltaY)
    X, Y = meshgrid(x,y)
    return (X,Y)
    
# fonction de tracé 3D 
def Tracer3D(X,Y):
    fig1 = figure(figsize=(10,8))
    ax = Axes3D(fig1)
    Z = Fonction(X,Y)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, cmap=binary)
    title(u'Diffraction par une fente carrée - Intensité')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('sqrt(I(x,y)/I0)')
    return Z

# fonction de tracé des lignes de niveau
def TracerLN(X,Y):
    fig2 = figure(figsize=(10,8))
    ax = fig2.add_subplot(1, 1, 1)
    NbLignesNiveau = 20
    Z = Fonction(X,Y)
    contour(X, Y, Z, NbLignesNiveau, cmap = spectral_r, linewidth=.5)
    major_ticks = arange(xmin, xmax, pi)
    minor_ticks = arange(ymin, ymax, pi/5)
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='both')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    title(u'Tracé des lignes de niveau')  
    return
 

# tracé graphique des courbes
X,Y = DomaineAff()   # définition des bornes du domaine pour l'affichage
Tracer3D(X,Y)        # affichage de la courbe en 3D
TracerLN(X,Y)        # affichage de la courbe en contours
