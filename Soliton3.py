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

import numpy as np
from scipy.integrate import odeint
from scipy.fftpack import diff as psdiff  #psdiff est un alias de scipy.fftpack
from matplotlib.pylab import figure, show, meshgrid;
from mpl_toolkits.mplot3d import Axes3D ;


def kdv_exact(x, c):
    """Profile of the exact solution to the KdV for a single soliton on the real line."""
    u = 0.5*c*np.cosh(0.5*np.sqrt(c)*x)**(-2)
    return u

def kdv(u, t, L):
    """Differential equations for the KdV equation, discretized in x."""
    # Compute the x derivatives using the pseudo-spectral method.
    ux = psdiff(u, period=L)
    uxxx = psdiff(u, period=L, order=3)

    # Compute du/dt.    
    dudt = -6*u*ux - uxxx

    return dudt

def kdv_solution(u0, t, L):
    """Use odeint to solve the KdV equation on a periodic domain.
    
    `u0` is initial condition, `t` is the array of time values at which
    the solution is to be computed, and `L` is the length of the periodic
    domain."""

    sol = odeint(kdv, u0, t, args=(L,), mxstep=5000)
    return sol


if __name__ == "__main__":
    # Set the size of the domain, and create the discretized grid.
    L = 50.0
    N = 64
    dx = L / (N - 1.0)
    x = np.linspace(0, (1-1.0/N)*L, N)

    # Set the initial conditions.
    # Not exact for two solitons on a periodic domain, but close enough...
    #u0 = kdv_exact(x-0.33*L, 0.75) + kdv_exact(x-0.65*L, 0.4)
    u0 = kdv_exact(x-0.33*L, 0.75)
    
    # Set the time sample grid.
    T = 200
    t = np.linspace(0, T, 501)
    sol = kdv_solution(u0, t, L)  # sol[t,x] 

    # préparation de la grille d'affichage
    a = list(range(0, N,2))     # indice x
    b = list(range(0, 501,20))  # indice t
    X, Y = meshgrid(b,a)
    fig = figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X, Y, sol[X, Y], color = 'b')
    ax.set_xlabel('Temps')
    ax.set_ylabel('Abscisse')
    ax.set_zlabel('Amplitude')
    show()