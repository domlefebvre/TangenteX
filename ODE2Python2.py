# Programme de resolution d'une EDO de second ordre non linéaire
# Dominique Lefebvre pour TangenteX.com
# 13 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from scipy import array, arange
from pylab import *                # fonction de tracé de courbe


# La variable t n'intervient pas directement dans le calcul
# mais est indispensable à la fonction odeint.
def EDO(Theta,t):
    theta = Theta[0]
    theta_point = Theta[1]
    dtheta = theta_point
    dtheta_point = -sin(theta)
    return array([dtheta, dtheta_point])

# saisie des conditions initiales de l'expérience
theta0 = input("angle initial (en rd) : ")
theta_point0 = input("vitesse angulaire initiale (en rd.s-1) : ")

# rangement des conditions dans un tableau 2*1
C0 = array([theta0, theta_point0])                 

# définition du vecteur temps de l'expérience
t0 = input("temps initial de l'experience (en secondes) : ")
tmax = input("durée de l'experience (en s) : ")
pastemps = input("increment de temps (en s) : ")
tmax = tmax + t0
time = arange(t0, tmax, pastemps)

THETA = array([1.0,1.0])

# intégration du système
THETA = odeint(EDO,C0,time)

# affichage de la courbe des résultats
figure()

title("Oscillation d'un pendule")
xlabel('Temps')
ylabel('Angle')

plot(time, THETA[:,0])

show()


