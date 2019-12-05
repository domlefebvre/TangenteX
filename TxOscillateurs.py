#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Routines de calcul et utilitaires pour étude oscillateurs """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "16 mai 2018" 
__email__       = "dominique.lefebvre@tangentex.com"


from scipy import array, sin, arange, sqrt
from scipy.integrate import odeint
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,subplot,title

#
# Routines d'initialisation
#
# définition du vecteur temps de l'expérience
def VecteurTemps(t0, tmax, pas):
    """ Définition du vecteur temps pour une expérience
        t0   : temps initial en s
        tmax : temps final en s
        pas  : pas de temps en s
    """
    time = arange(t0, tmax, pas)
    return time

# définition des conditions initiales pour un oscillateur harmonique
def CIHarmonique(theta0,vtheta0):
    """ Définition des conditions initiales pour un oscillateur harmonique
        theta0  : angle initial en rd
        vtheta0 : vitesse angulaire initiale en rd.s-1
    """
    C0 = array([theta0,vtheta0])
    return C0

#
# Définition des systèmes différentiels
#

# Intégration du système différentiel par odeint de python
def IntODE2(SysDif,C0,time,arg1):
    """ Integration d'un système différentiel d'ordre 2 par odeint
        SysDif : nom de la routine définissant le système différentiel
        C0     : vecteur des conditions initiales
        time   : vecteur temps
        
        La fonction retourne un vecteur contenant les abscisses et vitesse
    """
    x,x_point = odeint(SysDif,C0,time,args=(arg1,)).T
    return array([x, x_point])
    
# définition du système différentiel pour le pendule linéaire non amorti
def PenduleLineaire(theta,t,Omega2):
    """ Système différentiel d'un pendule simple linéaire non amorti
        theta  : vecteur contenant la position et la vitesse angulaire
        t      : variable temps
        Omega2 : carré de la pulsation de l'oscillateur        
    """
    return array([theta[1], -Omega2*theta[0]])   
    

# définition du système différentiel pour le pendule non linéaire non amorti
def PenduleNonLineaire(theta,t,Omega2):
    """ Système différentiel d'un pendule simple non linéaire non amorti
        theta  : vecteur contenant la position et la vitesse angulaire
        t      : variable temps
        Omega2 : carré de la pulsation de l'oscillateur        
    """
    return array([theta[1], -Omega2*sin(theta[0])]) 
    
# définition du système différentiel pour le pendule linéaire amorti
def PenduleLineaireAmorti(theta,t,Tau,Omega2):
    """ Système différentiel d'un pendule simple linéaire amorti
        theta  : vecteur contenant la position et la vitesse angulaire
        t      : variable temps
        Tau    : temps de relaxation du pendule
        Omega2 : carré de la pulsation de l'oscillateur
    """    
    return array([theta[1],  -theta[1]/Tau - Omega2*theta[0]])
    
# calcul du régime d'un oscillateur linéaire amorti
def RegimeOscillateur(Omega2, Tau):
    """ Calcul du régime d'un pendule simple amorti
        Discriminant de l'équation différentielle    
        Omega2 : carré de la pulsation de l'oscillateur
        Tau    : temps de relaxation du pendule
    """
    return ((1.0/Tau)**2 - 4*Omega2)


# définition du système différentiel pour le pendule non linéaire amorti forcé
def PenduleChaos(theta,t,K,Omega2,A,OmegaF):
    """ Système différentiel d'un pendule simple non linéaire amorti forcé
        theta  : vecteur contenant la position et la vitesse angulaire
        t      : variable temps
        Omega2 : carré de la pulsation de l'oscillateur
        K      : facteur d'amortissement
        A      : amplitude du signal de forçage
        OmegaF : pulsation du signal de forçage        
    """ 
    return array([theta[1], -K*theta[1]-Omega2*sin(theta[0])+A*sin(OmegaF*t)])


# définition du système différentiel de l'oscillateur de Van der Pol
def VanDerPol(X,t):
    """ Système différentiel de l'oscillateur de Van der Pol
        X  : vecteur contenant l'abscisse et la vitesse
        t  : variable temps
    """ 
    epsilon = 1.0
    return array([X[1], epsilon*(1 - X[0]*X[0])*X[1] - X[0]])   
    
    
#
# Routines d'affichage
#

# Affichage de la trajectoire d'un oscillateur
def AffTrajectoire(NumFig,theta,t):
    """ Affichage de la trajectoire d'un oscillateur harmonique
        NumFig : numéro de la figure
        t      : vecteur temps
        x      : vecteur position/vitesse issu de l'intégration
    """
    figure(NumFig)
    grid(True)
    plot(t, theta)
    t0 = min(t)
    tmax = max(t)
    xlim(t0,tmax)
    xlabel('$temps$', fontsize = 20)
    ylabel('$\\theta$', fontsize = 20)
    title('Trajectoire', fontsize = 15)
    return
    
# Affichage du diagramme de phase d'un oscillateur
def AffDiagPhase(NumFig,theta,theta_point):
    """ Affichage de la trajectoire d'un oscillateur harmonique
        NumFig : numéro de la figure
        x      : vecteur position/vitesse issu de l'intégration
    """
    figure(NumFig)
    grid(True)
    plot(theta, theta_point)
    xlabel('$\\theta$', fontsize = 20)
    ylabel('$\dot{\\theta}$', fontsize = 20)
    title('Diagramme de phase', fontsize = 15)
    return
    
# Affichage de la trajectoire et du diagramme de phase d'un oscillateur
def AfficheTrajDiag(NumFig,theta, theta_point,t) :
    """ Affichage de la trajectoire d'un oscillateur harmonique
        NumFig     : numéro de la figure
        theta      : vecteur position
        theta_point: vecteur vitesse
        t          : vecteur temps
    """
    figure(NumFig)    
    subplot(221)
    grid(True)
    plot(t, theta)
    xlim(min(t),max(t))
    xlabel('$temps$', fontsize = 20)
    ylabel('$\\theta$', fontsize = 20)

    subplot(222)
    grid(True)
    plot(theta, theta_point)
    xlabel('$\\theta$', fontsize = 20)
    ylabel('$\dot{\\theta}$', fontsize = 20)
    
