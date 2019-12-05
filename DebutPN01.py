# -*- coding: Latin-1 -*-
# DebutPN01 : programme de d�monstration du trac� d'une courbe y =f(x)
# Dominique Lefebvre pour TangenteX.com
# 26 mai 2017
#

# importation des librairies
import numpy as np
import matplotlib.pyplot as plt

# d�finition de la fonction sinus cardinal
def f(x): 
    try:
        sinc = np.sin(x) / x
    # prolongement par continuit� pour x = 0    
    except ZeroDivisionError:
        sinc = 1.0
    return sinc
    
# domaine de d�finition du trac� graphique
xmin = -6*np.pi
xmax = 6*np.pi
nbpoint = 600
x = np.linspace(xmin, xmax,nbpoint)

# calcul de f(x)
y = f(x)

# trac� de y = f(x)

# d�finition des limites d'affichage du graphe
plt.xlim(xmin, xmax)
plt.ylim(min(y),max(y))
#titre de la figure
plt.title('Fonction sinus cardinal')
# libell�s des axes
plt.xlabel('x')
plt.ylabel('y = f(x)')
# trac� d'une grille
plt.grid()
# trac� de la courbe
plt.plot(x,y,'r')
plt.show()