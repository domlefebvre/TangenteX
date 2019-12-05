#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé d'une distribution de Cauchy
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "2 novembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace
from matplotlib.pylab import figure, title, grid, xlim,xlabel,ylabel,plot
from scipy.stats import cauchy,norm

# domaine
x_min = -10.0
x_max = 10.0
x = linspace(x_min, x_max, 500)

# paramètres de la distribution de Cauchy
x0 = 0.0    # paramètre loc
a =  2.0    # paramètre scale

# paramètres de la distribution de Gauss
mu = 0.0
sigma = 2.0

# calcul de la distribution de Cauchy et de la gaussienne correspondante
y = cauchy.pdf(x,x0,a)
Yn = norm.pdf(x,mu, sigma)

# tracé superposé de la loretzienne et de la gaussienne
fig1 = figure(figsize=(10,8))
plot(x,y,'blue')
plot(x,Yn,'red')
grid()
xlim(x_min,x_max)
title(u'Lorentzienne (bleu) et Gaussienne (rouge)',fontsize=14)
xlabel('x')
ylabel('y')

# tracé de la fonction de répartition
z = cauchy.cdf(x,x0,a)
fig2 = figure(figsize=(10,8))
plot(x,z,'blue')

xlim(x_min,x_max)
title(u'Distribution de Cauchy - Fonction de répartition',fontsize=14)
xlabel('x')
ylabel('y')

grid(which='both')