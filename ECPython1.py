# -*- coding: Latin-1 -*-
# Programme de r�solution de l'�quation de chaleur adimensionn�e
# par diff�rences finies avec sch�ma FTCS
# Dominique Lefebvre pour TangenteX.com
# 29 janvier 2016
#

# importation des librairies
from scipy import meshgrid, zeros, linspace, ones
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D


# param�tres de l'exp�rience
L = 1.0
tfin = 0.2
# pas de discr�tisation
dx = 0.01
dt = 5.0e-5
    
# v�rification du crit�re de stabilit� du sch�ma FTCS (Forward Time Centred Space)
if dt > (dx*dx)/(2.0):
    print 'Attention schema instable'
    print 'dt doit etre inferier a : ',(dx*dx)/(2.0)
    sys.exit(1)
   
# d�claration des buffers de travail
Nx = int(L/dx)
Nt = int(tfin/dt)
X = linspace(0.0,1,Nx)
duree = linspace(0.0, tfin,Nt)
SX,ST = meshgrid(X,duree)

# conditions initiales et aux limites
TBarreInit = 100.0    # temp�rature initiale de la barre
TExt = 20.0           # temp�rature ext�rieure

# initialisation de la grille de calcul
T = zeros((Nt,Nx))

# Conditions initiales
for i in range(1,Nx-1):
    T[0][i] = TBarreInit

# Conditions aux limites
for t in range(0,Nt):
    T[t][0] = T[t][-1] = TExt

# sch�ma FTCS
c = dt/(dx*dx)
TT = zeros(Nx)
for t in range(0,Nt-1):          # boucle de discr�tisation temporelle
    TT[0] = TT[-1] = TExt    
    for x in range(1,Nx-1):      # boucle de discr�tisation spatiale
        TT[x] = T[t][x] + c*(T[t][x-1] - 2*T[t][x] + T[t][x+1])
    T[t+1] = TT.copy()           # recopie de T[t] dans T[t+1]  
    
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

# sauvegarde de l'image
plt.savefig('E:\PhysNumWeb1\images\EC1.png')
       

