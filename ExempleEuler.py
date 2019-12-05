#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Exemple d'emploi de la fonction Euler() """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "4 septembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from TxEDO import Euler, VecteurTemps
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title

# définition de l'EDO à intégrer
def EDO(x,t):
    return (1.0/x**2)
    
# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 500.0
dt = 0.01
t = VecteurTemps(t0, tmax, dt)

# définition de la condition initiale
x0 = 1.0

# solution par la méthode d'Euler
y = Euler(EDO,x0,t)

# Affichage de la solution
figure(1)
grid(True)
plot(t, y,'blue')
xlim(t0,tmax)
xlabel('$temps$', fontsize = 15)
ylabel('$y$', fontsize = 15)
title('Integration 1/x^2', fontsize = 15)