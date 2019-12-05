# -*- coding: Latin-1 -*-
# Calcul de la d�riv�e d'une fonction en un point donn�
# Dominique Lefebvre pour TangenteX.com
# 24 juillet 2017
#

from scipy import sin, pi
from scipy.misc import derivative

# d�finition de la fonction � d�river
def fonction(x):
    return sin(x)
    
# calcul de la d�riv�e au point x
x = pi
print derivative(fonction,x)