#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Recherche du maximum global d'une fonction de deux variables 
 par la méthode du gradient avec choix aléatoire du pas et de
 la direction de déplacement à partir du point initial (x0,y0)
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "30 octobre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import pi, sinc, fabs
from random import gauss

# déclaration du domaine d'étude
xmin = pi; xmax = pi
ymin = pi; ymax = pi

# définition du point initial pour la recherche
x0 = -3.1
y0 = 3.1

# paramètres des tirages aléatoires    
nbtirages = 20
# loi normale centrée réduite
mu = 0.0        # moyenne de la distribution des pas
sigma = 1.0     # variance de la distribution des pas

# paramètres de l'algorithme
epsilon = 1.e-6
maxiter = 50
pas = 1.0 
   
# définition de la fonction à traiter
def Fonction(x,y):
    z = fabs(sinc(x)*sinc(y))
    return z

# méthode du gradient en partant d'un point initial (x0,y0) fixe,
# avec choix aléatoire du pas et de la direction du déplacement
def MethodeStochastique(x0,y0,pas,epsilon,maxiter):
    # initialisation
    erreur = 2.*epsilon
    x = x0;y = y0; 
    i = 0
    if (x == 0.0) and (y == 0.0):
        X = 0.0; Y = 0.0; maximum = 1.0  
    else:        
        fmax = Fonction(x,y)
        fmax1 = fmax/2.0
        # boucle principale de calcul        
        while ((erreur > epsilon) and (i < maxiter)):
            j = 0
            # boucle de choix aléatoire du pas et de la direction de déplacement 
            while (fmax1 <= fmax) and (j < nbtirages):      
                x1 = x + pas*gauss(mu, sigma)
                y1 = y + pas*gauss(mu, sigma)
                fmax1 = Fonction(x1,y1)
                j += 1
            if (fmax1 > fmax):
                x = x1;y = y1
                erreur = fabs(fmax1 - fmax)
                fmax = fmax1
            else:
                pas /= 2.0
            i += 1
        X = x; Y = y; maximum = fmax1    
    return(X,Y,maximum,i)

# recherche du maximum de la fonction
Xm,Ym,Max,nbiter = MethodeStochastique(x0,y0,pas,epsilon,maxiter)
print "Maximum : %2.3f  en (%2.3f,%2.3f) %d iterations \n" % (Max,Xm,Ym,nbiter)
