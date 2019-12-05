#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Exemple d'utilisation de la FFT avec Python
    FFT et gaussienne
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "16 janvier 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import linspace, sin, pi,sqrt,exp, arange
from scipy.fftpack import fft,fftfreq
from matplotlib.pyplot import *


# définition d'une gaussienne
def gaussienne(x,sigma,mu):
    g = (1.0/(sigma*sqrt(2*pi)))*exp(-(x - mu)**2/(2*sigma**2))
    return g


# paramètres de la gaussienne
mu = 0.0
sigma = 2.0
    
# définition des paramètres de la FFT
N = 1024 

# domaine de la fonction
xmin = -10.0
xmax = 10.0

x = linspace(xmin, xmax, N)

# construction de la fonction
f = gaussienne(x,sigma,mu)

# calcul de la FFT normalisée
FFT = abs(fft(f))/N
fx = fftfreq(N)

# affichage de la transformée de Fourier
figure(1)

subplot(2,1,1)
xlim(x.min(), x.max())
ylim(f.min(),f.max())
xlabel('x')
ylabel('f(x)')
grid()
plot(x,f,'g')

subplot(2,1,2)
xlim(x.min(), x.max())
ylim(FFT.min(),FFT.max())
xlabel('x')
ylabel('FFT')
grid()
plot(x,FFT,'b')

show()
