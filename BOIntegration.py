# -*- coding: Latin-1 -*-
# programme BOintegration

from scipy import cos, pi, arange, sqrt
from scipy.integrate import quad
from matplotlib.pyplot import *

k = 1   # k = l/g - pour simplifier, je le pose = 1

# Définition de la période en fonction de theta et theta0
def f(theta,theta0):
    x = 1.0/sqrt(cos(theta) - cos(theta0))
    return x

# boucle de variation de theta0 entre 0.01 et PI/2 radians par pas de 0.01 rd
domaine = arange(0.01, pi/2.0, 0.01)

# Définition de la période avec l'approx. des petits angles
T0 = [2*pi*sqrt(k)]*len(domaine)

T = [0.0]*len(domaine)
i=0
for angle in domaine:
    T[i] = (4.0/sqrt(2))*quad(f,0,angle,args=(angle))[0]
    i = i+1
    
# Tracé de la courbe de variation de T en fonction de l'angle initial
# theta0, comparée à la droite T0, période calculée avec l'approximation
# des petits angles    
figure()
grid(True)
title('Variation de la periode en fonction de theta0')
xlabel('theta0')
ylabel('Periode')

xlim(0.01,pi/2.0)

plot(domaine,T, label="T")
plot(domaine,T0,'r', label = "T0")
legend()
show()




