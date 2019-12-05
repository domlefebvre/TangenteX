#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Construction de l'ensemble de Mandelbrot
 Algorithme rapide
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "13 août 2019" 
__email__       = "dominique.lefebvre@tangentex.com"


from numpy import linspace, complex64, zeros, less
import time
import matplotlib.pyplot as plt
from matplotlib import colors

# définition de l'ensemble de Mandelbrot
def MandelbrotSetSpeed(xmin, xmax, ymin, ymax, Lx, Ly, niter, horizon):    
    r1 = linspace(xmin, xmax, Lx)
    r2 = linspace(ymin, ymax, Ly)
    C = r1 + r2[:, None]*1j
    P = zeros(C.shape, dtype=int)
    Z = zeros(C.shape, complex64)
    for n in range(niter):
        I = less(abs(Z), horizon)
        P[I] = n
        Z[I] = Z[I]**2 + C[I]
    P[P == niter-1] = 0
    return P

# définition du domaine de calcul et des paramètres de calcul        
xmin, xmax = -2.25, +0.5
ymin, ymax = -1.25, +1.25
nbiter = 100

horizon = 100.0

# définition des paramètres graphiques
LX = 2000
LY = 1500
width =  15
height = 15*LY/LX

# calcul de l'ensemble de Mandelbrot
debut = time.time()
Points = MandelbrotSetSpeed(xmin, xmax, ymin, ymax, LX, LY, nbiter, horizon)
print("Temps de calcul : %s s" % (time.time() - debut))

# préparation de l'affichage
fig = plt.figure(figsize=(width, height), dpi=72)
fig.suptitle("Ensemble de Mandelbrot", fontsize=16, color = 'w')
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

# paramètres de réglage de l'affichage et affichage
gamma = 0.4
cmap = 'hot'
plt.imshow(Points, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic", 
           cmap = cmap, norm = colors.PowerNorm(gamma), origin='lower')


plt.show()
