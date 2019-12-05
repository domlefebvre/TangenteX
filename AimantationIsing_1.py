# -*- coding: Latin-1 -*-
# programme d'�tude de la transition de phase ferro-para magn�tique
# par le mod�le d'Ising - Transition de phase
# Dominique Lefebvre pour TangenteX.com
# 30 avril 2017
#

# importation des librairies
import time
from scipy import ones, exp, linspace
from numpy.random import random, randint
from matplotlib.pyplot import figure, grid, xlabel, ylabel, plot, show, title, axis

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
    Ev = nw[i-1][j] + nw[(i+1)%n][j] + nw[i][j-1] + nw[i][(j+1)%n]
    return 2.*Je*Ev*nw[i][j]
    
def DeltaM(nw,i,j,n):
    # calcul et retour de la variation d'aimantation
    return -2.*nw[i][j]/n**2
    
# D�finition du r�seau (N,N) avec la valeur initiale des spin = 1
N = 200
Gen = 200000
Reseau = InitReseau(N)
Energie = []
Aimantation = []

# Param�tres physiques de la manip
kB = 1.                           # constante de Boltzmann
Je = 1.                           # constante d'�change
T = 5.0                           # temp�rature initiale
Er = EnergieTotale(Reseau,N)      # �nergie initiale du r�seau
Ai = AimantationTotale(Reseau,N)  # aimantation initiale du r�seau

# Vecteur Temperature pour test
Temperature = linspace(T,0.1,99)

# Variables pour sauvegarde du r�seau aux temp�ratures s�lectionn�es
TempSelection = (T,4.0,3.0,2.5,2.0,0.5)
ListeReseau = []

# boucle principale d'�volution du r�seau en fonction de la temp�rature
t0 = time.time()
for t in Temperature:   
    # calcul de l'�tat du r�seau pour une temp�rature donn�e    
    for i in xrange(Gen):
        # choix al�atoire du spin � faire varier
        i = randint(0,N-1)
        j = randint(0,N-1)
        # calcul des variations d'�nergie et d'aimantation
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
    # sauvegarde du r�seau pour les temp�ratures s�lectionn�es
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

# trac� des configurations du r�seau pour les diff�rentes temp�ratures
fig = figure(3)
for n in range(len(TempSelection)):
    axe = fig.add_subplot(3, 2, n+1) 
    axe.set_xticklabels([]);axe.set_yticklabels([])
    axe.imshow(ListeReseau[n], origin='upper', interpolation='nearest') 
    title('T = %.1f'%TempSelection[n]);
    axis('tight')
show()


