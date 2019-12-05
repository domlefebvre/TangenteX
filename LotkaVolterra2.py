#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Modèle Proies/Prédacteurs de Lotka-Volterra
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "22 octobre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import integrate, array, linspace
from matplotlib.pylab import *


# définition des paramètres du modèle
a = 3.
b = 1.
c = 1.
d = 2.
x0 = 5     # population initiale des proies
y0= 2      # population initiale des prédateurs
X0 = array([x0, y0])

# définition du point d'équilibre non trivial du système 
X_f1 = array([ d/c, a/b])   

# définition du système différentiel
def LotkaVolterra(X, t=0):
    return array([ a*X[0] -      b*X[0]*X[1],
                   c*X[0]*X[1] - d*X[1] ])
                   
# définition des variables
t0 = 0
tmax= 20
nbpoints = 1000
t = linspace(t0, tmax,nbpoints)             

f2 = figure()
# tracé des différentes orbites
values  = linspace(0.3, 0.9, 5)                          
for v in values:
    X0 = v * X_f1                              
    X = integrate.odeint(LotkaVolterra,X0,t)
    plot(X[:,0], X[:,1],'r-')

# tracé du champ de vecteurs
xmax = xlim(xmin=0)[1]
ymax = ylim(ymin=0)[1]                       
nb_points   = 20
x = linspace(0, xmax, nb_points)
y = linspace(0, ymax, nb_points)
X1 , Y1  = meshgrid(x, y)                       
DX1, DY1 = LotkaVolterra([X1, Y1])
M = (hypot(DX1, DY1))    # calcul de la norme d'une flèche         
M[ M == 0] = 1.
DX1 /= M                 # normalisation de la norme d'une flèche
DY1 /= M
Q = quiver(X1, Y1, DX1, DY1, M, pivot = 'middle')

title(u'Diagramme de phases')
xlabel(u'Proies')
ylabel(u'Prédateurs')
grid()                   