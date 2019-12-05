#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Etude de la trajectoire et du diagramme de phase d'un pendule simple linéaire amorti """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "25 mai 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import pi
from scipy.integrate import odeint
from TxOscillateurs import VecteurTemps, CIHarmonique, PenduleLineaireAmorti
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title

# constantes physiques du système
Omega2 = 1.0    # pulsation en radian.s-1
Tau = 0.5       # temps caractéristique en s

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 15*pi
pas = 0.01
t = VecteurTemps(t0,tmax,pas)

# définition des conditions initiales du système
theta0 = pi/10.0
theta_point0 = 0.0
CI0 = CIHarmonique(theta0,theta_point0)

# intégration du système
theta, theta_point = odeint(PenduleLineaireAmorti, CI0, t, args=(Tau,Omega2)).T

# affichage de la trajectoire et de la trajectoire de phase du système
# comparaison des trajectoires
figure(1)
grid(True)
plot(t, theta,'blue')
t0 = min(t)
tmax = max(t)
xlim(t0,tmax)
xlabel('$temps$', fontsize = 20)
ylabel('$\\theta$', fontsize = 20)
title('Trajectoire', fontsize = 15)

# comparaison des diagrammes de phase
figure(2)
grid(True)
plot(theta, theta_point, 'blue')
xlabel('$\\theta$', fontsize = 20)
ylabel('$\dot{\\theta}$', fontsize = 20)
title('Trajectoire de phase', fontsize = 15)