#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 lois de distributions de probabilités
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "4 juillet 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from numpy.random import uniform
from matplotlib.pylab import figure, show, plot, grid


# loi uniform - variable aléatoire discrète
N = 100
x = uniform(0,10,N)

fig1 = figure(figsize=(14,8))
ax = fig1.add_subplot(111,autoscale_on=False, xlim=(0,1), ylim=(0,1))
grid(True)
plot(x)

show()

