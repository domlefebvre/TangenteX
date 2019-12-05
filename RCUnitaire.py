#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" réponse d'une cellule RC à une excitation """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "25 juin 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import sin, arange
from scipy.integrate import odeint
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title

# définition de la fonction de forçage sinusoïdale de la cellule
def ForcageSin(A,OmegaF,phi,t):
    E = A*sin(OmegaF*t + phi)
    return E

# définition du système différentiel 
def RC(u,t,E,tau):
    u_point = (E - u)/tau
    return u_point
    
# constantes physiques du système
R = 1.0e03    # résistance en ohms
C = 1.0e-06   # capacité en farads
tau = R*C     # constante de temps du circuit en secondes
E = 5.0       # échelon de tension en volt

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10*tau
pas = (tmax-t0)/100.0
t = arange(t0, tmax, pas)

# définition des conditions initiales du système
U0 = 0.0

# intégration du système différentiel
u = odeint(RC,U0,t,args=(E,tau))

# comparaison des trajectoires
figure(1)
grid(True)
plot(t, u,'blue')
t0 = min(t)
tmax = max(t)
xlim(t0,tmax)
xlabel('$temps$', fontsize = 20)
ylabel('$Tension$', fontsize = 20)
title('Reponse a un echelon de tension', fontsize = 15)
