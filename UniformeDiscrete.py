#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 lois de distribution uniforme discrète
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "20 septembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy.stats import randint
from scipy import arange
from matplotlib.pylab import figure, show, plot, grid


# loi uniform - variable aléatoire discrète
a = 1
b = 1

x = arange(randint.ppf(1.0,a,b)

fig1 = figure(figsize=(14,8))
ax = fig1.add_subplot(111,autoscale_on=False, xlim=(0,1), ylim=(0,1))
grid(True)
plot(x)

show()