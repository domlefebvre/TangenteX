# -*- coding: Latin-1 -*-
# Programme de resolution d'une EDO de second ordre sans second membre
# Dominique Lefebvre pour TangenteX.com
# 13 aout 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from scipy import array, arange, sin, log
from pylab import *                # fonction de tracé de courbe

# paramètres physiques de l'expérience
w0 = 1

# définition de la loi de rappel du ressort
def Rappel(x):
    k = 4.0    
    y = -x*sin(x/k)  
    return y
    
# Définition de l'EDO de deuxième ordre
def EDO(X,t):
    x = X[0]
    v = X[1]
    dx = v
    dv = Rappel(x)
    return array([dx, dv])

# saisie des conditions initiales de l'expérience
x0 = 1.0
v0 = 0.0

# rangement des conditions dans un tableau 2*1
C0 = array([x0, v0])                 

# définition du vecteur temps de l'expérience
t0 = 0.
tmax = 50.
pastemps = 0.01
time = arange(t0, tmax, pastemps)

X = array([1.0,1.0],float)

# intégration du système
X = odeint(EDO,C0,time)

# affichage de la courbe des résultats
figure()

title("Oscillateur non Hook")
xlabel('Temps')
ylabel('Position')

plot(time, X[:,0])

show()


