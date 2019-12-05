# -*- coding: Latin-1 -*-
# Calcul de la dérivée d'une fonction en un point donné
# Dominique Lefebvre pour TangenteX.com
# 24 juillet 2017
#

from scipy import sin, pi
from scipy.misc import derivative

# définition de la fonction à dériver
def fonction(x):
    return sin(x)
    
# calcul de la dérivée au point x
x = pi
print derivative(fonction,x)