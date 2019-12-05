# -*- coding: Latin-1 -*-
# DebutPN01 : programme de démonstration du tracé d'une courbe y =f(x)
# Dominique Lefebvre pour TangenteX.com
# 26 mai 2017
#

# importation des librairies
import numpy as np
import matplotlib.pyplot as plt

# définition de la fonction sinus cardinal
def f(x): 
    try:
        sinc = np.sin(x) / x
    # prolongement par continuité pour x = 0    
    except ZeroDivisionError:
        sinc = 1.0
    return sinc
    
# domaine de définition du tracé graphique
xmin = -6*np.pi
xmax = 6*np.pi
nbpoint = 600
x = np.linspace(xmin, xmax,nbpoint)

# calcul de f(x)
y = f(x)

# tracé de y = f(x)

# définition des limites d'affichage du graphe
plt.xlim(xmin, xmax)
plt.ylim(min(y),max(y))
#titre de la figure
plt.title('Fonction sinus cardinal')
# libellés des axes
plt.xlabel('x')
plt.ylabel('y = f(x)')
# tracé d'une grille
plt.grid()
# tracé de la courbe
plt.plot(x,y,'r')
plt.show()