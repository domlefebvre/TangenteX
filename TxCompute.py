#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Routines de calcul pour la physique numérique
    Le module TxCompute comprend des routines :
    - intégration (méthode de Simpson)
    - résolution d'EDO d'ordre 1 et 2 par Euler et RK4
    - recherche de zéros d'une fonction (Newton Raphson)
    - interpolation
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "16 mai 2018" 
__email__       = "dominique.lefebvre@tangentex.com"


from scipy import array

#
# Routines d'intégration d'une fonction
#

def Simpson(fonc, a, b, pas):
    """ Intégration d'une fonction fonc par la méthode de Simpson
        fonc : nom de la routine qui définit la fonction à intégrer
        a,b  : bornes inférieure et supérieure d'intégration
        pas    : pas d'intégration
    """
    if a > b:
        print 'les bornes d''intégration sont incorrectes'
        return None
    if pas%2 != 0:
        print 'Le pas d''intégration doit être pair'
        return None
    else:
    	h = (b - a)/float(pas)
    	sum1 = 0
    	for i in range(1, pas/2 + 1):
        	sum1 += fonc(a + (2*i - 1)*h)
    	sum1 *= 4
    	sum2 = 0
    	for i in range(1, pas/2):  
        	sum2 += fonc(a + 2*i*h)
    	sum2 *= 2
    	approx = (b - a)/(3.0*pas)*(fonc(a) + fonc(b) + sum1 + sum2)
    	return approx

#
# Routines d'intégration d'un système différentiel d'ordre 1
#

def EulerSys1 (DXDT, dom, x0, h):
    """
    EulerSys1 intégre le système d'EDO d'ordre 1 avec les paramètres
    suivants:
    - DXDT : désigne la dérivée de la fonction
    - dom : désigne le domaine d'intégration du système
    - x0 : conditions initiales du système
    - h : pas d'intégration sur le domaine
    La fonction retourne une liste contenant la courbe intégrale    
    """
    xi = []    
    r = array([x0])
    for t in dom:
        xi.append(r[0])
        r += DXDT(r)*h 
    return (xi)
    
    
def RK4Sys1(fonction, dom, x0, h):
    """
    RK4Sys1 intégre le système d'EDO d'ordre 1 avec les paramètres
    suivants:
    - fonction : désigne la fonction de définition du système
    - dom : désigne le domaine d'intégration du système
    - x0 : conditions initiales du système
    - h : pas d'intégration sur le domaine   
    La fonction retourne une liste contenant la courbe intégrale
    """
    xi = []    
    r = array([x0])
    for t in dom:
        xi.append(r[0])
        k1 = h*fonction(r,t)
        k2 = h*fonction(r + k1/2.0, t + h/2.0)
        k3 = h*fonction(r + k2/2.0, t + h/2.0)
        k4 = h*fonction(r + k3, t + h)
        r += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0  
    return (xi)

#    
# Routines d'intégration d'un système différentiel d'ordre 2
#
    
def RK4Sys2(fonction, dom, x0, y0, h):
    """
    RK4Sys2 intégre le système d'EDO d'ordre 2 avec les paramètres
    suivants:
    - fonction : désigne la fonction de définition du système
    - dom : désigne le domaine d'intégration du système
    - x0, y0 : conditions initiales du système
    - h : pas d'intégration sur le domaine
    
    La fonction retourne deux listes contenant les (xi,yi) de la
    courbe intégrale
    """
    xi = [];yi = []    
    r = array([x0,y0])
    for t in dom:
        xi.append(r[0])
        yi.append(r[1])    
        k1 = h*fonction(r,t)
        k2 = h*fonction(r + k1/2.0, t + h/2.0)
        k3 = h*fonction(r + k2/2.0, t + h/2.0)
        k4 = h*fonction(r + k3, t + h)
        r += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return (xi,yi)
    

