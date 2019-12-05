#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 Construction de l'ensemble de Mandelbrot 
 Algorithme naïf avec anti-aliasing
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "9 août 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace, zeros, log
import time
from matplotlib import colors
import matplotlib.pyplot as plt

# définition de la suite de récurrence
def MandelbrotDef(c,niter, horizon, logh):  
    z = c                     # initialisation de la récurrence 
    for n in range(niter):    # déroulement du nombre d'itérations max
        if abs(z) > horizon:  # test de divergence
            return n - log(log(abs(z)))/log(2) + logh           # si divergence, on retourne le nb d'itérations      
        z = z**2 + c           # calcul du terme suivant de la suite
    return 0                  # la suite est convergente, on retourne 0

# définition de l'ensemble de Mandelbrot
def MandelbrotSet(xmin, xmax, ymin, ymax, Lx, Ly, niter, horizon, logh):
    r1 = linspace(xmin, xmax, Lx)
    r2 = linspace(ymin, ymax, Ly)
    P = zeros((Lx,Ly))
    for i in range(Lx):
        for j in range(Ly):
            P[i,j] = MandelbrotDef(r1[i] + 1j*r2[j], niter, horizon, logh)
    return P

# définition du domaine de calcul et des paramètres de calcul       
xmin, xmax = -2.25, +0.5
ymin, ymax = -1.25, +1.25
nbiter = 100
horizon = 2.0**40
logh = log(log(horizon))/log(2)

# définition des paramètres graphiques
LX = 2000
LY = 1500
width =  15
height = 15*LY/LX

# calcul de l'ensemble de Mandelbrot
debut = time.time()
Points = MandelbrotSet(xmin, xmax, ymin, ymax, LX, LY, nbiter, horizon, logh)
print("Temps de calcul : %s s" % (time.time() - debut))

# préparation de l'affichage
fig = plt.figure(figsize=(width, height), dpi=72)
fig.suptitle("Ensemble de Mandelbrot", fontsize=16, color = 'w')
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

# paramètres de réglage de l'affichage et affichage
gamma = 0.4
cmap = 'hot'
plt.imshow(Points.T, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic", 
           cmap = cmap, norm = colors.PowerNorm(gamma))

plt.show()
