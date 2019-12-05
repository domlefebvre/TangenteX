#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé d'une distribution de Maxwell
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "2 novembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import linspace
from matplotlib.pylab import figure, title, grid, xlim,xlabel,ylabel,plot
from scipy.stats import maxwell

# domaine
x_min = 0.0
x_max = 10.0
x = linspace(x_min, x_max, 500)

# calcul de la distribution de Maxwell
y = maxwell.pdf(x)

# tracé de la distribution
fig1 = figure(figsize=(10,8))
plot(x,y,'blue')
grid()
xlim(x_min,x_max)
title(u'Distribution de Maxwell',fontsize=14)
xlabel('x')
ylabel('y')