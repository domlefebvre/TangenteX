#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Tracé d'un diagramme de Bode
"""
__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "5 décembre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import arange, angle, log, absolute
from matplotlib.pylab import figure, subplot,semilogx,grid


# Définition de la fonction de transfert
def H(w):
    return 1/(1 + 0.01*1j*w - w*w)

# Découpage régulier des puissances en base 10 de la pulsation ici de 10^-2 à 10^3
puissance_w = arange(-2,3,0.01)

# Les pulsations w
W = 10**puissance_w
# La phase en degré
phase = angle(H(W),'deg')
# Le module en dB
module = 20*log(absolute(H(W)))

#Tracer du diagramme de Bode
fig1 = figure(figsize=(10,8))
subplot(211) 
semilogx(W,module)  
grid(True) 
subplot(212)
semilogx(W,phase)  
grid(True)   
