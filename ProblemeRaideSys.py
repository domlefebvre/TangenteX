# -*- coding: Latin-1 -*-
# Programme de resolution d'un système d'EDO de premier ordre
# Cas d'un problème raide - différentes méthodes d'intégration
# Dominique Lefebvre pour TangenteX.com
# 10 septembre 2017
#

# importation des librairies
from scipy import exp, array, arange, asarray
from scipy.integrate import odeint
from scipy.linalg import eig
import matplotlib.pyplot as plt

# Définition du système d'EDO
def EDO(dxdy,t):
    x,y = dxdy    
    dx = a*x + b*y
    dy = c*x + d*y
    return (dx,dy)

# Fonction de calcul de la solution analytique
def SolAna(dom,vp1,vp2): 
    xi = [];yi = []
    for t in dom:
        xi.append(exp(vp1*t)  + exp(vp2*t))
        yi.append(-exp(vp1*t) + exp(vp2*t))
    return (xi,yi)

# méthode Euler
def Euler(fonction, C0, dom, h):
    xi = [];yi = []    
    r = array(C0,float)
    for t in dom:
        xi.append(r[0])
        yi.append(r[1])
        r += h*asarray(fonction(r,t))
    return (xi,yi)

# définition de la fonction RK4
def RK4(fonction, C0, dom, h):
    xi = [];yi = []    
    r = array(C0,float)
    for t in dom:
        xi.append(r[0])
        yi.append(r[1])    
        k1 = h*asarray(fonction(r,t))
        k2 = h*asarray(fonction(r + k1/2.0, t + h/2.0))
        k3 = h*asarray(fonction(r + k2/2.0, t + h/2.0))
        k4 = h*asarray(fonction(r + k3, t + h))
        r += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return (xi,yi)
    
# définition des paramètres du système
a = -20.0
b = -19.0
c = -19.0
d = -20.0

# rangement des conditions dans un tableau
x0 = 2.0
y0 = 0.0
C0 = array([x0,y0])
                 
# définition du domaine d'intégration
xinf = 0.0
xsup = 1.0
dx = 0.01
nbpas = int((xsup - xinf)/dx)
domaine = arange(xinf,xsup,dx)

# calcul des valeurs propres du système
J = [[a,b],[c,d]]  # matrice jacobienne du système  
vp,vcp = eig(J)        
lambda1, lambda2 = vp
v1,v2 = vcp
print 'les valeurs propres du systeme sont ',lambda1, ' et ',lambda2
print 'les vecteurs propres sont ',v1, ' et ', v2


# calcul de la solution analytique
X,Y = SolAna(domaine,lambda1.real,lambda2.real)

# intégration par la méthode d'Euler
xEu,yEu = Euler(EDO,C0,domaine,dx)

# intégration par la méthode RK4
xRK4,yRK4 = RK4(EDO,C0,domaine,dx)

# intégration par odeint()
S, infodict = odeint(EDO,C0,domaine,printmessg=True,full_output=True)
print infodict


# affichage des solutions
plt.figure()

plt.subplot(2,1,1)
plt.grid(True)
plt.title("Systeme EDO raide")
plt.xlabel('t')
plt.ylabel('x(t)')

plt.plot(domaine,X,'black',label = "analytique")
plt.plot(domaine,S[:,0],'r',label = "odeint()")
plt.plot(domaine,xEu,'g',label = "Euler")
plt.plot(domaine,xRK4,'b',label = "RK4")
plt.legend()

plt.subplot(2,1,2)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.plot(domaine,Y,'black')
plt.plot(domaine,S[:,1],'r')
plt.plot(domaine,yEu,'g')
plt.plot(domaine,yRK4,'b')

plt.tight_layout()
plt.show()
