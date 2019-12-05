# -*- coding: Latin-1 -*-
# programme de calcul effet de serre - 1
# Dominique Lefebvre pour TangenteX.com
# 15 septembre 2017
#

# importation des librairies
from scipy import pi

# Constantes physiques
kb = 1.38066e-23   # constante de Boltzmann en J/K
h = 6.626076e-34   # constante de Planck en J.s
c = 2.99792458e8   # vitesse de la lumière dans le vide en m/s
sigma = (2*(pi**5)*kb**4)/(15*h**3*c**2)  # constante de Stefan-Boltzmann

# paramètres physiques
Rs = 6.96e8       # rayon solaire en m
Ts = 5778.0        # température surface solaire moyenne en K
d  = 1.50e11       # distance Terre Soleil en m
alphaT = 0.3       # albéda moyen de la Terre

# calcul du flux solaire moyen (constante solaire)
Fs = (Rs**2*sigma*Ts**4)/d**2
print "Constante solaire = ",Fs

# calcul de la température de surface de la Terre sans effet de serre
Tns = (Fs*(1.0 - alphaT)/(4.0*sigma))**0.25
print "Temperature moyenne de la surface terrestre sans effet de serre = ",Tns
