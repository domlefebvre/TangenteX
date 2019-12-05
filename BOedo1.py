# Programme de resolution d'une EDO de premier ordre
# Dominique Lefebvre pour TangenteX.com
# 12 aout 2015
#

# importation des librairies
from scipy import cos, arange,pi
from scipy.integrate import odeint 
from matplotlib.pyplot import *              

# la fonction f retourne la valeur de dx/dt.
def fprime(x,t):
    x_point = cos(x**2 + t)
    return x_point

# définition du vecteur temps
t0 = 0.
tmax = 10*pi
pastemps = 0.1
time = arange(t0, tmax, pastemps)

# condition initiale
x0 = 0

# intégration du système
N = odeint(fprime,x0,time)

# affichage de la courbe des résultats
figure()
grid(True)
xlim(t0, tmax)
ylim(N.min(), N.max())
xlabel('t')
ylabel('y')

plot(time, N)

show()


