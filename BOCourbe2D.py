# Boite � outils Python pour le numericien
# trac� de courbes 2D
# Dominique Lefebvre pour TangenteX.com
# 29 juillet 2015
#

# importation des librairies
from mpl_toolkits.mplot3d import Axes3D
from scipy import arange, meshgrid,sin, pi         # import des fonctions et constantes utilis�es
from matplotlib.pyplot import *                    # fonction de trac� de courbe

# d�finition des vecteurs x et y
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

# ouvre la fen�tre graphique standard et r�cup�ration de son identifiant dans fig
fig = figure()
# d�finition du syst�me 3D sur la figure d�sign�e par fig
Fig3D = Axes3D(fig)

# Titre et l�gende des axes
title('Fonction z = sin(x^2 + y^2)')
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('sin(x^2 + y^2)')

# trac� de la courbe
Fig3D.plot_surface(x,y,z,rstride=1,cstride=1, color = 'r')

# affiche les objets graphiques cr�es dans la fen�tre graphique
show()


