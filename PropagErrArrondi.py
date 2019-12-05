#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Propagation des erreurs d'arrondi
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import exp

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
        
# valeur approchée de e-10
print format(exp(-10), '.30f')

# affichage des différents termes de la série
x = 0.0
for k in range(20):
    y = (-1)**k*((10.0**k)/fact(k))
    print 'u(%d) = %.30f' % (k,y,)
    x += y
print u'résultat calculé :%.30f' % (x,)

# autre mode de calcul
for k in range(20):
    y = ((10.0**k)/fact(k))
    print 'u(%d) = %.30f' % (k,y,)
    x += y
print u'résultat calculé :%.30f' % (1.0/x,)