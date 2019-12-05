# Programme de resolution d'une EDO de premier ordre
# Dominique Lefebvre pour TangenteX.com
# 5 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de tracé de courbe

# paramètres physiques de l'expérience
Lambda = 0.0125 # constante de désintégration du radon 220 en s-1

# la fonction EDO retourne la valeur de dx/dt. Dans le cas
# de notre exemple dx/dt = -lambda*x
# la variable t n'intervient pas directement dans le calcul
# mais est indispensable à la fonction odeint.
def EDO(x,t):
    x_point = -Lambda*x
    return x_point

# saisie des conditions initiales de l'expérience
N0 = input("Valeur de la condition initiale: ")

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
N = odeint(EDO,N0,time)

# affichage de la courbe des résultats
figure()

title("Decroissance radioactive Radon 220")
xlabel('Temps')
ylabel('Population')

plot(time, N)

show()


