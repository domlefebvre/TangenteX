# Programme de resolution d'une EDO de second ordre sans second membre
# Dominique Lefebvre pour TangenteX.com
# 12 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from scipy import array, arange
from pylab import *                # fonction de tracé de courbe

# paramètres physiques de l'expérience
g = 9.81   # accélération de la pesanteur en m.s-2


# La variable t n'intervient pas directement dans le calcul
# mais est indispensable à la fonction odeint.
def EDO(Z,t):
    z = Z[0]
    v = Z[1]
    dz = v
    dv = -g
    return array([dz, dv])

# saisie des conditions initiales de l'expérience
z0 = input("altitude initiale (en m) : ")
v0 = input("vitesse initiale (en m.s-1) : ")

# rangement des conditions dans un tableau 2*1
C0 = array([z0, v0])                 

# définition du vecteur temps de l'expérience
t0 = input("temps initial de l'experience (en secondes) : ")
tmax = input("durée de l'experience (en s) : ")
pastemps = input("increment de temps (en s) : ")
tmax = tmax + t0
time = arange(t0, tmax, pastemps)

Z = array([1.0,1.0],float)

# intégration du système
Z = odeint(EDO,C0,time)

# affichage de la courbe des résultats
figure()

title("Chute d'un corps")
xlabel('Temps')
ylabel('Altitude')

plot(time, Z[:,0])

show()


