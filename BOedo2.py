# -*- coding: Latin-1 -*-
# Programme de resolution d'un système d'EDO de premier ordre
# Dominique Lefebvre pour TangenteX.com
# 13 aout 2015
#

# importation des librairies
from scipy import arange, array
from scipy.integrate import odeint
from matplotlib.pyplot import *

# Définition du système d'EDO
def EDO(sysEDO,t):
    x = sysEDO[0]
    y = sysEDO[1]
    dx = -y + x*(1 - x**2 - y**2)
    dy =  x + y*(1 - x**2 - y**2)
    return [dx, dy]


# rangement des conditions dans un tableau
x0 = 0.01
y0 = 0.01
C0 = array([x0, y0])                 

# définition du vecteur temps de l'expérience
t0 = 0
tmax = 50
pastemps = 0.1
time = arange(t0, tmax, pastemps)

# intégration du système
S = odeint(EDO,C0,time)

# affichage de la courbe des résultats
figure()

grid(True)
xlim(S[:,0].min(), S[:,0].max())
ylim(S[:,1].min(), S[:,1].max())

title("Systeme d'EDO")
xlabel('x')
ylabel('y')

plot(S[:,0], S[:,1])

show()


