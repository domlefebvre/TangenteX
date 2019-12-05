# -*- coding: utf-8 -*-
# Programme de calcul de potentiel créé par un condensateur plan
# dans ubne boite reliée à la terre.
# Méthode de Gauss-Seidel
# Dominique Lefebvre pour TangenteX.com
# 2 mars 2016
#

# importation des librairies
from numpy import max,abs,empty,linspace,meshgrid
import time
import matplotlib
import matplotlib.pyplot as plt

# définition des paramètres physiques de l'expérience
V0 = 0.0             # les cotés de la boite sont au potentiel nul
Vp = 400.0           # potentiel de plaque 
  
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

# définition de la géométrie du condensateur
V[25:75,40]  = -Vp  # bord plaque gauche potentiel négatif
V[25:75,60]  = Vp   # bord plaque droit potentiel positif

# début du calcul - enregistrement de la durée
tdebut = time.time()

# boucle de calcul - méthode de Gauss-Seidel
while ecart > EPS:    
    iteration += 1
    # sauvegarde de la grille courante pour calculer l'écart
    Vprec = V.copy()
    # calcul de la nouvelle valeur du potentiel sur la grille
    V[1:-1,1:-1]= 0.25*(Vprec[0:-2,1:-1] +V[2:,1:-1] + Vprec[1:-1,0:-2] + V[1:-1,2:])
    # je réaffecte les valeurs constantes sur les plaques
    V[25:75,40]  = -Vp  
    V[25:75,60]  = Vp   
    # critère de convergence
    ecart = max(abs(V-Vprec))
   
# fin du calcul - affichage de la durée
print 'Nombre iterations : ',iteration    
print 'Temps de calcul (s) : ',time.time() - tdebut
 
# Affichage des résultats
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(1,1,1) 

# dessin des deux plaques
plt.plot([40,40],[25,75],'b-', lw = 4)  # plaque gauche
plt.plot([60,60],[25,75],'r-', lw = 4)  # plaque droite

# dessin de la grille de calcul
plt.grid()

# tracé des équipotentielles
x = linspace(0,N+1,N+1)
y = linspace(0,N+1,N+1)
X,Y = meshgrid(x,y)
equ = plt.contour(X,Y,V,20,colors='b')
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.clabel(equ, fontsize=10, inline=1,fmt='%1.0f')

# tracé de la grille
plt.imshow(V, cmap='hot')
plt.colorbar()

plt.show()

