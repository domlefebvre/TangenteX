#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Routines d'intégration des EDO """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "20 juillet 2018" 
__email__       = "dominique.lefebvre@tangentex.com"


from scipy import zeros,arange

# définition du vecteur temps de l'expérience
def VecteurTemps(t0, tmax, pas):
    """ Définition du vecteur temps pour une expérience
        t0   : temps initial en s
        tmax : temps final en s
        pas  : pas de temps en s
    """
    time = arange(t0, tmax, pas)
    return time

# Méthode d'Euler
def Euler(fonction,y0,t):
    """ Intégration d'une EDO du premier ordre par la méthode d'Euler
        fonction : EDO à intégrer
        y0 : valeur initiale 
        t : vecteur variable d'intégration 
    """
    # détermination des paramètres d'intégration nombre de pas (n) et
    # intervalle entre deux pas (h)
    n = len(t)
    h = t[1]-t[0]
    # initialisation du vecteur de retour
    y = zeros(n)
    y[0] = y0   
    # calcul du vecteur de retour
    for i in range(n-1):
        y[i+1] = y[i] + fonction(y[i], t[i]) * h
    return y
    

# Méthode de Runge-Kutta d'ordre 4
def RK4(fonction,y0,t):
    """ Intégration d'une EDO du premier ordre par la méthode de Rung-Kutta d'ordre 4
        fonction : EDO à intégrer
        y0 : valeur initiale 
        t : vecteur variable d'intégration 
    """
    # détermination des paramètres d'intégration nombre de pas (n) et
    # intervalle entre deux pas (h)
    n = len(t)
    h = t[1]-t[0]    
    # initialisation du vecteur de retour
    y = zeros(n)
    y[0] = y0     
    # calcul du vecteur de retour
    for i in range(n-1):
        k1 = fonction(y[i],t[i])
        k2 = fonction(y[i]+k1/2.,t[i]+h/2.0)
        k3 = fonction(y[i]+k2/2., t[i]+h/2.0)
        k4 = fonction(y[i]+k3, t[i]+h)
        y[i+1] = y[i] + h * (k1 + 2. * k2 + 2. * k3 + k4) / 6.
    return y  