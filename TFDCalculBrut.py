# -*- coding: utf-8 -*-
# Programme de calcul brut de la TFD d'un signal échantillonné par
# Dominique Lefebvre pour TangenteX.com
# 6 avril 2016

# importation des librairies
import matplotlib.pyplot as plt
from scipy import sin, pi, zeros, exp, arange
import time

# définition du signal à traiter
# Fmax = 20 Hz 
# dF = 0.1 Hz  résolution en fréquence de l'analyse spectrale
Fe = 40.0      # fréquence d'échantillonnage
dF = 0.1       # résolution fréquentielle

# le nombre d'échantillons est déterminé par la résolution fréquentielle
# hypothèse N = L
N = int(Fe/dF)  # nombre d'échantillons

# la durée du signal à analyser (la période d'échantillonnage Te) dépend du
# nombre d'échantillons à acquérir et de la fréquence d'échantillonnage
# Te = N/Fe d'où Te = 1/dF
Te = 1.0/dF                 # durée du signal à échantillonner

# construction du signal échantillonné s
t = arange(0.0,Te,Te/N)     # vecteur temps discrétisé
A0 = 5.0; F0 = 10.0         # amplitude et fréquence de la sinusoïde
A1 = 2.0; F1 = 5.0
s = A0*sin(2.0*pi*F0*t) + A1*sin(2.0*pi*F1*t)

# construction du vecteur fréquence
f = dF*arange(N)

# boucle de calcul de la TFD
X = zeros(N,dtype= complex) # définition du vecteur spectral
ex = -2j*pi/N               # part invariable de l'exposant 

tdebut = time.time()
for k in range(0,N-1):
    y = 0.0
    for n in range(0,N-1):
        y += s[n]*exp(ex*n*k)
    X[k] = y 
print 'Temps de calcul (s) : ',time.time() - tdebut

# calcul du spectre SP normalisé
FacteurNorm = 2.0/N
SP = FacteurNorm * abs(X)

# affichage des résultats
fig = plt.figure(figsize=(14,8))
# affichage du spectre
plt.xlabel('frequence', fontsize = 16)
plt.ylabel('amplitude', fontsize = 16)
plt.plot(f,SP)

plt.show()

