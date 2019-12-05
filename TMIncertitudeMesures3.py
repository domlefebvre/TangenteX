# -*- coding: utf-8 -*-

# programme de tracé d'une courbe gaussienne
# Dominique Lefebvre
# TangenteX.com
# 8 octobre 2016

# importation des librairies
from scipy import arange
import matplotlib.pyplot as plt
import scipy.stats as stats

# tracé de la loi normale centrée réduite
mu = 0
sigma = 1
x = arange(-10.0,10.0,0.0001)
y = stats.norm.pdf(x,mu,sigma)

# Affichage de l'histogramme
fig = plt.figure()
plt.plot(x,y,'blue')
plt.xlabel('x')
plt.ylabel('G(x)')
plt.xticks(arange(-10.0,10.0,1.))
plt.grid(True)

plt.show()