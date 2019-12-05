#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Recherche du maximum global d'une fonction de deux variables 
 par la méthode du gradient avec point initial fixe
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "23 octobre 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

from scipy import hypot, pi, sinc, fabs

# déclaration du domaine d'étude
xmin = pi; xmax = pi
ymin = pi; ymax = pi

# définition du point initial pour la recherche
x0 = 0.0
y0 = 2.4
    
# définition de la fonction à traiter
def Fonction(x,y):
    z = fabs(sinc(x)*sinc(y))
    return z

# méthode du gradient en partant d'un point initial (x0,y0) fixe,
# déterminé par l'utilisateur
def MethodeGradientPF(x0,y0,pas,epsilon,maxiter):
    erreur = 2.*epsilon
    x = x0;y = y0; i = 0
    if (x == 0.0) and (y == 0.0):
        X = 0.0; Y = 0.0; maximum = 1.0  
    else:        
        fmax = Fonction(x,y)
        while ((erreur > epsilon) and (i < maxiter)):
            dx = Fonction(x + pas, y) - Fonction(x - pas, y)
            dy = Fonction(x, y + pas) - Fonction(x, y - pas)
            gradF = hypot(dx,dy)        
            x1 = x + pas*dx/gradF
            y1 = y + pas*dy/gradF
            fmax1 = Fonction(x1,y1)
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
epsilon = 1.e-6
maxiter = 50
pas = 1.0
Xm,Ym,Max,nbiter = MethodeGradientPF(x0,y0,pas,epsilon,maxiter)
print "Maximum : %2.3f  en (%2.3f,%2.3f) %d iterations \n" % (Max,Xm,Ym,nbiter)
