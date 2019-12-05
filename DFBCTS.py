# -*- coding: Latin-1 -*-
# Programme de r�solution de l'�quation de chaleur adimensionn�e
# par diff�rences finies avec sch�ma BCTS
# Dominique Lefebvre pour TangenteX.com
# 21 octobre 2016
#

# importation des librairies

from scipy import meshgrid,zeros,linspace,ones,dot
from scipy.linalg import inv
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D

# Routine de construction d'une matrice tridiagonale
def MatDiag(n,c1,c2):
    M = zeros((n+1,n+1),float)
    M[0,0] = M[n,n] = 1
    for i in range(1,n):
        M[i,i]= c2
        M[i,i-1] = M[i,i+1]= c1
    return M
    
# param�tres de l'exp�rience
L = 1.0
tfin = 0.2
# pas de discr�tisation
dx = 1.0e-2
dt = 1.0e-5
# coefficient de discr�tisation
c = dt/(dx*dx)

# d�claration des buffers de travail
Nx = int(L/dx)
Nt = int(tfin/dt)
X = linspace(0.0,L,Nx+1)
duree = linspace(0.0, tfin,Nt+1)
SX,ST = meshgrid(X,duree)

# construction de la matrice diagonale
A = MatDiag(Nx,-c,1 + 2*c)
# inversion de la matrice diagonale
AI = inv(A)

# conditions initiales et aux limites
TBarreInit = 100.0    # temp�rature initiale de la barre
TExt = 20.0           # temp�rature ext�rieure

# d�finition de la matrice T pour la temp�rature
T = zeros((Nt+1,Nx+1),float)

# Conditions initiales
T[0,:] = TBarreInit*ones(Nx+1,float)

# Conditions aux limites
T[:,0] = TExt*ones(Nt+1,float)   # bord gauche
T[:,Nx] = TExt*ones(Nt+1, float) # bord droit

# sch�ma de BCTS
for t in range(0,Nt):
    T[t+1,:] = dot(AI,T[t,:])
    
# affichage de l'�volution de la temp�rature
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X', fontsize = 16)
ax.set_ylabel('temps', fontsize = 16)
ax.set_zlabel('temperature', fontsize = 16)
ax.view_init(elev=15, azim = 120)

norm = colors.Normalize(TExt,TBarreInit)
p = ax.plot_surface(SX,ST,T,cstride=1,linewidth=0,cmap='jet')
cb = fig.colorbar(p,ax = ax)
       

