#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Suite de Muller
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 mai 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

import matplotlib.pyplot as plt

Indice = []
Valeur = []

# les variables u0 et u1 sont de type float Python ()
u0 = 2.0
u1 = -4.0

print "u( 0) = %21.20f" % u0
print "u( 1) = %21.20f" % u1

Indice.append(0);Valeur.append(u0)
Indice.append(1);Valeur.append(u1)

for i in range(1,19):
    tmp = 111.0 - 1130.0/u1 + 3000.0/(u0*u1)
    print "u(%2d) = %21.20f \n" % (i+1,tmp)
    Indice.append(i)
    Valeur.append(tmp)
    u0 = u1
    u1 = tmp

plt.figure()
plt.grid()
plt.plot(Indice, Valeur)
plt.show()