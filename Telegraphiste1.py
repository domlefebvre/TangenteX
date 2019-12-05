#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Résolution de l'équation des télégraphistes pour une ligne sans perte
 Méthode matricielle
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "27 mars 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import zeros,linspace,dot, pi, exp, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Routine de construction de la matrice tridiagonale A
def MatDiag(n):
    M = zeros((n+1,n+1),float)
    for i in range(1,n):
        M[i,i-1], M[i,i], M[i,i+1] = 1,-2,1  # coefficients diagonaux
    M = Alpha*M
    return M

# fonction gaussienne de configuration initiale de l'onde
def Uzero():
    U0 = k*exp(-0.5*((X - mu)/sigma)**2)
    return U0
    
    
# calcul de la dérivée de V(x,t) pour déterminer les conditions de bord
def dUzero():
    U1 = zeros(Nx+1)
    U0 = Uzero()
    U1 = -((X-mu)/sigma**2)*U0
    return U1

# Paramètres physiques de la simulation
L = 0.1             # inductance linéique
C = 2.5             # capacitance linéique
c = 1.0/sqrt(L*C)
        
# Définition du maillage spatial - indice i
LX = 200.     
dx = 0.05
Nx = int(LX/dx)
X = linspace(0,LX,Nx+1) 

# Définition du maillage temporel en respectant CFL = 1 - indice j
duree = 100
dt = dx/c    # application du CFL = 1
Nt = int(duree/dt)
T = linspace(0,duree,Nt+1)

# Constantes de calcul
Alpha = (c*dt/dx)**2

# Construction de la matrice diagonale du système avec les conditions 
# aux limites (valeurs aux bords nulles)
A = MatDiag(Nx)

# Définition de la matrice U
U = zeros((Nx+1,Nt+1),float)

# paramètres du signal gaussien (conditions initiales)
mu = 0.0
sigma = 0.5
k = 1./(sigma*sqrt(2*pi))

# Définition des conditions initiales
U[:,0] = Uzero()
U[:,1] = dUzero()

# Calcul de la matrice U résultante
for j in range(1,Nt):
    U[:,j+1] = dot(A,U[:,j]) + 2*U[:,j] - U[:,j-1]
    
# Affichage de la solution
fig = plt.figure(figsize=(14,8))
plt.grid(True)
plt.title(u"Equation des télégraphistes sans perte - méthode matricielle")
ax = fig.add_subplot(111)
ax.set_xlabel('X', fontsize = 16)
ax.set_ylabel('amplitude', fontsize = 16)

# préparation de l'animation
lines = []
plt.hold("off")
for i in range(Nt):
    p, = plt.plot(X,U[:,i],'k')
    lines.append([p])
ani = animation.ArtistAnimation(fig,lines,interval=2,blit=True)
      
plt.show()