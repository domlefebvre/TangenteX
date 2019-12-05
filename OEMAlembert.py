# -*- coding: Latin-1 -*-
# Programme de résolution de l'équation d'Alembert
# par différences finies 
# Dominique Lefebvre pour TangenteX.com
# 20 novembre 2016
#

# importation des librairies

from scipy import meshgrid,zeros,linspace,dot, sin, pi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Routine de construction de la matrice tridiagonale A
def MatDiag(n):
    M = zeros((n+1,n+1),float)
    for i in range(1,n):
        M[i,i-1], M[i,i], M[i,i+1] = 1,-2,1  # coefficients diagonaux
    M = Alpha*M
    return M

# Fonctions de définition de la configuration initiale de l'onde
# la fonction fixant les conditions initiale est arbitraire, ici un sin(x)
def Uzero():
    U0 = sin(2*pi*X/4.0)
    return U0
# fonction de définition de la vitesse initiale de l'onde (la dérivée de Uzero)
def dUzero():
    U1 = zeros(Nx+1)
    U0 = Uzero()
    for i in range(1,Nx):
        U1[i] = U0[i] +  (Alpha/2.)*(U0[i+1] - 2*U0[i] + U0[i-1])
    U1[0] = U1[Nx] = 0.0
    return U1

# Paramètres physiques de la simulation
c = 1.0      # célérité de l'onde
        
# Définition du maillage spatial - indice i
L = 4.0     # la cavité est dimensionnée pour un mode = 2
dx = 1.0e-2
Nx = int(L/dx)
X = linspace(0,L,Nx+1) 

# Définition du maillage temporel en respectant CFL = 1 - indice j
duree = 2*pi
dt = dx/c    # application du CFL = 1
Nt = int(duree/dt)
T = linspace(0,duree,Nt+1)

# Paramètres de calcul
Alpha = (c*dt/dx)**2

# Construction de la matrice diagonale du système avec les conditions 
# aux limites (valeurs aux bords nulles)
A = MatDiag(Nx)

# Définition de la matrice U
U = zeros((Nx+1,Nt+1),float)

# Définition des conditions initiales
U[:,0] = Uzero()
U[:,1] = dUzero()

# Calcul de la matrice U résultante
for t in range(1,Nt):
    U[:,t+1] = dot(A,U[:,t]) + 2*U[:,t] - U[:,t-1]
    
# Affichage de la solution
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('abscisse', fontsize = 16)
ax.set_ylabel('temps', fontsize = 16)
ax.set_zlabel('amplitude', fontsize = 16)
ax.view_init(elev = 15, azim = 120)

ST,SX = meshgrid(T,X)
p = ax.plot_surface(SX,ST,U,color = 'white')       
plt.show()