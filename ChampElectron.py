# -*- coding: utf-8 -*-
# Programme de calcul du champ électrique créé par un électron
# par l'équation de Poisson
# Méthode de Gauss-Seidel
# Dominique Lefebvre pour TangenteX.com
# 16 mars 2016
#

# importation des librairies
from numpy import max,abs,empty,linspace,meshgrid,zeros,gradient
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# définition des paramètres physiques de l'expérience
V0 = 0.0             # le potentiel est nul aux bords de la grille
Q = -1.0             # charge normalisée d'un électron
  
# définition de la grille de calcul
N = 50                 # nombre de pas sur la grile (identique en Ox et Oy)
V = empty([N+1,N+1])     # création de la grille, en float par défaut


# critère de précision du calcul
EPS = 1e-3        # précision souhaitée pour le critère de convergence

# initialisation des compteurs
ecart = 1.0       
iteration = 0

# définition des conditions aux limites
V[0,:]  = V0  # bord supérieur
V[:,0]  = V0  # bord gauche
V[:,-1] = V0  # bord droit
V[-1,:] = V0  # bord inférieur

# initialisation de l'intérieur de la grille
V[1:N,1:N] = 0.0

# définition de la distribution des charges
C = zeros([N+1,N+1])
C[N/2,N/2] = Q


# boucle de calcul - méthode de Gauss-Seidel
while ecart > EPS:    
    iteration += 1
    Vprec = V.copy()
    V[1:-1,1:-1]= 0.25*(Vprec[0:-2,1:-1]+V[2:,1:-1]+Vprec[1:-1,0:-2]+V[1:-1,2:]+C[1:-1,1:-1])
    ecart = max(abs(V-Vprec))
 
# calcul du champ électrique
Ex,Ey = gradient(V)
E = -(Ex*Ex + Ey*Ey)**0.5
# normalisation à la position de l'électron par moyenne sur le voisinage
i = j = N/2
E[i,j] = 0.25*(E[i-1,j] + E[i+1,j] + E[i,j-1] + E[i,j+1])

# définition de la grille de visualisation
x = linspace(0,N+1,N+1)
y = linspace(0,N+1,N+1)
X,Y = meshgrid(x,y)

# affichage du champ électrique
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X', fontsize = 16)
ax.set_ylabel('Y', fontsize = 16)
ax.set_zlabel('Champ electrique', fontsize = 16)
ax.view_init(elev=15, azim = 120)

p = ax.plot_surface(X,Y,E,cstride=1,linewidth=0.5,cmap='hot')

plt.show()

