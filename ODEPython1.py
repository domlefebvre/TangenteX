# Programme de resolution d'une EDO de premier ordre
# Dominique Lefebvre pour TangenteX.com
# 5 mai 2015
#

# importation des librairies
from scipy.integrate import odeint # on importe uniquement ce dont on a besoin
from pylab import *                # fonction de trac� de courbe

# param�tres physiques de l'exp�rience
Lambda = 0.0125 # constante de d�sint�gration du radon 220 en s-1

# la fonction EDO retourne la valeur de dx/dt. Dans le cas
# de notre exemple dx/dt = -lambda*x
# la variable t n'intervient pas directement dans le calcul
# mais est indispensable � la fonction odeint.
def EDO(x,t):
    x_point = -Lambda*x
    return x_point

# saisie des conditions initiales de l'exp�rience
N0 = input("Valeur de la condition initiale: ")

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
N = odeint(EDO,N0,time)

# affichage de la courbe des r�sultats
figure()

title("Decroissance radioactive Radon 220")
xlabel('Temps')
ylabel('Population')

plot(time, N)

show()


