# -*- coding: utf-8 -*-
# Programme de résolution de l'équation de Laplace
# par la méthode de Jacobi
# Dominique Lefebvre pour TangenteX.com
# 25 février 2016
#

# importation des librairies
import numpy as np
import time
import matplotlib.pyplot as plt

# définition des paramètres physiques de l'expérience
Vi = 100.0           # le couvercle est à 100 V
V0 = 0.0             # les cotés sont au potentiel nul
  
# définition de la grille de calcul
N = 100                     # nombre de pas sur la grile (identique en Ox et Oy)
V = np.empty([N+1,N+1])     # grille de calcul courante
Vnew = np.empty([N+1,N+1])  # grille de stockage des calculs nouveaux

# critère de précision du calcul
EPS = 1e-3
# initialisation des compteurs        
ecart = 1.0
iteration = 0

# définition des conditions aux limites
V[0,:]  = Vi  # bord supérieur
V[:,0]  = V0  # bord gauche
V[:,-1] = V0  # bord droit
V[-1,:] = V0  # bord inférieur

# initialisation de l'intérieur de la grille
V[1:N,1:N] = 0.0

# début du calcul - enregistrement de la durée
tdebut = time.time()

# boucle de calcul - méthode de Jacobi en utilisant la vectorisation des boucles
Vnew = V.copy()
while ecart > EPS: 
    iteration += 1   
    # boucle de calcul Numpy
    Vnew[1:-1,1:-1]= 0.25*(V[0:-2,1:-1] +V[2:,1:-1] + V[1:-1,0:-2] + V[1:-1,2:])
    # critère de convergence
    ecart = np.max(np.abs(Vnew - V))
    # sauvegarde dans la grille V de la grille calculée    
    V = Vnew.copy()
   
# fin du calcul - affichage de la durée
print 'Nombre iterations : ',iteration    
print 'Temps de calcul (s) : ',time.time() - tdebut
    
# Affichage des résultats
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)    
plt.imshow(V,cmap='hot')
plt.colorbar()
plt.show()

# sauvegarde de l'image
plt.savefig('E:\PhysNumWeb1\images\Laplace2bis.png')

