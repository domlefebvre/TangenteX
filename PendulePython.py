# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule simple
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from scipy import array, sin, arange, pi
from scipy.integrate import odeint
from pylab import figure,plot,xlabel,ylabel,show

# paramètres physiques de l'expérience
l = 1.         # longueur en m
g = 9.81       # accélération de la pesanteur en m.s-2
m = 1.         # masse en kilogramme
Omega2 = g/l  # pulsation du pendule


#définition du système différentiel
def Pendule(theta,t):
    return array([theta[1], -Omega2*sin(theta[0])])

# saisie des conditions initiales de l'expérience
theta0 = input("Angle initial (en rd): ");
vtheta0 = input("Vitesse angulaire initiale (en rd/s): ");
C0 = array([theta0,vtheta0])  # angle initial et vitesse angulaire initiales

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 5*pi
pastemps = 0.01
time = arange(t0, tmax, pastemps)

# intégration du système
theta = odeint(Pendule,C0,time)

# affichage de la trajectoire du pendule simple
figure()
plot(time, theta[:,0])
xlabel('temps')
ylabel('angle')
show()
