#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 résolution de l'équation de Korteweg de Vries
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import zeros, tanh
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# définition des buffers de travail
Nx = 131
U = zeros((Nx, 3), float) 

# paramètres de la simulation
dx = 0.4   # pas spatial
dt = 0.1   # pas temporel
mu = 0.1
fac = mu*dt/dx**3
eps = 0.2 

k = range(0,Nx)


# onde initiale
X = 0.0
for i in range(0,Nx):
    U[i,0] = 0.5*(1 - tanh(X/5. - 5.))
    X += dx       

# conditions de Dirichlet
U[0,1] = 1. ; U[0,2] = 1.; 
U[Nx-1,1] = 0. ; U[Nx-1,2] = 0. 
 

# initialisation du calcul
for  i in range (1, Nx-1):                              
    a1 = eps*dt*(U[i + 1, 0] + U[i, 0] + U[i - 1, 0])/(dx*6.)
    if i > 1 and  i < Nx-2: 
       a2 = U[i+2,0] + 2.*U[i-1,0] - 2.*U[i+1,0] - U[i-2,0]
    else: 
       a2 = U[i-1, 0] - U[i+1, 0]
    a3 = U[i+1, 0] - U[i-1, 0]
    U[i, 1] = U[i, 0] - a1*a3 - fac*a2/3.

# fonction de tracé de l'animation
def animate(dum):
    for  i in range (1, Nx-2): 
         a1 = eps*dt*(U[i + 1, 1] + U[i, 1] + U[i - 1, 1])/(dx*3.)
         if i > 1 and i < Nx-2: 
            a2 = U[i+2,1]+2.*U[i-1,1]-2.*U[i+1,1]-U[i-2,1]
         else: 
            a2 = U[i-1, 1] - U[i+1, 1]
         a3 = U[i+1, 1] - U[i-1, 1]
         U[i, 2] = U[i, 0] - a1*a3 - 2.*fac*a2/3.
    # sauvegarde des résultats
    line.set_data(k,U[:,2])
    # permutation des buffers     
    U[:, 0] = U[:, 1]
    U[:, 1] = U[:, 2]
    return line,

# tracé de l'évolution
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111,autoscale_on=False, xlim=(0,Nx), ylim=(-3,3))
plt.grid(True)
plt.title(u"Equation de Korteweg de Vries")
plt.xlabel("X")
plt.ylabel("U(x,t)")
plt.hold("off")
line, = ax.plot(k,U[k,0])

ani = animation.FuncAnimation(fig,animate,frames=1000,interval=20,blit=True)

plt.show()

