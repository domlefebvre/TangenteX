# -*- coding: Latin-1 -*-
# programme BOInterpolation
# Dominique Lefebvre pour www.tangenteX.com
# le 9 aout 2015

#Appel des librairies
from scipy import arange, array
from scipy.interpolate import interp1d 
from matplotlib.pyplot import *


# d�finition des tableaux de mesures
Temperature = array([0.0, 5.0, 10.0, 15.0, 20.0])
MasseVol = array([999.87, 999.99, 999.73, 999.13, 998.23])

# recherche du polynome P d'interpolation
P = interp1d(Temperature,MasseVol, kind='cubic')

# calcul de la courbe d'interpolation r�sultante
x = arange(0,20,0.1)
C = P(x)

# trac� de la courbe d'interpolation
figure()
grid(True)
plot(Temperature, MasseVol,'o', ms=8, label="Mesures")
plot(x,C,'r', label = "interpolation cubique")
legend()
show()




