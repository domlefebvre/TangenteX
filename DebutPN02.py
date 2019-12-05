# -*- coding: Latin-1 -*-
# DebutPN02 : programme de d�monstration du trac� d'une courbe z =f(x,y)
# Dominique Lefebvre pour TangenteX.com
# 27 mai 2017
#

# importation des librairies
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# d�finition de la fonction sinus cardinal
def f(x,y): 
    try:
        r = (x**2 + y**2)        
        sinc = np.sin(r) / r
    # prolongement par continuit� pour x = 0    
    except ZeroDivisionError:
        sinc = 1.0
    return sinc
    
# domaine de d�finition du trac� graphique
xmin = ymin = -2*np.pi
xmax = ymax = 2*np.pi
nbpoint = 100
x = np.linspace(xmin, xmax,nbpoint)
y = np.linspace(ymin, ymax,nbpoint)

# construction de la grille de trac�
X,Y = np.meshgrid(x,y)

# calcul de f(x)
Z = f(X,Y)

# d�finition du r�f�rentiel 3D
fig = plt.figure()
Fig3D = Axes3D(fig)

# d�finition des limites d'affichage du graphe
Fig3D.set_xlim(xmin, xmax)
Fig3D.set_ylim(min(y),max(y))
#titre de la figure
plt.title('Fonction sinus cardinal z = f(x,y)')
# libell�s des axes
Fig3D.set_xlabel('x')
Fig3D.set_ylabel('y')
Fig3D.set_zlabel('z = f(x,y)')
# trac� de la courbe
Fig3D.plot_surface(X,Y,Z,rstride=1,cstride=1,linewidth=0,
                   antialiased=False,cmap=plt.cm.Reds)
plt.show()