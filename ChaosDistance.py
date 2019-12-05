# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule amorti forcé
# Tracé de la distance entre deux trajectoires chaotiques
# Dominique Lefebvre pour TangenteX.com
# 21 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi, hypot
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# définition du système différentiel pour le pendule amorti
def PenduleChaos(theta,t):
    return array([theta[1], -Omega02*sin(theta[0])-K*theta[1]+ \
                 A*sin(Omega*t)])

# paramètres de la simulation
# pendule simple
Omega02 = 1.0     # pulsation du pendule
K = 0.5           # coefficient d'amortissement
# pendule amorti forcé
Omega = 0.7       # pulsation de forçage
A = 1.22          # amplitude chaotique
Tf = 2*pi/Omega   # periode de forçage

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 40*Tf
pastemps = 0.01*Tf
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
theta0 = pi/6.0   # angle initial en radian
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s


# calcul de la première trajectoire
C0 = array([theta0,vtheta0])
theta1 = odeint(PenduleChaos,C0,time)

# calcul de la seconde trajectoire
epsilon = 1.e-8
C0 = array([theta0+epsilon,vtheta0])
theta2 = odeint(PenduleChaos,C0,time)

# calcul de la distance entre les deux trajectoires en fonction du temps
distance = hypot(theta2[:,0] - theta1[:,0],theta2[:,1] - theta1[:,1])

# tracé de la courbe distance
fig1 = plt.figure(1)
plt.grid(True)
plt.semilogy(time, distance)
plt.xlim(t0,tmax)
plt.title('Distance entre deux trajectoires chaotiques')
plt.xlabel('temps')
plt.ylabel('distance')
plt.tight_layout()
plt.show()

