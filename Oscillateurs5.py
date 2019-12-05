#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Diagramme d'évolution de l'énergie mécanique d'un pendule simple linéaire amorti """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "9 aout 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import pi,cos
from scipy.integrate import odeint
from TxOscillateurs import VecteurTemps, CIHarmonique, PenduleLineaireAmorti
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title

# constantes physiques du système
Omega2 = 1.0    # pulsation en radian.s-1
Tau = 3.0       # temps caractéristique en s

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10.0
pas = 0.01
t = VecteurTemps(t0,tmax,pas)

# définition des conditions initiales du système
theta0 = pi/10.0
theta_point0 = 0.0
CI0 = CIHarmonique(theta0,theta_point0)

# intégration du système
theta, theta_point = odeint(PenduleLineaireAmorti, CI0, t, args=(Tau,Omega2)).T

# calcul de l'énergie potentielle et cinétique du système
# les constantes m, g et l sont normalisées à 1
Ep = 1 - cos(theta)
Ec = (theta_point)**2/2.0

# tracé des courbes Ep et Ec
figure(1)
grid(True)
plot(t, Ep, "black")
plot(t, Ec, "red")
plot(t,Ep+Ec,"blue")
t0 = min(t)
tmax = max(t)
xlim(t0,tmax)
xlabel('$Temps$', fontsize = 12)
ylabel('$Energie$', fontsize = 12)
title('Energie mecanique du pendule simple lineaire amorti', fontsize = 10)

                        