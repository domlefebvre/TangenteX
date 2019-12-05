# -*- coding: Latin-1 -*-
# programme d'étude de la transition de phase ferro-para magnétique
# par le modèle d'Ising - Transition de phase
# Dominique Lefebvre pour TangenteX.com
# 30 avril 2017
#

# importation des librairies
import time
from scipy import ones, exp, linspace
from numpy.random import random, randint
from matplotlib.pyplot import figure, grid, xlabel, ylabel, plot, show, title, axis

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
    Ev = nw[i-1][j] + nw[(i+1)%n][j] + nw[i][j-1] + nw[i][(j+1)%n]
    return 2.*Je*Ev*nw[i][j]
    
def DeltaM(nw,i,j,n):
    # calcul et retour de la variation d'aimantation
    return -2.*nw[i][j]/n**2
    
# Définition du réseau (N,N) avec la valeur initiale des spin = 1
N = 200
Gen = 200000
Reseau = InitReseau(N)
Energie = []
Aimantation = []

# Paramètres physiques de la manip
kB = 1.                           # constante de Boltzmann
Je = 1.                           # constante d'échange
T = 5.0                           # température initiale
Er = EnergieTotale(Reseau,N)      # énergie initiale du réseau
Ai = AimantationTotale(Reseau,N)  # aimantation initiale du réseau

# Vecteur Temperature pour test
Temperature = linspace(T,0.1,99)

# Variables pour sauvegarde du réseau aux températures sélectionnées
TempSelection = (T,4.0,3.0,2.5,2.0,0.5)
ListeReseau = []

# boucle principale d'évolution du réseau en fonction de la température
t0 = time.time()
for t in Temperature:   
    # calcul de l'état du réseau pour une température donnée    
    for i in xrange(Gen):
        # choix aléatoire du spin à faire varier
        i = randint(0,N-1)
        j = randint(0,N-1)
        # calcul des variations d'énergie et d'aimantation
        dE = DeltaE(Reseau,i,j,N)
        dM = DeltaM(Reseau,i,j,N)
        # application de l'algorithme de Metropolis
        if random() < exp(-dE/(kB*t)):
            Reseau[i][j] = -Reseau[i][j]   # inversion du spin
        else:
           dE = dM = 0.0
        Er = Er + dE
        Ai = Ai + dM
    Energie.append(Er)
    Aimantation.append(Ai)
    # sauvegarde du réseau pour les températures sélectionnées
    if t in TempSelection:
        ListeReseau.append(Reseau.tolist())
        print("Sauvegarde du reseau pour T = %.1f" % (t))
print "temps de calcul : %d secondes\n" % (time.time() - t0)
       
# affichage
figure(1)
grid(True)
xlabel('Temperature')
ylabel('Energie')
plot(Temperature,Energie)

figure(2)
grid(True)
xlabel('Temperature')
ylabel('Aimantation moyenne')
plot(Temperature,Aimantation)

# tracé des configurations du réseau pour les différentes températures
fig = figure(3)
for n in range(len(TempSelection)):
    axe = fig.add_subplot(3, 2, n+1) 
    axe.set_xticklabels([]);axe.set_yticklabels([])
    axe.imshow(ListeReseau[n], origin='upper', interpolation='nearest') 
    title('T = %.1f'%TempSelection[n]);
    axis('tight')
show()


