# -*- coding: Latin-1 -*-
# programme de simulation d'un pendule amorti forc�
# Trac� du spectre
# Dominique Lefebvre pour TangenteX.com
# 21 f�vrier 2017
#

# importation des librairies
from scipy import array, sin, arange, pi, sqrt,log
from scipy.integrate import odeint
from scipy.fftpack import fft
from scipy.signal import blackman
import matplotlib.pyplot as plt



# d�finition du syst�me diff�rentiel pour le pendule amorti
def PenduleChaos(theta,t):
    return array([theta[1], -Omega02*sin(theta[0])-K*theta[1]+ \
                 amplitude*sin(Omega*t)])


# param�tres de la simulation
# pendule simple
Omega02 = 1.0     # pulsation du pendule
K = 0.5           # coefficient d'amortissement
# pendule amorti forc�
Omega = 0.7       # pulsation de for�age
Tf = 2*pi/Omega   # periode de for�age

# d�finition du vecteur de variation de l'amplitude de for�age
A = arange(0.9,1.25,0.001)

# d�finition du vecteur temps de l'exp�rience
t0 = 0.0
tmax = 20*Tf
pastemps = 0.01*Tf
time = arange(t0, tmax, pastemps)

# conditions initiales de la simulation
theta0 = pi/6.0   # angle initial en radian
vtheta0 = 0.0     # vitesse angulaire initiale en rd/s
C0 = array([theta0,vtheta0])

# d�finition de la fen�tre de Blackman
filtre = time > 40  # s�lection du signal en r�gime �tabli
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



