# -*- coding: Latin-1 -*-
# programme de calcul effet de serre - CO2
# deux noyaux
# Dominique Lefebvre pour TangenteX.com
# 18 octobre 2017
#

# importation des librairies
from scipy import pi, sqrt

# Constantes physiques
c = 2.99792458e8   # vitesse de la lumière dans le vide en m.s-1
k = 1.42e3         # coefficient de la raideur de la liaison C=O en N.m-1
mO = 2.66e-26      # masse de l'atome d'oxygène en kg
mC = 1.99e-26      # masse de l'atome de carbone en kg
r0 = 0.166e-9      # longueur de liaison C=O
C = 7.70e-19       # en Joules

# calcul des pulsations propres d'une molécule de CO2 en mouvement longitudinal
omega1 = sqrt(k/mO)
omega2 = sqrt( (k/mO) + (2*k/mC))
print "Pulsations propres omega1 (en rad.s-1) = ", omega1
print "Pulsations propres omega2 (en rad.s-1) = ", omega2

# calcul des longueurs d'onde en mouvement longitudinal
lambda1 = 2*pi*c/omega1
lambda2 = 2*pi*c/omega2
print "Longueur d'onde lambda1 (en micromètres) = ", lambda1*1e6
print "Longueur d'onde lambda2 (en micromètres) = ", lambda2*1e6

# calcul de la plusation et de la longueur d'onde en mode de flexion
omegaF = sqrt((2*C/(r0*r0))*((1/mO) + (2/mC)))
print "Pulsation propre en mode de flexion", omegaF
lambdaF = 2*pi*c/omegaF
print "Longueur d'onde lambdaF (en micromètres) = ", lambdaF*1e6