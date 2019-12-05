# -*- coding: Latin-1 -*-
# programme BOintegrationSinus
# Dominique Lefebvre pour www.tangenteX.com
# le 5 aout 2015

#Appel des librairies
from scipy import sin, pi
from scipy.integrate import quad

# Définition de la fonction à intégrer
def f(x):
    return sin(x)

# intégration
t = quad(f,0,pi/2)[0]
print 'integrale entre 0 et PI/2 de sin(x) : ',t





