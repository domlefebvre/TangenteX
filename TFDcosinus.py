# -*- coding: utf-8 -*-
# Programme de tracé d'une courbe cosinus
# Dominique Lefebvre pour TangenteX.com
# 2 avril 2016

# importation des librairies
import matplotlib.pyplot as plt
from scipy import arange, cos

# vecteur temps discrétisé
t0 = 0.0
tf = 10.0
pas = 0.1
t = arange(t0,tf,pas)

plt.xlim(t0,tf)
plt.ylim(-1,1)

# affichage de la courbe
fig = plt.figure(figsize=(14,8))
ax.set_xlabel('t', fontsize = 16)
ax.set_ylabel('V', fontsize = 16)

#plt.plot(t,cos(t),'blue')
plt.scatter(t,cos(t))

plt.show()

