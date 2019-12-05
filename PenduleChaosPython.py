# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule amorti forcé
# découverte du chaos
# Dominique Lefebvre pour TangenteX.com
# 12 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi, sqrt
from scipy.integrate import odeint
from scipy.fftpack import fft, fftfreq
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
A = 1.20       # amplitude du forçage
Omega = 0.7       # pulsation de forçage
Tf = 2*pi/Omega   # periode de forçage

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 20*Tf
pastemps = 0.01*Tf
time = arange(t0, tmax, pastemps)


# conditions initiales de la simulation
theta0 = pi/6.0   # angle initial en radian
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])

# intégration
theta = odeint(PenduleChaos,C0,time)

#trajectoire
fig1 = plt.figure(1)
plt.grid(True)
plt.plot(time, theta[:,0])
plt.xlim(t0,tmax)
titre = 'Amplitude forcage : ' + str(A)
plt.title(titre)
plt.xlabel('temps')
plt.ylabel('angle')
plt.show()

# trajectoire de phase
fig2 = plt.figure(2)
plt.grid(True)
plt.plot(theta[:,0],theta[:,1]/sqrt(Omega02) )
plt.title(titre)
plt.xlabel('angle')
plt.ylabel('vitesse angulaire')
plt.text(0.55,0,'C0')
plt.show()

# calcul du spectre du signal en régime établi
filtre = time > 40  # sélection du signal en régime établi
theta = theta[filtre,0]
theta -= theta.mean()           # élimination du signal moyen
N =theta.size

Te = 0.1
freq = fftfreq(N, Te)
freq = freq[range(N/2)]

s = abs(fft(theta)/N)
s = s[range(N/2)]
fig3 = plt.figure(3)
plt.grid(True)
plt.plot(freq,s)
titre = 'Spectre pour amplitude forcage = ' + str(A)
plt.title(titre)
plt.xlabel('frequence')
plt.ylabel('amplitude')
plt.show()


