#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Calcul du développement limité d'une fonction """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "20 aout 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from sympy import *

# Fonction de calcul d'un développement limité
def DevLimite(fonc,variable,x0,ordre):
    """ Fonction de calcul du développement limité
        fonc     : fonction dont on cherche le DL
        variable : nom de la variable
        x0       : point au voisinage duquel on calcule le DL
        ordre    : ordre du DL
    """
    return (series(fonc,variable,x0,ordre+1))
    
# définition des variables
x = symbols('x')

# paramètres du DL
fonction = 'tan(x)'  # fonction à développer
x0 = 0               # DL au voisinage de 0
ordre = 4            # DL d'ordre 3

# calcul du DL
DL=DevLimite(fonction,x,x0,ordre)
print(DL)



