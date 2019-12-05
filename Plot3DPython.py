# programme de trac� 3D en Python
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, title,show

# d�finition des vecteurs x et y
x = arange(-4,4,0.25)
y = arange(-4,4,0.25)

# ouvre la fen�tre graphique standard et r�cup�ration de son identifiant dans fig
fig = figure()

# d�finition du syst�me 3D sur la figure d�sign�e par fig
Fig3D = Axes3D(fig)
x,y = meshgrid(x,y)

# calcul de la courbe de la fonction sin(sqrt(x2 + y2))
z = sin(sqrt(x**2 + y**2))

# trac� de la courbe - voir la doc d'Axes3D pour la signification des param�tres
Fig3D.plot_surface(x,y,z,rstride=1,cstride=1)

# un titre ...
title('Courbe 3D')

# trac� des labels sur les axes
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('z')

# affiche les objets graphiques cr�es dans la fen�tre graphique
show()
