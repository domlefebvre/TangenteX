#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 résolution de l'équation de Korteweg de Vries
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import zeros, tanh
from matplotlib.pylab import figure, show, meshgrid;
from mpl_toolkits.mplot3d import Axes3D ;

# définition des buffers de travail
Nx = 131
u = zeros((Nx, 3), float) 

# paramètres de la simulation
dx = 0.4   # pas spatial
dt = 0.1   # pas temporel
mu = 0.1
fac = mu*dt/(dx**3)
eps = 0.2 

# préparation du buffer d'affichage
PasAff = 100
Nt = 2000
NbCourbes = int(Nt/PasAff) + 1
BufAff = zeros((Nx, NbCourbes), float)
ncourbes = 0

# onde initiale
X = 0.0
for  i in range(0, Nx):                                   
    u[i, 0] = 0.5*(1 - tanh(X/5. - 5.))
    X += dx

# conditions de bord    
u[0,1] = 1. ; u[0,2] = 1.; 
u[Nx-1,1] = 0. ; u[Nx-1,2] = 0.     

for  i in range (1, Nx-1):                              
    a1 = eps*dt*(u[i + 1, 0] + u[i, 0] + u[i - 1, 0])/(dx*6.)
    if i > 1 and  i < Nx-2: 
       a2 = u[i+2,0] + 2.*u[i-1,0] - 2.*u[i+1,0] - u[i-2,0]
    else: 
       a2 = u[i-1, 0] - u[i+1, 0]
    a3 = u[i+1, 0] - u[i-1, 0]
    u[i, 1] = u[i, 0] - a1*a3 - fac*a2/3.


# boucle principale de calcul
for j in range (1, Nt+1):                             
    for i in range(1, Nx-2):
        a1 = eps*dt*(u[i + 1, 1]  +  u[i, 1]  +  u[i - 1, 1])/(dx*3.)
        if i > 1 and i < Nx-2:
            a2 = u[i+2,1] + 2.*u[i-1,1] - 2.*u[i+1,1] - u[i-2,1]
        else:  
            a2 = u[i-1, 1] - u[i+1, 1]
        a3 = u[i+1, 1] - u[i-1, 1]
        u[i, 2] = u[i,0] - a1*a3 - 2.*fac*a2/3.
    
    # enregistrement pour affichage    
    if j % PasAff == 0:
        for i in range (1, Nx-2): 
            BufAff[i, ncourbes] = u[i, 2]
        ncourbes += 1
    
    # permutation des buffers de travail    
    for k in range(0, Nx):
        u[k, 0] = u[k, 1]
        u[k, 1] = u[k, 2]

# préparation de la grille d'affichage
x = list(range(1, Nx, 2))
y = list(range(0, NbCourbes))
X, Y = meshgrid(x, y)

# Affichage
fig = figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, BufAff[X, Y], color = 'b')
ax.set_xlabel('Abscisse')
ax.set_ylabel('Temps')
ax.set_zlabel('Amplitude')
show()

print "Fin de programme"
