# -*- coding: Latin-1 -*-
# programme BODerivationSinus
# Dominique Lefebvre pour www.tangenteX.com
# le 5 aout 2015

#Appel des librairies
from scipy import sin, pi, arange
from scipy.misc import derivative
from matplotlib.pyplot import *

# D�finition de la fonction � d�river
def f(x):
    return sin(x)

# domaine de d�rivation
x = arange(0,2*pi,0.01)

# construction du vecteur y pour le trac� de la fonction
y = f(x)

# construction du vecteur yp pour le trac� de la d�riv�e
yprime = derivative(f,x,n=1,dx=0.01)

# trac� de la courbe et de sa d�riv�e
figure()
grid(True)
xlim(0,2*pi)
plot(x,y,'b',label= "fonction")
plot(x,yprime,'r', label = "derivee")
legend()
show()




