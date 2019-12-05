#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé d'une distribution exponentielle
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "2 novembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace
from matplotlib.pylab import figure, title, grid, xlim,xlabel,ylabel,plot
from scipy.stats import expon

# domaine
x_min = 0.0
x_max = 10.0
x = linspace(x_min, x_max, 500)

# paramètres de la distribution exponentielle
Lambda = 1.0

# calcul de la distribution exponentielle
y = expon.pdf(x,scale = 1./Lambda)   # densité de probabilité
Y = expon.cdf(x,scale = 1./Lambda)   # fonction de répartition

# tracé de la densité de probabilité
fig1 = figure(figsize=(10,8))
plot(x,y,'blue')
grid()
xlim(x_min,x_max)
title(u'Distribution exponentielle - Densité de probabilité',fontsize=14)
xlabel('x')
ylabel('y')

# tracé de la fonction de répartition
fig2 = figure(figsize=(10,8))
plot(x,Y,'blue')
xlim(x_min,x_max)
title(u'Distribution exponentielle - Fonction de répartition',fontsize=14)
xlabel('x')
ylabel('y')

grid(which='both')