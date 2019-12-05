#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé d'une distribution gaussienne
 fonction de densité de probabilité et fonction de répartition
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "2 novembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace, arange
from matplotlib.pylab import figure, title, grid, xlim,xlabel,ylabel,plot, xticks,yticks
from scipy.stats import norm

# domaine
x_min = -10.0
x_max = 10.0
x = linspace(x_min, x_max, 200)

# paramètre de la distribution
mu = 0.0      # moyenne
sigma = 1.0   # écart type

# calcul de la distribution de Laplace-Gauss - densité de probabilité
y = norm.pdf(x,mu,sigma)

# calcul de la fonction de répartition
z = norm.cdf(x,mu,sigma)

# tracé de la fonction de densité de probabilité
fig1 = figure(figsize=(10,8))
plot(x,y,'blue')

xlim(x_min,x_max)
title(u'Distribution de Laplace-Gauss - Densité de probabilité',fontsize=14)
xlabel('x')
ylabel('y')
x_major_ticks = arange(x_min, x_max,1.0)
y_major_ticks = arange(0.0,0.5,0.05)
xticks(x_major_ticks)
yticks(y_major_ticks)
grid(which='both')

# fonctionde répartition
fig2 = figure(figsize=(10,8))
plot(x,z,'blue')

xlim(x_min,x_max)
title(u'Distribution de Laplace-Gauss - Fonction de répartition',fontsize=14)
xlabel('x')
ylabel('y')
x_major_ticks = arange(x_min, x_max,1.0)
y_major_ticks = arange(0.0,1.0,0.1)
xticks(x_major_ticks)
yticks(y_major_ticks)
grid(which='both')