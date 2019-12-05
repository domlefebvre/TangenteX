#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé de la densité de probabilité guassienne
 Comparaiosn de la fonction norm() de scipy et la transformation de Box-Muller
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "&2 novembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace, arange, pi, log, sin, cos, sqrt, random
from matplotlib.pylab import figure, title, grid, xlim,xlabel,ylabel,plot, xticks,yticks
from scipy.stats import norm

# Transformation de Box_Muller
def Box_Muller(x1,x2):
  g1 = sqrt(-2*log(x1))*cos(2*pi*x2)
  g2 = sqrt(-2*log(x1))*sin(2*pi*x2)
  return g1,g2

# domaine
x_min = -10.0
x_max = 10.0
x = linspace(x_min, x_max, 200)

# paramètre de la distribution
mu = 0.0      # moyenne
sigma = 1.0   # écart type

# calcul de la distribution de Laplace-Gauss - densité de probabilité par scipy
y = norm.pdf(x,mu,sigma)

# calcul de la distribution gaussienne par Box-Muller
x1 = random.random(200)
x2 = random.random(200)
g1,g2 = Box_Muller(x1,x2)

# tracé de la fonction de densité de probabilité
fig1 = figure(figsize=(10,8))
plot(x,y,'blue')
plot(g1,g2,'red')

xlim(x_min,x_max)
title(u'Distribution de Laplace-Gauss - Densité de probabilité',fontsize=14)
xlabel('x')
ylabel('y')
x_major_ticks = arange(x_min, x_max,1.0)
y_major_ticks = arange(0.0,0.5,0.05)
xticks(x_major_ticks)
yticks(y_major_ticks)
grid(which='both')
