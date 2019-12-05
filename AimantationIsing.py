# -*- coding: Latin-1 -*-
# programme d'�tude de la transition de phase ferro-para magn�tique
# par le mod�le d'Ising - Etat d'�quilibre du r�seau
# Dominique Lefebvre pour TangenteX.com
# 29 avril 2017
#

# importation des librairies
from scipy import ones, exp
import time
from numpy.random import random, randint
from matplotlib.pyplot import figure, grid, xlabel, ylabel, plot, show

# Fonction d'initialisation du r�seau de spins (matrice carr�e de NxN)
def InitReseau(N):    
    Res = ones([N,N],int)  # tous les spins sont � 1
    return Res
    
# Fonction de calcul de l'�nergie totale du r�seau
def EnergieTotale(nw,n):
    energie = 0.0
    for i in range(n):
        for j in range(n):
            energie += nw[i][j]
    return -2*Je*energie

# Fonction de calcul de l'aimantation totale du r�seau
def AimantationTotale(nw,n):
    aimantation = 0.0
    for i in range(n):
        for j in range(n):
            aimantation += nw[i][j]
    return aimantation/n**2    
    
# Fonctions de calcul des variations
def DeltaE(nw,i,j,n):
    # calcul de l'�nergie du voisinage aux conditions de bord p�riodiques
    Ev = nw[i-1][j] + nw[(i+1)%n][j] + nw[i][j-1] + nw[i][(j+1)%n]
    # calcul et retour de la variation d'�nergie du r�seau
    return 2.*Je*Ev*nw[i][j]
    
def DeltaM(nw,i,j,n):
    # calcul et retour de la variation d'aimantation
    return -2.*nw[i][j]/n**2
    
# Fonction d'�volution du r�seau de spin avec condition de Metropolis
def EvolSpin(nw,n,Temp):
    # choix al�atoire du spin � faire varier
    i = randint(0,n-1)
    j = randint(0,n-1)
    # calcul des variations d'�nergie et d'aimantation
    dE = DeltaE(nw,i,j,n)
    dM = DeltaM(nw,i,j,n)
    # application de l'algorithme de Metropolis
    if random() < exp(-dE/(Kb*Temp)):
        nw[i][j] = -nw[i][j]   # inversion du spin
    else:
        dE = dM = 0
    return[nw, dE, dM]
    
# D�finition du r�seau (N,N) avec la valeur initiale des spin = 1
N = 200
Reseau = InitReseau(N)
Gen = 300000

# Param�tres physiques de la manip
Kb = 1.                                  # constante de Boltzmann
Je = 1.                                  # constante d'�change
T = 5.0                                  # temp�rature initiale
Er = [EnergieTotale(Reseau,N)]           # �nergie initiale du r�seau
Ai = [AimantationTotale(Reseau,N)]       # aimantation initiale du r�seau

# boucle d'�quilibre thermique � T
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




