# programme de tracé du champ gravitationnel terrestre
# Dominique Lefebvre pour TangenteX.com
# 8 aout 2014
#

# ce programme trace la valeur de la norme du champ gravitationnel
# terrestre pour des valeurs de r allant de 0 à 3R
# le but du programme étant de montrer la forme de la courbe
# j'ai normalisée toutes les constantes à 1.

# importation des librairies
from pylab import *                # fonction de tracé de courbe

# constantes
R = 1

# definition de la fonction de calcul de G(r)
def G(r):
    if r < R:
      return -(1/R**3)*r
    else:
      return -1/(r**2)

# initialisation
r0 = 0.0
rmax = 3*R
pas_r = 0.01
r = arange(r0, rmax, pas_r)
NormeG = zeros(len(r))

# calcul de la valeur de G(r)
for i in xrange(len(r)):
    NormeG[i] = G(r[i])

# affichage de la norme du champ en fonction de r
figure()
plot(r, NormeG)
xlabel('r')
ylabel('G(r)')
show()
