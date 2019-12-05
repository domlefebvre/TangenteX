# -*- coding: Latin-1 -*-
# programme de tracé du portrait de phase d'un pendule
# Dominique Lefebvre pour TangenteX.com
# 17 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# définition du système différentiel pour le pendule amorti
def PenduleChaos(theta,t):
    return array([theta[1], -Omega02*sin(theta[0])-K*theta[1]+ \
                 A*sin(Omega*t)])


# paramètres de la simulation
# pendule simple
Omega02 = 1.0  # pulsation du pendule

# pendule amorti
K = 0.5        # coefficient d'amortissement

# pendul amorti forcé
A = 0.0        # amplitude du forçage
Omega = 0.7    # pulsation de forçage

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 5*pi
pastemps = 0.01
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
pastheta0 = pi/10.0
ThetaInit = arange(0, pi, pastheta0)
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s

# tracé du portrait de phase
plt.figure(figsize=(8, 8))
for theta0 in ThetaInit:
    theta,vtheta = odeint(PenduleChaos,(theta0,vtheta0),time).T
    plt.plot(theta,vtheta)

plt.grid(True)
plt.title('Portait de phase')
plt.xlabel('angle')
plt.ylabel('vitesse angulaire')
plt.axis('equal')
plt.tight_layout()
plt.show()
