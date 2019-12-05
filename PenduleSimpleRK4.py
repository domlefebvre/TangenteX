# -*- coding: Latin-1 -*-
# Programme de resolution d'un système d'EDO de premier ordre
# Cas du pendule simple - résolution par RK4
# Dominique Lefebvre pour TangenteX.com
# 31 juillet 2017
#

# importation des librairies
from scipy import array, arange, pi, sin
import matplotlib.pyplot as plt

# Définition du système Pendule simple
def Pendule(dxdy,t):
    x,y = dxdy    
    return array([y,-omega0**2*sin(x)])

# définition de la fonction RK4
def RK4Sys2(fonction, dom, xini, yini, h):
    """
    27 juillet 2017
    @author: dominique lefebvre - tangentex.com
    
    cette fonction intégre le système d'EDO d'ordre 2 avec les paramètres
    suivants:
    - fonction : désigne la fonction de définition du système
    - dom : désigne le domaine d'intégration du système
    - xini, yini : conditions initiales du système
    - h : pas d'intégration sur le domaine
    
    La fonction retourne deux listes contenant les (xi,yi) de la
    courbe intégrale
    """
    xi = [];yi = []    
    r = array([xini,yini])
    for t in dom:
        xi.append(r[0])
        yi.append(r[1])    
        k1 = h*fonction(r,t)
        k2 = h*fonction(r + k1/2.0, t + h/2.0)
        k3 = h*fonction(r + k2/2.0, t + h/2.0)
        k4 = h*fonction(r + k3, t + h)
        r += (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return (xi,yi)
    
# paramètres du système
omega0 = 1.0      # pulsation propre du pendule

# rangement des conditions dans un tableau
theta0 = pi/6.0   # angle initial
dtheta0 = 0.00    # vitesse angulaire initiale
                 
# définition du domaine d'intégration
xinf = 0.0
xsup = 4.0*pi
dt = 0.01
nbpas = int((xsup - xinf)/dt)
domaine = arange(xinf,xsup,dt)

# intégration du système par RK4
theta,dtheta = RK4Sys2(Pendule,domaine,theta0,dtheta0,dt)

# affichage de la courbe des résultats
plt.figure()
plt.grid(True)
plt.xlim(xinf,xsup)
plt.title("Pendule simple - RK4")
plt.xlabel('temps')
plt.ylabel('angle')
plt.plot(domaine,theta,'b')
plt.show()


