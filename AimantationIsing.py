# -*- coding: Latin-1 -*-
# programme d'étude de la transition de phase ferro-para magnétique
# par le modèle d'Ising - Etat d'équilibre du réseau
# Dominique Lefebvre pour TangenteX.com
# 29 avril 2017
#

# importation des librairies
from scipy import ones, exp
import time
from numpy.random import random, randint
from matplotlib.pyplot import figure, grid, xlabel, ylabel, plot, show

# Fonction d'initialisation du réseau de spins (matrice carrée de NxN)
def InitReseau(N):    
    Res = ones([N,N],int)  # tous les spins sont à 1
    return Res
    
# Fonction de calcul de l'énergie totale du réseau
def EnergieTotale(nw,n):
    energie = 0.0
    for i in range(n):
        for j in range(n):
            energie += nw[i][j]
    return -2*Je*energie

# Fonction de calcul de l'aimantation totale du réseau
def AimantationTotale(nw,n):
    aimantation = 0.0
    for i in range(n):
        for j in range(n):
            aimantation += nw[i][j]
    return aimantation/n**2    
    
# Fonctions de calcul des variations
def DeltaE(nw,i,j,n):
    # calcul de l'énergie du voisinage aux conditions de bord périodiques
    Ev = nw[i-1][j] + nw[(i+1)%n][j] + nw[i][j-1] + nw[i][(j+1)%n]
    # calcul et retour de la variation d'énergie du réseau
    return 2.*Je*Ev*nw[i][j]
    
def DeltaM(nw,i,j,n):
    # calcul et retour de la variation d'aimantation
    return -2.*nw[i][j]/n**2
    
# Fonction d'évolution du réseau de spin avec condition de Metropolis
def EvolSpin(nw,n,Temp):
    # choix aléatoire du spin à faire varier
    i = randint(0,n-1)
    j = randint(0,n-1)
    # calcul des variations d'énergie et d'aimantation
    dE = DeltaE(nw,i,j,n)
    dM = DeltaM(nw,i,j,n)
    # application de l'algorithme de Metropolis
    if random() < exp(-dE/(Kb*Temp)):
        nw[i][j] = -nw[i][j]   # inversion du spin
    else:
        dE = dM = 0
    return[nw, dE, dM]
    
# Définition du réseau (N,N) avec la valeur initiale des spin = 1
N = 200
Reseau = InitReseau(N)
Gen = 300000

# Paramètres physiques de la manip
Kb = 1.                                  # constante de Boltzmann
Je = 1.                                  # constante d'échange
T = 5.0                                  # température initiale
Er = [EnergieTotale(Reseau,N)]           # énergie initiale du réseau
Ai = [AimantationTotale(Reseau,N)]       # aimantation initiale du réseau

# boucle d'équilibre thermique à T
t0 = time.time()
for i in xrange(Gen):
    Reseau,dE,dM = EvolSpin(Reseau,N,T)
    Er.append(Er[i]+dE)
    Ai.append(Ai[i]+dM)
print "temps de calcul : %d secondes\n" % (time.time() - t0)
    
    
# affichage
figure(1)
grid(True)
xlabel('Generation')
ylabel('Energie')
plot(Er)

figure(2)
grid(True)
xlabel('Generation')
ylabel('Aimantation moyenne')
plot(Ai)

show()




