# -*- coding: Latin-1 -*-
# Tracé de la fonction de Planck pour les températures de
# surface du Soleil et de la Terre
# Dominique Lefebvre pour TangenteX.com
# 18 septembre 2017
#

# importation des librairies
from scipy import exp, arange

import matplotlib.pyplot as plt

# Constantes physiques
kb = 1.38066e-23   # constante de Boltzmann en J/K
h = 6.626076e-34   # constante de Planck en J.s
c = 2.99792458e8   # vitesse de la lumière dans le vide en m/s

# Définition de la fonction de Planck
def Planck(Lambda,T):
    u = []
    for l in Lambda:
        l = l*1.0e-9   # conversion en metre
        u.append((2.*h*c**2/l**5)*1./(exp((h*c)/(l*kb*T)) - 1.))
    return u
    
# calcul de la courbe de Planck pour la température de surface du Soleil
lambdaS_min = 250    # longueur d'onde min en nm
lambdaS_max = 2500   # longueur d'onde max en nm
pas = 10.
LambdaS = arange(lambdaS_min, lambdaS_max,pas)
les_S = Planck(LambdaS, 5778.0)

# calcul de la courbe de Planck pour la température de surface de la Terre
lambdaT_min = 5.0e3    # longueur d'onde min en nm
lambdaT_max = 1.0e5    # longueur d'onde max en nm
pas = 100.
LambdaT = arange(lambdaT_min, lambdaT_max,pas)
les_T = Planck(LambdaT, 288.0)

# Tracé des deux courbes
plt.figure()
plt.subplot(2,1,1)
plt.grid(True)
plt.title("Courbes de Planck - Soleil")
plt.xlabel("Longueur d'onde en nm")
plt.ylabel('LES en W/m2/nm')
plt.xlim(lambdaS_min,lambdaS_max)
plt.plot(LambdaS,les_S,'blue',label = "T = 5778 K")
plt.legend()

plt.subplot(2,1,2)
plt.grid(True)
plt.title("Courbes de Planck - Terre")
plt.xlabel("Longueur d'onde en nm")
plt.ylabel('LES en W/m2/nm')
plt.xlim(lambdaT_min,lambdaT_max)
plt.plot(LambdaT,les_T,'red',label = "T = 288 K")
plt.legend()

plt.tight_layout()
plt.show()
