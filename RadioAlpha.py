#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Simuler la radioactivité alpha en résolvant l'équation de Schrodinger 1D """

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2018 - TangenteX.com"
__version__     = "1.0"
__date__        = "10 octobre 2018" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import pi, ones, zeros, sqrt, log, exp, linspace
from scipy.constants import hbar, e, epsilon_0
from scipy.integrate import simps, quad
from matplotlib.pyplot import figure,plot,show,grid,xlabel,ylabel, title, xlim, ylim

############################################################################
# définition des paramètres physiques 
############################################################################

# facteurs de conversion d'unité et coefficients constants
Fe = 1.6e-13       # facteur de conversion en MeV
Fl = 1.0e-15       # facteur de conversion en fermi (femtometre pour le SI)
C1 = 1./(4.*pi*epsilon_0)

# définition de la barrière coulombienne
U0 = -40.0              # potentiel initial en MeV

# paramètres de la particule alpha (noyau d'hélium)
Malpha = 6.64465723e-27 # masse d'une particule alpha
Zalpha = 2              # Z hélium

# caractéristiques de l'isotope père
Z = 84        # Z Polonium
A = 210       # nombre de masse du noyau père (Polonium 210)
E = 5.4       # énergie de la particule alpha (en MeV)

# caractéristiques du noyau fils
Zf = 82       # Z Plomb

# délimitation de la zone interdite
r0 = 1.07*((A - 4)**(1./3.) + pow(4,1./3.)) 
r1 = C1*Zalpha*(Zf - Zalpha)*e**2/(E*Fe*Fl)        
 

# calcul de l'énergie de la particule alpha
MPo = 209.9824
MPb = 205.9745
MHe = 4.00260
E1 = (MPo - MPb - MHe)*931.5
print 'Energie calculée particule alpha : ',"{0:.2f}".format(E1), ' MeV'
print

############################################################################
# paramètres de la simulation 
############################################################################  
L = 130.0         # distance max en fermi
Nx = 60000
xmin = 0.0
xmax = L
x = linspace(xmin,xmax,Nx)
dx = x[1] - x[0]

############################################################################
# calcul par l'approximation de Gamow 
############################################################################
# définition de la fonction Energie pour intégration du facteur de Gamow
def Up(x):
    y = sqrt(C1*Zf*Zalpha*e**2/x - E*Fe)
    return y
# calcul de la vitesse de la particule alpha et de la fréquence de collision
# avec la barrière coulombienne
Valpha = sqrt(2.*E*Fe/Malpha);
Fcol =  Valpha/(2*r0*Fl);
    
ProbG = exp(-(2./hbar)*sqrt(2*Malpha)*quad(Up,r0*Fl,r1*Fl)[0])
LambdaG = Fcol*ProbG
DVG = log(2.0)/LambdaG
print 'Modèle de Gamow'
print 'Probabilité de sortie : ',"{0:.2e}".format(ProbG)
print 'Constante de désintégration : ',"{0:.2e}".format(LambdaG),'s-1  [5,81 10^-8]'
print 'Demi-vie : ',"{0:.2e}".format(DVG), 's  [1,20 10^7]'
print

############################################################################
# résolution de l'équation de Schrodinger indépendante du temps par la méthode
# des différences finies arrière
############################################################################

# définition de la barrière de potentiel
U = U0*ones(Nx)
for i in range(0,Nx):
    if x[i] > r0 :
        U[i] = C1*Zalpha*(Z - Zalpha)*e**2/(Fl*Fe*x[i])
   
# calcul des indices de x pour lesquels U = Umax et U = E
for i in range(0,Nx):
    if U[i] > U0 :
        ind1 = i
        break
for i in range(Nx-1,ind1+1,-1):   
    if U[i] >= E :
        ind2 = i
        break

# conditions initiales de la fonction d'onde
Psi = zeros(Nx) 
Psi[Nx-2] = 1.e-15

# calcul de la fonction d'onde
for i in range(Nx-2,1,-1): 
    Psi[i-1] = 2*(1 - Fl**2*Fe*((dx**2)*Malpha/(hbar**2)*(E - U[i]))) * Psi[i] - Psi[i+1]

# normalisation de la fonction d'onde
C = simps(Psi**2,x)
Psi = Psi/sqrt(C)

# calcul de l'amplitude Ain de Psi dans le noyau 0 <= r <= r0
AmpIn = max(abs(Psi[:ind1]))
# calcul de l'amplitude Aout de Psi en dehors de la barrière (E>U) r > r1
AmpOut = max(abs(Psi[ind2:]))
# calcul de la probabilité de sortie de la particule alpha
PSortie = (AmpOut/AmpIn)**2

# calcul de la constante de désintégration et de la demi-vie
Lambda = Fcol*PSortie
Demi_vie = log(2.0)/Lambda

print '-----------------------------------------------------'
print
print "Résolution de l'équation de Schrödinger"
print 'Probabilité de sortie : ',"{0:.2e}".format(PSortie)
print 'Constante de désintégration : ',"{0:.2e}".format(Lambda),'s-1  [5,81 10^-8]'
print 'Demi-vie : ',"{0:.2e}".format(Demi_vie), 's  [1,20 10^7]'

############################################################################

figure(1)
grid(True)
xlabel('x [fermi]', fontsize = 15)
ylabel('Energie [MeV]', fontsize = 15)
title('Radioactivite alpha', fontsize = 15)
xlim(xmin, xmax)
ylim(U.min()-1.,U.max()+1.0)
plot(x,U,'red')                    # barrière de potentiel
plot([x[0],x[Nx-1]],[E,E],'blue')  # énergie de la particule alpha
plot(x, 50.*Psi,'green')

figure(2)
grid(True)
xlabel('x [fermi]', fontsize = 15)
ylabel('Psi', fontsize = 15)
title('Effet tunnel', fontsize = 15)
xlim(xmin, xmax)
ylim(U.min()-1.,U.max()+1.0)
plot(x,U,'red')                    # barrière de potentiel
plot([x[0],x[Nx-1]],[E,E],'blue')  # énergie de la particule alpha
plot(x[ind2:], 1.e+15*Psi[ind2:],'green')
show()