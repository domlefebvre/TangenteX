# -*- coding: Latin-1 -*-
# programme BODeriveeOpt
# Dominique Lefebvre pour www.tangenteX.com
# le 5 aout 2015

#Appel des librairies
from scipy import pi, arange
from scipy.misc import derivative
from matplotlib.pyplot import *


# Définition de la fonction à dériver
def f(r):
    return ((2.0/r) + 2*pi*r**2)


# domaine de dérivation
rmax = 2.0
r = arange(0.1,rmax,0.01)
S = f(r)

# recherche de la dérivée de la fonction S
Sprime = derivative(f,r,n=1,dx=0.01)

# recherche du zéro de la dérivée
i=0
while (Sprime[i] < 0):
    i = i +1
print 'rayon optimum :',r[i-1]

# tracé de la courbe et de sa dérivée
figure()
grid(True)
xlim(0,rmax)
ylim(-25,25)
plot(r,S,'b', label="Surface")
plot(r,Sprime,'r', label = "Sprime")
legend()
show()




