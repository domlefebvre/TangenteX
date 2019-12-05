# Programme de resolution d'un syst�me d'�quations lin�aires
# Dominique Lefebvre pour TangenteX.com
# 18 aout 2015
#

# importation des librairies
from scipy.optimize import fsolve

# d�finition du syst�me � r�soudre           
def systeme(var):
    i1,i2,i3 = var[0], var[1], var[2]
    eq1 = 5 - 3*i1 - 6*(i1 - i2)
    eq2 = 6*(i1 - i2) - 10*i2 - 5*(i2 + i3)
    eq3 = -5*(i2 + i3) - 3*i3
    r = [eq1, eq2, eq3]
    return r

# initialisation de la r�solution (pour fsolve)
init = [0,0,0]

# solution du syst�me
S = fsolve(systeme, init)

# affichage de la solution
print S
