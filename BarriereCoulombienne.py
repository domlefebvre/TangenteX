# -*- coding: Latin-1 -*-
# programme de calcul de la barri�re coulombienne entre
# deux noyaux
# Dominique Lefebvre pour TangenteX.com
# 15 septembre 2017
#

# importation des librairies
from scipy import pi

import matplotlib.pyplot as plt

# Constantes physiques
e = 1.60218e-19    # charge �l�mentaire en Coulomb
kb = 1.38066e-23   # constante de Boltzmann en J/K
h = 6.626076e-34   # constante de Planck en J.s
eps0 = 8.85419e-12 # permittivit� du vide en C2.N-1.m-2
c = 2.99792458e8   # vitesse de la lumi�re dans le vide en m/s

# Coefficients physiques
CKeV = e/kb        # coefficient de conversion K <-> eV

# fonctions de conversion d'unit�
def JouleToeV (joule):
    eV = joule/e
    return eV

def eVToJoule(ev):
    joule = ev*e
    return joule
    
def eVToK(eV):
    K = eV*CKeV
    return K
    
def KToeV(K):
    eV = K/CKeV
    return eV

# d�finition des interactions
def PotInterCoulomb(q1,q2,r):
    V = (1./(4*pi*eps0))*(q1*q2/r)
    return V
    
# autres fonctions de calcul

# calcul du bilan d'�nergie de masse d'une r�action nucl�aire
# Mp = masse du noyau p�re
# Mf = masse du noyau fils
# Mn = masse des neutrons g�n�r�s    
def Q(Mp,Mf,Mn):
    q = (Mp - Mf - Mn)*c^2
    return q
    
# calcul de la densit� du noyau en fonction de la distance
def DensiteNoyau(r):
    d = rho0/(1 +exp((r - R))/a)
    return d
    
