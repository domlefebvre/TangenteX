# Boite à outils Python pour le numericien
# tracé de courbes 2D
# Dominique Lefebvre pour TangenteX.com
# 10 août
#

# importation des librairies
from mpl_toolkits.mplot3d import Axes3D
from scipy import arange, meshgrid, sqrt        
from matplotlib.pyplot import *         

# Définition de la fonction scalaire
def Fonction(x,y):
    return sqrt(x**2 + y**2)
    
# Définition de la grille de calcul    
hx = 0.01
hy = 0.01
X = arange(-2,2,hx)
Y = arange(-2,2,hy)
x,y = meshgrid(X,Y)

# tracé
fig = figure()
Fig3D = Axes3D(fig)
title('Fonction z = sqrt(x^2 + y^2)')
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('sqrt(x^2 + y^2)')
Fig3D.plot_surface(x,y,Fonction(x,y),rstride=1,cstride=1)
show()


