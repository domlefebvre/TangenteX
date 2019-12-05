# -*- coding: Latin-1 -*-
# Recherche des racines d'une fonction avec fsolve()
# Dominique Lefebvre pour TangenteX.com
# 31 juillet 2017
#

# importation des librairies
from scipy.optimize import fsolve

# Fonction dont on cherche les racines
def f(x):
    return x**3 + 4*x**2 + 5
    
# programme principal
xi = -4.0
x0 = fsolve(f,xi)
print'racine : ',x0