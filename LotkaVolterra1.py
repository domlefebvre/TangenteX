#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Modèle Proies/Prédacteurs de Lotka-Volterra
 Tracé des courbes de dynamique des populations proies/prédateurs
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "22 octobre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import integrate, array, linspace
from matplotlib.pylab import figure,plot,grid,legend,xlabel,ylabel,title

# définition des paramètres du modèle
a = 3.
b = 1.
c = 1.
d = 2.
x0 = 5     # population initiale des proies
y0= 2      # population initiale des prédateurs
X0 = array([x0, y0]) 

# définition du système différentiel
def LotkaVolterra(X, t=0):
    return array([ a*X[0] -      b*X[0]*X[1] ,
                   c*X[0]*X[1] - d*X[1] ])

# définition des variables
t0 = 0
tmax= 20
nbpoints = 1000
t = linspace(t0, tmax,nbpoints)             
                                   
# calcul de la dynamique de la population
X = integrate.odeint(LotkaVolterra, X0, t)
proies, predateurs = X.T

# tracé de la dynamique de la population
fig = figure()
plot(t, proies,'b-',label= u'Proies')
plot(t, predateurs,'g-',label= u'Prédateurs')
grid()
legend()
xlabel('Temps')
ylabel('Population')
title('Dynamique des populations')  

