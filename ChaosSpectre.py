# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule amorti forcé
# Tracé du spectre
# Dominique Lefebvre pour TangenteX.com
# 21 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi, sqrt,log
from scipy.integrate import odeint
from scipy.fftpack import fft
from scipy.signal import blackman
import matplotlib.pyplot as plt



# définition du système différentiel pour le pendule amorti
def PenduleChaos(theta,t):
    return array([theta[1], -Omega02*sin(theta[0])-K*theta[1]+ \
                 amplitude*sin(Omega*t)])


# paramètres de la simulation
# pendule simple
Omega02 = 1.0     # pulsation du pendule
K = 0.5           # coefficient d'amortissement
# pendule amorti forcé
Omega = 0.7       # pulsation de forçage
Tf = 2*pi/Omega   # periode de forçage

# définition du vecteur de variation de l'amplitude de forçage
A = arange(0.9,1.25,0.001)

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 20*Tf
pastemps = 0.01*Tf
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
theta0 = pi/6.0   # angle initial en radian
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])

# définition de la fenêtre de Blackman
filtre = time > 40  # sélection du signal en régime établi
hann = blackman(filtre.sum())

# boucle de calcul du spectre en fonction de l'amplitude
spectre = []
plt.figure(1)
for amp in A:
    amplitude = amp  
    theta = odeint(PenduleChaos,C0,time)
    theta = theta[filtre,0]
    theta -= theta.mean()
    theta /= sqrt((theta**2).mean())
    theta *= hann
    spectre.append(fft(theta))
    
# affichage    
spectre = array(spectre)
plt.imshow(log(abs(spectre[:,:200]).T), aspect='auto',interpolation='nearest',\
           origin='lower',extent=[0.9,1.25,0,200])
plt.title('Spectre en fonction du forcage')
plt.xlabel('forcage')
plt.ylabel('frequence')



