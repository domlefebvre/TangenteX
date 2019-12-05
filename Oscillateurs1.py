#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Etude de la trajectoire et du diagramme de phase d'un pendule simple linéaire """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "23 mai 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import pi
from TxOscillateurs import VecteurTemps, CIHarmonique, IntODE2, PenduleLineaire, \
                           PenduleNonLineaire
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title, axis

# constantes physiques du système
Omega2 = 1.0

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10*pi
pas = 0.01
t = VecteurTemps(t0,tmax,pas)

# définition des conditions initiales du système
theta0 = pi/2.0
theta_point0 = 0.0
CI0 = CIHarmonique(theta0,theta_point0)

# intégration du système
Ltheta, Ltheta_point = IntODE2(PenduleLineaire, CI0, t, Omega2)
NLtheta, NLtheta_point = IntODE2(PenduleNonLineaire, CI0, t, Omega2)

# comparaison des trajectoires
figure(1)
grid(True)
plot(t, Ltheta,'blue')
plot(t, NLtheta,'red')
t0 = min(t)
tmax = max(t)
xlim(t0,tmax)
xlabel('$temps$', fontsize = 20)
ylabel('$\\theta$', fontsize = 20)
title('Trajectoire', fontsize = 15)

# comparaison des diagrammes de phase
figure(2)
grid(True)
axis("equal")
plot(Ltheta, Ltheta_point, 'blue')
plot(NLtheta, NLtheta_point, 'red')
xlabel('$\\theta$', fontsize = 20)
ylabel('$\dot{\\theta}$', fontsize = 20)
title('Trajectoire de phase', fontsize = 15)