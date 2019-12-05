# -*- coding: Latin-1 -*-
# Tracé de la température du sol terrestre en fonction de
# l'absorbance de l'atmosphère
# Dominique Lefebvre pour TangenteX.com
# 18 septembre 2017
#

# importation des librairies
from scipy import arange, pi
import matplotlib.pyplot as plt

# Constantes physiques
kb = 1.38066e-23   # constante de Boltzmann en J/K
h = 6.626076e-34   # constante de Planck en J.s
c = 2.99792458e8   # vitesse de la lumière dans le vide en m/s
sigma = (2*(pi**5)*kb**4)/(15*h**3*c**2)  # constante de Stefan-Boltzmann
Fs = 1368.0    # constante solaire en W.m^2
alphaT = 0.30  # albédo terrestre

# définition de Ts en fonction de l'absorbance
def CalculTs(alpha):
    T = ((Fs*(1.0 - alphaT))/(4.0*sigma*(1.0 - alpha/2.0)))**0.25
    return T

# définition du vecteur d'absorbance atmosphérique
pas = 0.01
alphaA = arange(0.0,1.0,pas)

# calcul de Ts
Ts = CalculTs(alphaA)
    
# Tracé de la courbe
plt.figure()
plt.grid(True)
plt.title("Courbes de temperature en fonction de l'absorbance")
plt.xlabel("Absorbance atmosphere")
plt.ylabel('Temperature (K)')
plt.xlim(0.0, 1.0)
plt.plot(alphaA,Ts,'blue')

plt.show()
