#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Définition et exemple d'emploi de la méthode de Simpson """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 janvier 2019" 
__email__       = "dominique.lefebvre@tangentex.com"


def Simpson(f,a,b,n):
    # vérification de la parité du nombre de pas
    if n % 2 != 0 :
        return -1
    else :        
        h=(b-a)/float(n)
        sum1=(f(a)+f(b))/6.0
        for i in range(1,n) :
           sum1 += f(a+i*h)/3.0
        for i in range(n) :
           sum1 += f(a+(2*i+1)*h/2.0)*2.0/3.0
    I = h*sum1
    return I

# définition de la fonction à intégrer
def fonction(x):
    return x**2
    
# intégration de la fonction x**2
pasint = 1000
a = 0.0; b = 1.0  # domaine d'intégration
I = Simpson(fonction,a,b,pasint)
print ("Valeur integrale : "),I

