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

from scipy.stats import poisson
from matplotlib.pylab import figure, title, xlabel,ylabel,hist

# paramètres de la distribution de Poisson
Lambda = 10.0
nbtirage = 10000

# calcul de la distribution discrète
y = poisson.rvs(Lambda, size=nbtirage)

# paramètres de l'histogramme
NbClasses = 50
Xmin = 0
Xmax = 20

# tracé de la distribution de Poisson
fig2 = figure(figsize=(10,8))
hist(y, bins=NbClasses, range=(Xmin,Xmax), normed=True)
title(u'Distribution de Poisson',fontsize=14)
xlabel(u'Evènements')
ylabel(u'Probabilité')

