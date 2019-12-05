#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Simulation d'un paquet d'ondes à enveloppe gaussienne """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "4 septembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import sin, cos, exp, zeros, pi, sqrt, arange
from scipy.constants import h, hbar, e, m_e
from scipy.integrate import simps
from matplotlib.pyplot import figure,plot,xlim,xlabel,ylabel,grid,title,show,ion, ioff


# définition des constantes - les constantes physiques standard sont
# tirées du package scipy.constants
DeuxPi = 2.0*pi
L = 5.0e-9             # dimension de la boite quantique (USI)  

# définition du domaine spatial et temporel
Nx = 1001    # nombre de pas d'intégration sur le domaine spatial
xmin = 0.0
xmax = L
dx = (xmax-xmin)/Nx
x = arange(0.0,L,dx)

# définition des paramètres du paquet d'onde inital
x0 = x[Nx/4]                 # position initiale du paquet
sigma = 2.e-10               # largeur du paquet en m
Lambda = 1.5e-10             # longeur d'onde de de Broglie l'électron (en m)
Ec = (h/Lambda)**2/(2*m_e*e) # énergie cinétique théorique de l'électron (en eV)

# définition des coefficients constants
a1 = -(hbar**2/(2*m_e*e*dx**2))

# initialisation des buffers de calcul aux conditions initiales
Psi_Real = zeros(Nx)
Psi_Imag = zeros(Nx)
Psi_Prob = zeros(Nx)

# calcul de la fonction d'onde initiale
Psi_Real = exp(-0.5*((x-x0)/sigma)**2)*cos(DeuxPi*(x-x0)/Lambda)
Psi_Imag = exp(-0.5*((x-x0)/sigma)**2)*sin(DeuxPi*(x-x0)/Lambda)
# normalisation du paquet d'onde
PsiPsiC = Psi_Real**2 + Psi_Imag**2
C = simps(PsiPsiC,x)
Psi_Real = Psi_Real/sqrt(C)
Psi_Imag = Psi_Imag/sqrt(C)
Psi_Prob = Psi_Real**2 + Psi_Imag**2
# calcul de l'énergie moyenne transportée par le paquet
En = zeros(Nx)
En[1:-1] = a1*(Psi_Real[1:-1] - 1j*Psi_Imag[1:-1]) \
           *(Psi_Real[2:] - 2*Psi_Real[1:-1] + Psi_Real[:-2] \
           + 1j*(Psi_Imag[2:] - 2*Psi_Imag[1:-1] + Psi_Imag[:-2]))                     
Ebarre = simps(En,x)
print "Energie theorique : " + str(Ec) + " eV"
print "Energie moyenne du paquet : " + str(Ebarre.real) + " eV"
                     
# affichage de l'état du paquet d'ondes initial
ion()
figure(1)
grid(True)
plot(x*1.e9, Psi_Real,'blue')
plot(x*1.e9, Psi_Imag,'red')
xlim(xmin*1.e9, xmax*1.e9)
xlabel('x [nanometre]', fontsize = 15)
ylabel('Amplitude de probabilite', fontsize = 15)
title('Evolution', fontsize = 15)

figure(2)
grid(True)
plot(x*1.e9, Psi_Prob,'green')
xlim(xmin*1.e9, xmax*1.e9)
xlabel('x [nanometre]', fontsize = 15)
ylabel('$\Psi \Psi^*$', fontsize = 20)
title('Densite de probabilite de detection', fontsize = 15)
ioff()
show()
