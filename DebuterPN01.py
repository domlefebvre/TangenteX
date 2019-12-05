# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:29:12 2017

@author: dominique
"""
from cmath import sqrt

# definition de la fonction de calcul
def RacinesPolynome(a,b,c):
    # calcul du discriminant
    delta = b**2 - 4*a*c
    # calcul des racines
    s1 = (-b + sqrt(delta))/(2.*a)
    s2 = (-b - sqrt(delta))/(2.*a)
    return s1,s2
    
# saisie des coefficients
a = input("a = ")
b = input("b = ")
c = input("c = ")

# calcul
s1,s2 = RacinesPolynome(float(a),float(b),float(c))

# affichage des solutions
print "s1 : ",s1
print "s2 : ",s2