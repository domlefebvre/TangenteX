#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" construction d'un paquet d'ondes """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "4 septembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import sin, cos, arange, sinc
from matplotlib import pyplot, animation
    
# fonction d'animation
def traceframe(i):
	courbe.set_ydata(mescourbes[i])
	return courbe,
 
# paramètres de l'expérience
Psi0 = 0.5       # amplitude initiale 
xmin = 0.0
xmax = 50.0
dx = 0.1
t0 = 0.0
tmax = 500.0
dt = 0.1
x = arange(xmin, xmax, dx)
temps = arange(t0, tmax,dt)

# calcul d'une superposition de deux OPPH en milieu non dispersif
omega0 = 1000.0
domega = 1.0
k0 = 0.5
dk = 0.01
#mescourbes=[[2*Psi0*cos(domega*t - dk*xi)*cos(omega0*t - k0*xi) for xi in x] for t in temps]

# calcul d'un paquet d'ondes
mescourbes=[[2*Psi0*sinc(domega*t - dk*xi)*cos(omega0*t - k0*xi) for xi in x] for t in temps]

# tracé de l'animation
fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, xmax), ylim=(-1.0, 1.0))
courbe, =ax.plot(x,mescourbes[0])
line_ani = animation.FuncAnimation(fig, traceframe, 100, interval=50, repeat=True)
pyplot.show()

