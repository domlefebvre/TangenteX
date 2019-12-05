# Programme de resolution d'une EDO de premier ordre avec second membre
# Dominique Lefebvre pour TangenteX.com
# 6 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de tracé de courbe

# paramètres physiques de l'expérience
Vc = 5.0

# la fonction EDO retourne la valeur de dx/dt. Dans le cas
# de notre exemple dx/dt = 1/RC(-x + Vc) avec RC = 1
# la variable t n'intervient pas directement dans le calcul
# mais est indispensable à la fonction odeint.
def EDO(x,t):
    x_point = -x + Vc
    return x_point

# saisie des conditions initiales de l'expérience
V0 = input("Valeur de la condition initiale: ")

# définition du vecteur temps de l'expérience, entre 0 et 400 secondes
t0 = input("temps initial de l'experience (en secondes) : ")
tmax = input("durée de l'experience (en secondes) : ")
pastemps = input("increment de temps (en secondes) : ")
tmax = tmax + t0
time = arange(t0, tmax, pastemps)

# intégration du système
# N est un vecteur de même dimension que le vecteur time, qui contient
# les valeurs calculées du nombre de noyaux restant pour chaque valeur
# de temps
V = odeint(EDO,V0,time)

# affichage de la courbe des résultats
figure()

title("Charge d'un condensateur")
xlabel('Temps')
ylabel('Tension')

plot(time, V)

show()


