# programme de tracé 3D en Python
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, title,show

# définition des vecteurs x et y
x = arange(-4,4,0.25)
y = arange(-4,4,0.25)

# ouvre la fenêtre graphique standard et récupération de son identifiant dans fig
fig = figure()

# définition du système 3D sur la figure désignée par fig
Fig3D = Axes3D(fig)
x,y = meshgrid(x,y)

# calcul de la courbe de la fonction sin(sqrt(x2 + y2))
z = sin(sqrt(x**2 + y**2))

# tracé de la courbe - voir la doc d'Axes3D pour la signification des paramètres
Fig3D.plot_surface(x,y,z,rstride=1,cstride=1)

# un titre ...
title('Courbe 3D')

# tracé des labels sur les axes
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('z')

# affiche les objets graphiques crées dans la fenêtre graphique
show()
