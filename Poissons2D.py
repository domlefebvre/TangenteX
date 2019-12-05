# -*- coding: utf-8 -*-
# Programme de calcul du champ de potentiel pour une distribution de charges
# par l'équation de Poisson
# Méthode de Gauss-Seidel
# Dominique Lefebvre pour TangenteX.com
# 6 mars 2016
#

# importation des librairies
from numpy import max,abs,empty,linspace,meshgrid,zeros
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# définition des paramètres physiques de l'expérience
V0 = 0.0             # les cotés de la boite sont au potentiel nul
Q = 100.0              # valeur absolue des charges
  
# définition de la grille de calcul
N = 100                  # nombre de pas sur la grile (identique en Ox et Oy)
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
C[N/4,N/4] = Q
C[3*N/4,3*N/4] = -Q

# boucle de calcul - méthode de Gauss-Seidel
tdebut = time.time()
while ecart > EPS:    
    iteration += 1
    Vprec = V.copy()
    V[1:-1,1:-1]= 0.25*(Vprec[0:-2,1:-1]+V[2:,1:-1]+Vprec[1:-1,0:-2]+V[1:-1,2:]+C[1:-1,1:-1])
    ecart = max(abs(V-Vprec))
print 'Nombre iterations : ',iteration    
print 'Temps de calcul (s) : ',time.time() - tdebut
 
# définition de la grille de visualisation
x = linspace(0,N+1,101)
y = linspace(0,N+1,101)
X,Y = meshgrid(x,y)

# affichage du champ de potentiel
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0,101)
ax.set_ylim(0,101)
ax.set_zlim(-60,60)
ax.set_xlabel('X', fontsize = 16)
ax.set_ylabel('Y', fontsize = 16)
ax.set_zlabel('Potentiel', fontsize = 16)
ax.view_init(elev=15, azim = 120)

p = ax.plot_surface(X,Y,V,cstride=1,linewidth=0,cmap='hot')
cb = fig.colorbar(p,ax = ax)
plt.show()

