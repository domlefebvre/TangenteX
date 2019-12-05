# programme de simulation d'un pendule simple amorti
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de tracé de courbe

# paramètres physiques de l'expérience
l = 1        # longueur en m
g = 9.81       # accélération de la pesanteur en m.s-2
Omega2 = g/l   # pulsation du pendule


#définition du système différentiel
def Pendule(theta,t):
    return array([theta[1], -Omega2*theta[0] - K*theta[1]])

# saisie des conditions initiales de l'expérience
theta0 = input("Angle initial (en rd): ")
vtheta0 = input("Vitesse angulaire initiale (en rd/s): ")
K = input("Taux d'amortissement (en s-1): ")
C0 = array([theta0,vtheta0])  # angle initial et vitesse angulaire initiales

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10*pi
nbpoints = 5000
time = linspace(t0, tmax, nbpoints)

# intégration du système
theta = odeint(Pendule,C0,time)

# affichage des résultats
figure(1)
# trajectoire du système
subplot(211)
plot(time, theta[:,0])
xlabel('temps')
ylabel('angle')
# portrait de phase
subplot(212)
plot(theta[:,0],theta[:,1])
ylabel('vitesse angulaire')
xlabel('amplitude')

show()
