# -*- coding: utf-8 -*-
# Programme de résolution de l'équation de Laplace
# par la méthode de Gauss-Seidel
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
N = 100                  # nombre de pas sur la grile (identique en Ox et Oy)
V = np.empty([N+1,N+1])  # création de la grille, en float par défaut

# critère de précision du calcul
EPS = 1e-3        # précision souhaitée pour le critère de convergence

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

# boucle de calcul - méthode de Gauss-Seidel
while ecart > EPS:    
    iteration += 1
    # sauvegarde de la grille courante pour calculer l'écart
    Vprec = V.copy()
    # calcul de la nouvelle valeur du potentiel sur la grille
    V[1:-1,1:-1]= 0.25*(Vprec[0:-2,1:-1] +V[2:,1:-1] + Vprec[1:-1,0:-2] + V[1:-1,2:])
    # critère de convergence
    ecart = np.max(np.abs(V-Vprec))

    
# fin du calcul - affichage de la durée
print 'Nombre iterations : ',iteration    
print 'Temps de calcul (s) : ',time.time() - tdebut
    
# Affichage des résultats
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)    
plt.imshow(V, cmap='hot')
plt.colorbar()
plt.show()


