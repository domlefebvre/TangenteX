# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule simple
# Dominique Lefebvre pour TangenteX.com
# 6 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# paramètres physiques
g = 9.81       # accélération de la pesanteur en m.s-2

# définition du système différentiel pour le pendule non amorti
def Pendule(theta,t):
    return array([theta[1], -Omega2*sin(theta[0])])


# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 2*pi
pastemps = 0.01
time = arange(t0, tmax, pastemps)

# lancement des simulations
plt.figure(1)

# simulation 1

# paramètres de la simulation
l = 1.         # longueur en m
Omega2 = g/l   # pulsation du pendule
# conditions initiales de la simulation
theta0 = 0.5   # angle initial en radian
vtheta0 = 0.0  # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])
# intégration
theta = odeint(Pendule,C0,time)
# affichage du résultat
plt.subplot(221)
plt.grid(True)
plt.plot(time, theta[:,0])
plt.xlim(t0,tmax)
plt.xlabel('temps')
plt.ylabel('angle')

# tracé du portrait de phase
plt.subplot(224)
plt.grid(True)
plt.plot(theta[:,0],theta[:,1])
plt.xlabel('angle')
plt.ylabel('vitesse angulaire')

# simulation 2 (variation de l et donc de la période)

# paramètres de la simulation
l = 4.         # longueur en m
Omega2 = g/l   # pulsation du pendule
# conditions initiales de la simulation
theta0 = 0.5   # angle initial en radian
vtheta0 = 0.0  # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])
# intégration
theta = odeint(Pendule,C0,time)
# affichage du résultat
plt.subplot(222)
plt.grid(True)
plt.plot(time, theta[:,0])
plt.xlim(t0,tmax)
plt.xlabel('temps')
plt.ylabel('angle')


# simulation 3 (variation de theta0 avec l=1.0)

# paramètres de la simulation
l = 1.         # longueur en m
Omega2 = g/l   # pulsation du pendule
# conditions initiales de la simulation
theta0 = 3.0   # angle initial en radian
vtheta0 = 0.0  # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])
# intégration
theta = odeint(Pendule,C0,time)
# affichage du résultat
plt.subplot(223)
plt.grid(True)
plt.plot(time, theta[:,0])
plt.xlim(t0,tmax)
plt.xlabel('temps')
plt.ylabel('angle')





