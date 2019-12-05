# Programme de resolution d'une EDO de premier ordre avec second membre
# Dominique Lefebvre pour TangenteX.com
# 6 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de trac� de courbe

# param�tres physiques de l'exp�rience
Vc = 5.0

# la fonction EDO retourne la valeur de dx/dt. Dans le cas
# de notre exemple dx/dt = 1/RC(-x + Vc) avec RC = 1
# la variable t n'intervient pas directement dans le calcul
# mais est indispensable � la fonction odeint.
def EDO(x,t):
    x_point = -x + Vc
    return x_point

# saisie des conditions initiales de l'exp�rience
V0 = input("Valeur de la condition initiale: ")

# d�finition du vecteur temps de l'exp�rience, entre 0 et 400 secondes
t0 = input("temps initial de l'experience (en secondes) : ")
tmax = input("dur�e de l'experience (en secondes) : ")
pastemps = input("increment de temps (en secondes) : ")
tmax = tmax + t0
time = arange(t0, tmax, pastemps)

# int�gration du syst�me
# N est un vecteur de m�me dimension que le vecteur time, qui contient
# les valeurs calcul�es du nombre de noyaux restant pour chaque valeur
# de temps
V = odeint(EDO,V0,time)

# affichage de la courbe des r�sultats
figure()

title("Charge d'un condensateur")
xlabel('Temps')
ylabel('Tension')

plot(time, V)

show()


