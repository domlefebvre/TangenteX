# Boite à outils Python pour le numericien
# tracé de courbes 2D
# Dominique Lefebvre pour TangenteX.com
# 29 juillet 2015
#

# importation des librairies
from mpl_toolkits.mplot3d import Axes3D
from scipy import arange, meshgrid,sin, pi         # import des fonctions et constantes utilisées
from matplotlib.pyplot import *                    # fonction de tracé de courbe

# définition des vecteurs x et y
xmin = -pi/2.0
xmax = pi/2.0
ymin = xmin
ymax = xmax
pas = 0.1
x = arange(xmin, xmax, pas)
y = arange(ymin, ymax, pas)

# calcul de la courbe de la fonction
x,y = meshgrid(x,y)
z = sin(x**2 + y**2)

# ouvre la fenêtre graphique standard et récupération de son identifiant dans fig
fig = figure()
# définition du système 3D sur la figure désignée par fig
Fig3D = Axes3D(fig)

# Titre et légende des axes
title('Fonction z = sin(x^2 + y^2)')
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('sin(x^2 + y^2)')

# tracé de la courbe
Fig3D.plot_surface(x,y,z,rstride=1,cstride=1, color = 'r')

# affiche les objets graphiques crées dans la fenêtre graphique
show()


