# -*- coding: Latin-1 -*-
# Intégration d'une fonction par la méthode de Monte-Carlo
# Dominique Lefebvre pour TangenteX.com
# 31 juillet 2017

from scipy import sin,fabs,linspace
from numpy.random import *
import matplotlib.pyplot as plt

# Fonction à intégrer
def f(x):
    return x*(1-x)*sin(200*x*(1-x))**2
    
    
# fonction d'intégration par la méthode de Monte-Carlo - algo pierre
def IntMonteCarlo(f,xmin,xmax,dx,dy,n):
    AireRect = dx*dy
    compteur = 0
    for i in range(n):
        x = xmin + dx*random()
        y = ymin + dy*random()
        if fabs(y) <= fabs(f(x)):
            if f(x) > 0 and y > 0 and y <= f(x):
               compteur += 1
            if f(x) < 0 and y < 0 and y >= f(x):
               compteur -= 1
    aire = AireRect * float(compteur)/float(n)   
    return aire

# Intégration MC - algo de la moyenne
def IntMonteCarloMean(f,xmin,xmax,n):
    x = uniform(xmin, xmax,n)
    s = sum(f(x))
    A = ((xmax-xmin)/n)*s
    return A
    
# définition du domaine
xmin = 0.0
xmax = 1.0
ymin = 0.0
ymax = 0.25
x = linspace(xmin, xmax, 1000)

# intégration par Monte-Carlo
dx = xmax-xmin
dy = ymax-ymin
n = 5000

aire = IntMonteCarlo(f,xmin,xmax,dx,dy,n)
print 'aire (Monte-Carlo) : ',aire
aire1 = IntMonteCarloMean(f,xmin,xmax,n)
print 'aire (Mean) : ',aire1

# affichage de la courbe à intégrer
plt.figure()
plt.grid(True)
plt.xlim(xmin,xmax)
plt.plot(x,f(x),'b')
plt.show()    


