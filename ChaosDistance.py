# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule amorti forc�
# Trac� de la distance entre deux trajectoires chaotiques
# Dominique Lefebvre pour TangenteX.com
# 21 f�vrier 2017
#

# importation des librairies
from scipy import array, sin, arange, pi, hypot
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# d�finition du syst�me diff�rentiel pour le pendule amorti
def PenduleChaos(theta,t):
    return array([theta[1], -Omega02*sin(theta[0])-K*theta[1]+ \
                 A*sin(Omega*t)])

# param�tres de la simulation
# pendule simple
Omega02 = 1.0     # pulsation du pendule
K = 0.5           # coefficient d'amortissement
# pendule amorti forc�
Omega = 0.7       # pulsation de for�age
A = 1.22          # amplitude chaotique
Tf = 2*pi/Omega   # periode de for�age

# d�finition du vecteur temps de l'exp�rience
t0 = 0.0
tmax = 40*Tf
pastemps = 0.01*Tf
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
theta0 = pi/6.0   # angle initial en radian
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s


# calcul de la premi�re trajectoire
C0 = array([theta0,vtheta0])
theta1 = odeint(PenduleChaos,C0,time)

# calcul de la seconde trajectoire
epsilon = 1.e-8
C0 = array([theta0+epsilon,vtheta0])
theta2 = odeint(PenduleChaos,C0,time)

# calcul de la distance entre les deux trajectoires en fonction du temps
distance = hypot(theta2[:,0] - theta1[:,0],theta2[:,1] - theta1[:,1])

# trac� de la courbe distance
fig1 = plt.figure(1)
plt.grid(True)
plt.semilogy(time, distance)
plt.xlim(t0,tmax)
plt.title('Distance entre deux trajectoires chaotiques')
plt.xlabel('temps')
plt.ylabel('distance')
plt.tight_layout()
plt.show()

