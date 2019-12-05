# Modèle HCl - calcul de valeurs propres
# Dominique Lefebvre pour TangenteX.com
# 20 aout 2015
#

# importation des librairies
from scipy.linalg import eig
              
# paramètres de la simulation
k = 10.   # raideur ressort
m1 = 1.   # masse H
m2 = 35.  # masse Cl

# définition de la matrice
A = [[-k/m1,k/m1],[k/m2,-k/m2]]

# calcul des valeurs et vecteurs propres.
la,v = eig(A)

# affichage des valeurs propres
l1,l2 = la
print 'Les valeurs propres sont :', l1, 'et', l2

# affichage des vecteurs propres
print 'premier vecteur propre : ',v[:,0]
print 'second vecteur propre : ',v[:,1]



