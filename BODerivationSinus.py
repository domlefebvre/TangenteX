# -*- coding: Latin-1 -*-
# programme BODerivationSinus
# Dominique Lefebvre pour www.tangenteX.com
# le 5 aout 2015

#Appel des librairies
from scipy import sin, pi, arange
from scipy.misc import derivative
from matplotlib.pyplot import *

# Définition de la fonction à dériver
def f(x):
    return sin(x)

# domaine de dérivation
x = arange(0,2*pi,0.01)

# construction du vecteur y pour le tracé de la fonction
y = f(x)

# construction du vecteur yp pour le tracé de la dérivée
yprime = derivative(f,x,n=1,dx=0.01)

# tracé de la courbe et de sa dérivée
figure()
grid(True)
xlim(0,2*pi)
plot(x,y,'b',label= "fonction")
plot(x,yprime,'r', label = "derivee")
legend()
show()




