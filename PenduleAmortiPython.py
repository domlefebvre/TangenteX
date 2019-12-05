# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule simple
# Dominique Lefebvre pour TangenteX.com
# 6 f�vrier 2017
#

# importation des librairies
from scipy import array, sin, arange, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# param�tres physiques
g = 9.81       # acc�l�ration de la pesanteur en m.s-2

# d�finition du syst�me diff�rentiel pour le pendule amorti
def PenduleAmorti(theta,t):
    return array([theta[1], -Omega2*sin(theta[0])-K*theta[1]])

# d�finition du vecteur temps de l'exp�rience
t0 = 0.0
tmax = 5*pi
pastemps = 0.01
time = arange(t0, tmax, pastemps)

# lancement des simulations
plt.figure(1)

# simulation 1

# param�tres de la simulation
l = 1.         # longueur en m
Omega2 = g/l   # pulsation du pendule
K = 0.5        # coefficient d'amortissement
# conditions initiales de la simulation
theta0 = 0.5   # angle initial en radian
vtheta0 = 0.0  # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])
# int�gration
theta = odeint(PenduleAmorti,C0,time)

# affichage du r�sultat
plt.subplot(221)
plt.grid(True)
plt.plot(time, theta[:,0])
plt.xlim(t0,tmax)
plt.xlabel('temps')
plt.ylabel('angle')

plt.subplot(222)
plt.grid(True)
plt.plot(theta[:,0],theta[:,1] )
plt.xlabel('angle')
plt.ylabel('vitesse angulaire')




