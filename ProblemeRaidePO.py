# -*- coding: Latin-1 -*-
# Programme de resolution d'une EDO
# Cas d'un problème raide de premier ordre
# Comparaison de plusieurs méthodes de résolution
# Dominique Lefebvre pour TangenteX.com
# 18 août 2017
#

# importation des librairies
from scipy import array, ones, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# définition de l'EDO
def EDO(y,t):
    return (-150.0*y + 30.0)

# méthode Euler
def Euler(fonction, dom, y0, h):
   Y = [];y = y0    
   for t in dom:
        Y.append(y)
        y += h*fonction(y,t)
   return Y

    
# méthode RK4
def RK4(fonction, dom, y0, h):
    Y = []; y = y0     
    for t in dom:
        Y.append(y)    
        k1 = h*fonction(y,t)
        k2 = h*fonction(y + k1/2.0, t + h/2.0)
        k3 = h*fonction(y + k2/2.0, t + h/2.0)
        k4 = h*fonction(y + k3, t + h)
        y += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return Y
         
# définition du domaine d'intégration
xinf = 0.0
xsup = 1.0
dx = 0.015
nbpas = int((xsup - xinf)/dx)
X = linspace(xinf,xsup,nbpas)

# vecteur des conditions initiales
epsilon = 0.0001
y0 = 1.0/5.0 + epsilon
C0 = array([xinf,y0])

# intégration du système par la méthode d'Euler
#ye = Euler(EDO,X,y0,dx)

# intégration du système par la méthode RK4
#yRK4 = RK4(EDO,X,y0,dx)

# integration par odeint()
S,infodict = odeint(EDO,y0,X, printmessg=True,full_output=True)
print infodict

# affichage de la courbe des résultats
plt.figure()

plt.grid(True)
plt.title("Solutions - pas = " + str(dx) )
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(xinf,xsup)
plt.ylim(-2.0,2.0)

plt.plot(X,0.2*ones(len(X)),'black', label = "solution analytique")
#plt.plot(X,ye,'g', label = "solution Euler")
#plt.plot(X,yRK4,'b', label = "solution RK4")   # dx = .0185 sur [0,10]
plt.plot(X,S,'r', label = "solution odeint()")

plt.legend()
plt.show()


