# -*- coding: Latin-1 -*-
# Programme de résolution de l'équation de chaleur adimensionnée
# par couple d'EDO
# Dominique Lefebvre pour TangenteX.com
# 28 janvier 2016
#

# importation des librairies
from scipy.integrate import odeint
from scipy import ones, meshgrid, zeros,linspace
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D


# Définition de la fonction de résolution du système
def Xdiscret(T,t):
    # initialisation
    dTdt = zeros(X.shape)
    # calcul sur le segment
    dTdt[1:-1] = (T[:-2] - 2*T[1:-1] + T[2:]) / dx**2    
    return dTdt
    
# paramètres de l'expérience
L = 1.0
tfin = 0.2
# pas de discrétisation
dx = 0.01
dt = 1.0e-4
       
# déclaration des buffers de travail
Nx = int(L/dx)
Nt = int(tfin/dt)
# déclaration des buffers de travail
t = linspace(0.0,tfin,Nt)
X = linspace(0,L,Nx)
SX,ST = meshgrid(X,t)

# définition des conditions initiales et des conditions aux limites
TBarreInit = 100.0   # température initiale de la barre
TExt = 20.0           # température extérieure
init = TBarreInit*ones(X.shape)  
init[0] = init[-1] = TExt    

# résolution du système d'EDO
Tevol = odeint(Xdiscret, init,t)

# affichage de l'évolution de la température
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X', fontsize = 16)
ax.set_ylabel('temps', fontsize = 16)
ax.set_zlabel('temperature', fontsize = 16)
ax.view_init(elev=15, azim = 120)

norm = colors.Normalize(TExt,TBarreInit)
ax.plot_surface(SX,ST,Tevol,cstride=1,linewidth=0,cmap='jet')
cb = fig.colorbar(p,ax = ax)

# sauvegarde de l'image
plt.savefig('E:\PhysNumWeb1\images\EC2.png')
       

