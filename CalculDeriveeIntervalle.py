# -*- coding: Latin-1 -*-
# Calcul de la d�riv�e d'une fonction sur un intervalle donn�
# Dominique Lefebvre pour TangenteX.com
# 24 juillet 2017
#

from scipy import cos, pi, arange
from scipy.misc import derivative
import matplotlib.pyplot as plt

# d�finition de la fonction � d�river
def fonction(x):
    return cos(x)
    
# d�finition de l'intervalle sur lequel on calcule la d�riv�e
Xmin = -2*pi
Xmax = 2*pi
X = arange(Xmin,Xmax,0.01)

# calcul de la fonction
Y = fonction(X)
    
# calcul de la d�riv�e sur l'intervalle X
dY = derivative(fonction,X)

# affichage de la fonction et de sa d�riv�e sur l'intervalle
plt.xlim(Xmin, Xmax)
plt.ylim(-1,1)
     
plt.plot(X,Y,'b')
plt.plot(X,dY,'r')

plt.text(-5.2, 0.7,
     r'$f(x)= cos(x)$', horizontalalignment='left',
     fontsize=18,color='b')

plt.text(-0.6, 0.7,
     r"$f '(x)= -sin(x)$", horizontalalignment='left',
     fontsize=18,color='r')
plt.grid(True)
plt.show()