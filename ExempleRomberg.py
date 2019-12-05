#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Définition et exemple d'emploi de la méthode de Romberg """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 janvier 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import zeros, linspace

# méthode des trapèzes
def Trapeze(f,a,b,N):
    h   = (b-a)/float(N)
    xi  = linspace(a,b,N+1)
    fi  = f(xi)
    aire   = 0.0
    for i in range(1,N):
        aire += fi[i]
    aire = (h/2)*(fi[0] + fi[N]) + h*aire
    return aire 

def Romberg(fonction,a,b,eps,nmax):
    A = zeros((nmax,nmax),float)
    for i in range(0,nmax):
        N = 2**i
        A[i,0] = Trapeze(fonction,a,b,N)
        for k in range(0,i):
            n = k + 2
            A[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*A[i,k] - A[i-1,k])
        if (i > 0):
            if (abs(A[i,k+1] - A[i,k]) < eps):
               break   
    return A[i,k+1]

# définition de la fonction à intégrer
def fonction(x):
    return x**2
    
# intégration de la fonction x**2
eps = 1.0e-6      # précision souhaitée
nmax = 21         # ordre
a = 0.0; b = 1.0  # domaine d'intégration
I = Romberg(fonction,a,b,eps,nmax)
print ("Valeur integrale : "),I

