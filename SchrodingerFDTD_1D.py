#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" résolution Schrödinger 1D par la méthode FDTD """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 septembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import sin, cos, exp, zeros, pi, sqrt, arange
from scipy.constants import h, hbar, e, m_e
from scipy.integrate import simps
from matplotlib.pyplot import figure,axis,plot,pause,show,ion,ioff,savefig,grid,xlabel,ylabel, title

# définition des constantes - les constantes physiques standards sont
# tirées du package scipy.constants
DeuxPi = 2.0*pi
L = 5.0e-9             # dimension de la boite quantique (USI)  

# définition du domaine spatial et temporel
Nx = 1001    # nombre de pas d'intégration sur le domaine spatial
xmin = 0.0
xmax = L
dx = (xmax-xmin)/Nx
x = arange(0.0,L,dx)

Nt = 15000                    # nombre de pas d'intégration sur le domaine temporel
PasAff = 1000
a2 = 0.1
dt = a2*2*m_e*dx**2/hbar
a3 = e*dt/hbar

# définition des paramètres du paquet d'onde inital
x0 = x[Nx/4]                 # position initiale du paquet
sigma = 2.0e-10              # largeur du paquet en m
Lambda = 1.5e-10             # longeur d'onde de de Broglie l'électron (en m)
Ec = (h/Lambda)**2/(2*m_e*e) # énergie cinétique théorique de l'électron (en eV)

# définition du potentiel
U = zeros(Nx)          # particule libre dans le puit

# initialisation des buffers de calcul aux conditions initiales
Psi_Real = zeros(Nx)
Psi_Imag = zeros(Nx)
Psi_Prob = zeros(Nx)

# calcul et affichage de la fonction d'onde initiale
Psi_Real = exp(-0.5*((x-x0)/sigma)**2)*cos(DeuxPi*(x-x0)/Lambda)
Psi_Imag = exp(-0.5*((x-x0)/sigma)**2)*sin(DeuxPi*(x-x0)/Lambda)
# normalisation du paquet d'onde
PsiPsiC = Psi_Real**2 + Psi_Imag**2
C = simps(PsiPsiC,x)
Psi_Real = Psi_Real/sqrt(C)
Psi_Imag = Psi_Imag/sqrt(C)
Psi_Prob = Psi_Real**2 + Psi_Imag**2

# initialisation graphique
ion()                 # mode interactif
fig = figure()
ymax = Psi_Real.max()
axis([xmin*1.e9,xmax*1.e9,-ymax,ymax])
grid(True)
xlabel('x [nanometre]', fontsize = 15)
ylabel('Amplitude de probabilite', fontsize = 15)
title('Evolution', fontsize = 15)

# tracé de la fonction d'onde initiale
linePsiR, = plot(x*1.e9,Psi_Real,'blue')
linePsiI, = plot(x*1.e9,Psi_Imag,'red')     
linePsiP, = plot(x*1.e9,Psi_Prob/1.e5,'green')

# boucle de calcul et d'affichage de l'évolution
for t in range(Nt):
    Psi_Real[1:-1] = Psi_Real[1:-1] - a2*(Psi_Imag[2:] - 2*Psi_Imag[1:-1] + Psi_Imag[:-2]) \
                     + a3*U[1:-1]*Psi_Imag[1:-1]
    Psi_Imag[1:-1] = Psi_Imag[1:-1] + a2*(Psi_Real[2:] - 2*Psi_Real[1:-1] + Psi_Real[:-2]) \
                     - a3*U[1:-1]*Psi_Real[1:-1]
    Psi_Prob[1:-1] = Psi_Real[1:-1]**2 + Psi_Imag[1:-1]**2
    if t % PasAff == 0:        
        linePsiR.set_ydata(Psi_Real)
        linePsiI.set_ydata(Psi_Imag)
        linePsiP.set_ydata(Psi_Prob/1.e5)
        pause(0.2)

print('Fin de calcul')
ioff()   # sortir du mode interactif

   
