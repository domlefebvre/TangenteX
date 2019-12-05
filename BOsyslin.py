# Programme de resolution d'un système d'équations linéaires
# Dominique Lefebvre pour TangenteX.com
# 18 aout 2015
#

# importation des librairies
from scipy.optimize import fsolve

# définition du système à résoudre           
def systeme(var):
    i1,i2,i3 = var[0], var[1], var[2]
    eq1 = 5 - 3*i1 - 6*(i1 - i2)
    eq2 = 6*(i1 - i2) - 10*i2 - 5*(i2 + i3)
    eq3 = -5*(i2 + i3) - 3*i3
    r = [eq1, eq2, eq3]
    return r

# initialisation de la résolution (pour fsolve)
init = [0,0,0]

# solution du système
S = fsolve(systeme, init)

# affichage de la solution
print S
