# programme de simulation d'un sismographe
# Dominique Lefebvre pour TangenteX.com
# 19 aout 2014
#

# importation des librairies
from numpy import linspace, sin, cos, arange, sqrt, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# définition des constantes du sismographe
m = 1.0        # masse en kg(5 kg)
k = 500.0      # raideur du ressort en N.m-1 (500)

#f0 = input("Frequence propre sismometre : ")
#k = m*(2*pi*f0)**2

# calcul de la pulsation propre du sismographe
Omega0Carre = k/m
Omega0 = sqrt(Omega0Carre)
Q = input("Facteur de qualite: ")

# calcul de l'amortissement
h = Omega0*m/Q


# paramètres de l'onde sismique
Z0 = 1.0
f = input("Frequence de l'onde sismique : ")
OmegaF = 2*pi*f
print 'Frequence propre: ',Omega0/(2*pi),'  Frequence onde : ',f, ' Q :',Q

# fonction de simulation de l'onde sismique
def onde(Z0, t, OmegaF):
    return (Z0*sin(OmegaF*t))
            
# modèle du sismographe
def modele_sismo(y,t,Q,Omega0,Z0,OmegaF):
    z,z_dot = y
    z_ddot = Z0*cos(OmegaF*t)*OmegaF**2 - (Omega0**2)*z - (Omega0/Q)*z_dot
    return[z_dot, z_ddot]

# définition du vecteur temps de l'expérience
t0 = 0
t1 = 5
nbpoints = 1000
t = linspace(t0, t1, nbpoints)

# calcul de l'onde sismique
ondesismique = onde(Z0,t,OmegaF)

# conditions initiales du sismographe
z0 =0.0
z_dot0 = 0.0

# excitation du sismographe
sol = odeint(modele_sismo, [z0, z_dot0], t, args=(Q,Omega0,Z0,OmegaF))

#affichage du signal de forçage
plt.title('Onde sismique et reponse du sismographe')
plt.plot(t,ondesismique,'b', label='onde sismique')
plt.plot(t,sol[:,0],'r', label='reponse sismographe')
plt.legend()
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')


plt.show()

