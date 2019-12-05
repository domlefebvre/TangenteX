#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Résolution de l'équation des télégraphistes pour une ligne avec pertes résistives
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "27 mars 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import zeros,sqrt,arange,exp,pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# paramètres physiques du système
L = 0.1             # inductance linéique
C = 2.5             # capacitance linéique
R = 1.0             # résistance linéique
c = 1.0/sqrt(L*C)

# paramètres de la simulation
dx = 0.05              # pas spatial
LX = 200               # longueur de la ligne
Alpha = 1.0           
dt = sqrt(Alpha)*dx/c  # le pas temporel est adapaté pour que la condition CFL soit vérifiée



# définition du vecteur Tension
V = zeros((LX+1,3),float)

# fonction d'initialisation
def init():
    line.set_data([],[])
    return line,

# fonction de tracé de l'animation
def animate(dum):
    i = arange(1,LX)
    V[i,2] = (1.0/(1.0 + dt*R/2*L))*(V[i+1,1] + V[i-1,1] - (1.0 - R*dt/2*L)*V[i,0])         
    line.set_data(i,V[i,2])
    V[:,0] = V[:,1]
    V[:,1] = V[:,2]
    return line,

# conditions initiales : paquet d'ondes gaussien de paramètres (mu,sigma)
# définition de l'enveloppe gaussienne
mu = 0.0
sigma = 0.5
k = 1./(sigma*sqrt(2*pi))
X = 0.0

# construction du paque d'ondes
for i in range(0,LX):
    V[i,0] = k*exp(-0.5*((X - mu)/sigma)**2)
    X += dx
    
# conditions de bords 
for i in range(1,LX):
    V[i,2] = (1.0/(1.0 + dt*R/2*L))*(V[i+1,1] + V[i-1,1] - (1.0 - R*dt/2*L)*V[i,0])
V[:,0] = V[:,1]
V[:,1] = V[:,2]
    
# tracé de l'évolution
fig = plt.figure()
ax = fig.add_subplot(111,autoscale_on=False, xlim=(0,LX),ylim=(-5.0,5.0))
plt.grid(True)
plt.title(u"Equation des télégraphistes avec pertes résistives")
plt.xlabel("X")
plt.ylabel("V(x,t)")
plt.hold("off")
line, = ax.plot([],[],lw = 2)
ani = animation.FuncAnimation(fig,animate,init_func=init,frames=5000,\
                              interval=20,blit=True)
plt.show()