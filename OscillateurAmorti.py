# -*- coding: Latin-1 -*-
# programme d'�tude d'un oscillateur harmonique amorti
# d2x/dt2 + (omega0/Q)dx/dt + omega0**2 x = 0
# Dominique Lefebvre pour TangenteX.com
# 28 avril 2017
#

# importation des librairies
from scipy import array, arange
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# param�tres physiques de l'oscillateur
Omega0 = 1.0
Q = 0.5
tau = Q/Omega0    # temps caract�ristique du syst�me

# param�tres calcul�s
Omega2 = Omega0**2
K = Omega0/Q
   

# analyse du r�gime de l'oscillateur
delta = K**2 - 4*Omega2

# d�finition du syst�me diff�rentiel pour l'oscillateur amorti
def OscillateurAmorti(x,t):
    return array([x[1], -K*x[1] - Omega2*x[0]])

# d�finition du vecteur temps de l'exp�rience
t0 = 0.0
tmax = 10*tau
pastemps = 0.01
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
x0 = 0.5     # position initiale
v0 = 0.0     # vitesse initiale
C0 = array([x0,v0])

# int�gration
x = odeint(OscillateurAmorti,C0,time)

# affichage
# trajectoire
plt.figure(1)
plt.grid(True)
plt.plot(time, x[:,0])
plt.xlim(t0,tmax)
plt.xlabel('temps')
plt.ylabel('position')
# diagramme de phase
plt.figure(2)
plt.grid(True)
plt.plot(x[:,0],x[:,1] )
plt.xlabel('angle')
plt.ylabel('vitesse')




