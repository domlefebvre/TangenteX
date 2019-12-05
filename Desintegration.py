#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Désintégration radioactive """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "20 juillet 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

from TxEDO import Euler, RK4, VecteurTemps
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title
    
# définition de la fonction de désintégration (l'EDO à intégrer)
def Desintegration(x,t):
    x_point = -Lambda*x
    return x_point
    
# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 400.0
dt = 1.0
t = VecteurTemps(t0, tmax, dt)

# définition des paramètres de l'expérience
Lambda = 0.0125   # constante de désintégration du radon 222
N0 = 1.0e4        # nombre de noyaux initial

# solution par la méthode d'Euler
N_Euler = Euler(Desintegration,N0,t)

# solution par RK4
N_RK4 = RK4(Desintegration,N0,t)

# Affichage des deux solutions
figure(1)
grid(True)
plot(t, N_Euler,'blue')
plot(t, N_RK4,'red')
xlim(t0,tmax)
xlabel('$temps$', fontsize = 15)
ylabel('$Population$', fontsize = 15)
title('Desintegration', fontsize = 15)