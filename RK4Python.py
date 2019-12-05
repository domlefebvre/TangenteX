#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Implémentation de la routine RK4 en Python 
    Exemple d'application sur le pendule simple
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "26 décembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import pi, ones, zeros, sin, arange, shape, array
from matplotlib.pyplot import figure,plot,show

# définition des paramètres physiques
omega0 = 1.0        # pulsation propre du pendule
theta0 = 0.5        # angle initial en radian
dtheta0 = 0.0       # vitesse angulaire initiale en radian.s-1


# définition de l'équation différentielle à intégrer (équation du pendule simple)
def Pendule(theta,t):
    return array([theta[1], -omega0**2*sin(theta[0])])
    
# définition de la routine RK4
""" Définition des paramètres:
    f : edo à intégrer
    X0: conditions initiales
    h : pas de calcul
"""
def RK4(f,X0,t,h):
    n = len(t)
    X = zeros((len(t),2) + shape(X0))
    X[0] = X0
    for i in range(n-1):        
        k1  = h*f(t[i], X[i])
        k2  = h*f(t[i] + h/2.0, X[i] + k1/2.0)
        k3  = h*f(t[i] + h/2.0, X[i] + k2/2.0)
        k4  = h*f(t[i] + h,X[i] + k3)
        X[i+1] = X[i] + (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return (X)
    
# définition des conditions d'intégration
dt = 0.1                # pas de temps
t = arange(0.0,10.0,dt) # vecteur temps pour l'intégration

# intégration de l'EDO du pendule simple par la méthode RK4
X0 = array([theta0, dtheta0])
y = RK4(Pendule,X0,t,dt)
    
# visualisation de la courbe intégrale
figure()

plot(t,y[:,1])
show()
 