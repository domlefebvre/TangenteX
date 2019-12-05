#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Tracé d'un portait de phase d'un pendule simple linéaire """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "24 mai 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy.integrate import odeint 
from scipy import linspace,pi
from matplotlib.pyplot import figure,plot,show,xlabel,ylabel,title,tight_layout, axis
from TxOscillateurs import VecteurTemps, PenduleLineaire

# constantes physiques du système
Omega2 = 1.0

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10*pi
pas = 0.01
t = VecteurTemps(t0,tmax,pas)

# table des variations des conditions initiales pour tracer
# le diagramme de phase
borne_init = pi/10.
nb_orbites = 10
theta_init = linspace(0,borne_init,nb_orbites)

# calcul et tracé du portrait de phase
figure(figsize=(6,6))
axis("equal")
for theta0 in theta_init:
    theta, theta_point = odeint(PenduleLineaire,(theta0,0),t,args=(Omega2,)).T
    plot(theta, theta_point)

# titre et libellés
title("Portait de phase - pendule simple lineaire")
xlabel('$\\theta$', fontsize = 20)
ylabel('$\dot{\\theta}$', fontsize = 20)
tight_layout()
show()