#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" résolution Schrödinger 1D par la méthode FDTD avec barrière de potentiel """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 septembre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import sin, cos, exp, zeros, pi, sqrt, arange
from scipy.constants import h, hbar, e, m_e
from scipy.integrate import simps
from matplotlib.pyplot import figure,axis,plot,pause,show,ion,ioff,savefig,grid,subplots,close

# définition des constantes - les constantes physiques standards sont
# tirées du package scipy.constants
DeuxPi = 2.0*pi
L = 5.0e-9                   # dimension de la boite quantique (USI)  

# définition du domaine spatial et temporel
Nx = 1001    # nombre de pas d'intégration sur le domaine spatial
xmin = 0.0
xmax = L
dx = (xmax-xmin)/Nx
x = arange(0.0,L,dx)
a1 = -(hbar**2/(2*m_e*e*dx**2))

Nt = 15000                   # nombre de pas d'intégration sur le domaine temporel
PasAff = 1000
a2 = 0.1
dt = a2*2*m_e*dx**2/hbar
a3 = e*dt/hbar

# définition des paramètres du paquet d'onde inital
x0 = x[Nx/4]                 # position initiale du paquet
sigma = 2.e-10               # largeur du paquet en m
Lambda = 1.5e-10             # longeur d'onde de de Broglie l'électron (en m)
Ec = (h/Lambda)**2/(2*m_e*e) # énergie cinétique théorique de l'électron (en eV)

# définition du potentiel
U0 = 80                     # en eV
U = zeros(Nx)
#U[Nx/2:] = U0              # définition d'une marche de potentiel
EppBar = 30                 # largeur de la barrière en nombre de pas dx (0.15 nm)
U[Nx/2:Nx/2+EppBar] = U0    # définition d'une barrière de potentiel

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
ion()                 
fig, axe1 = subplots()
axe2 = axe1.twinx()
ymax = Psi_Prob.max()
axe1.axis([xmin*1.e9,xmax*1.e9,0,ymax*1.e-9 + 6.0])
axe1.grid(True)
axe1.set_xlabel('x [nanometre]')
axe1.set_ylabel('Densite de proba. de detection [m-1]')
axe2.set_ylabel('U [eV]')

# tracé de la fonction d'onde initiale    
linePsiP, = axe1.plot(x*1.e9,Psi_Prob,'green')
# tracé de la barrière de potentiel
lineEner, = axe2.plot(x*1.e9,U,'blue')

# boucle de calcul et d'affichage de l'évolution
for t in range(Nt):
    Psi_Real[1:-1] = Psi_Real[1:-1] - a2*(Psi_Imag[2:] - 2*Psi_Imag[1:-1] + Psi_Imag[:-2]) \
                     + a3*U[1:-1]*Psi_Imag[1:-1]
    Psi_Imag[1:-1] = Psi_Imag[1:-1] + a2*(Psi_Real[2:] - 2*Psi_Real[1:-1] + Psi_Real[:-2]) \
                     - a3*U[1:-1]*Psi_Real[1:-1]
    Psi_Prob[1:-1] = Psi_Real[1:-1]**2 + Psi_Imag[1:-1]**2
    # calcul de l'énergie potentielle
    Ep = U*Psi_Prob
    Ubarre = simps(Ep,x)
    # calcul de l'énergie cinétique moyenne transportée par le paquet
    Ec = zeros(Nx)
    Ec[1:-1] = a1*(Psi_Real[1:-1] - 1j*Psi_Imag[1:-1]) \
               *(Psi_Real[2:] - 2*Psi_Real[1:-1] + Psi_Real[:-2] \
               + 1j*(Psi_Imag[2:] - 2*Psi_Imag[1:-1] + Psi_Imag[:-2]))                     
    Ebarre = simps(Ec,x)
    # calcul de l'énergie totale
    Etbarre = Ubarre + Ebarre
    # affichage
    if t % PasAff == 0:
        linePsiP.set_ydata(Psi_Prob*1.e-9)
        pause(0.1)
    if t == 6000:
        savefig('Schro1D2U_1.png')
    if t == 9000:
        savefig('Schro1D2U_2.png')
    
    
print('Fin de calcul')
ioff()   # sortir du mode interactif
close()

   
