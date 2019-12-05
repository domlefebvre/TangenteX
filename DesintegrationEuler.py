#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Désintégration radioactive avec Euler """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "20 juillet 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des libraires
from TxEDO import Euler, VecteurTemps
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title
    
# définition de l'EDO à integrer    
def Desintegration(x,t):
    x_point = -Lambda*x
    return x_point
    
# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 100.0
dt = 0.1
t = VecteurTemps(t0, tmax, dt)

# définition des paramètres de l'expérience
Lambda = 1.8e-3     # constante de désintégration
N0 = 6.00e20        # nombre de noyaux initial

# solution par la méthode d'Euler
N_Euler = Euler(Desintegration,N0,t)

# Affichage des deux solutions
figure(1)
grid(True)
plot(t, N_Euler,'blue')
xlim(t0,tmax)
xlabel('$temps$', fontsize = 15)
ylabel('$Population$', fontsize = 15)
title('Desintegration', fontsize = 15)