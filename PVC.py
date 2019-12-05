# -*- coding: Latin-1 -*-
# programme de résolution du problème du voyaguer de commerce
# par l'algorithme du recuit simulé
# Dominique Lefebvre pour TangenteX.com
# 14 mars 2017

# importation des librairies
from scipy import *
from matplotlib.pyplot import *

# paramètres du problème
N = 20    # nombre de villes

# paramètres de l'algorithme de recuit simulé
T0 = 10.0
Tmin = 1e-2
tau = 1e4

# fonction de calcul de l'énergie du système, égale à la distance totale
# du trajet selon le chemin courant
def EnergieTotale():
    global trajet
    energie = 0.0
    coord = c_[x[trajet],y[trajet]]
    energie = sum(sqrt(sum((coord - roll(coord,-1,axis=0))**2,axis=1)))
    return energie

# fonction de fluctuation autour de l'état "thermique" du système
def Fluctuation(i,j):
    global trajet
    Min = min(i,j)
    Max = max(i,j)
    trajet[Min:Max] = trajet[Min:Max].copy()[::-1]
    return

# fonction d'implémentation de l'algorithme de Metropolis
def Metropolis(E1,E2):
    global T
    if E1 <= E2:
        E2 = E1  # énergie du nouvel état = énergie système
    else:
        dE = E1-E2
        if random.uniform() > exp(-dE/T): # la fluctuation est retenue avec  
            Fluctuation(i,j)              # la proba p. sinon retour trajet antérieur
        else:
            E2 = E1 # la fluctuation est retenue 
    return E2
    
# initialisation des listes d'historique
Henergie = []     # énergie
Htemps = []       # temps
HT = []           # température

# répartition aléatoire des N villes sur le plan [0..1,0..1]
x = random.uniform(size=N)
y = random.uniform(size=N)

# défintion du trajet initial : ordre croissant des villes
trajet = arange(N)
trajet_init = trajet.copy()

# calcul de l'énergie initiale du système (la distance initiale à minimiser)
Ec = EnergieTotale()

# boucle principale de l'algorithme de recuit simulé
t = 0
T = T0
while T > Tmin:
    # choix de deux villes différentes au hasard
    i = random.random_integers(0,N-1)
    j = random.random_integers(0,N-1)
    if i == j: continue
        
    # création de la fluctuation et mesure de l'énergie
    Fluctuation(i,j) 
    Ef = EnergieTotale()   
    Ec = Metropolis(Ef,Ec)
    
    # application de la loi de refroidissement    
    t += 1
    T = T0*exp(-t/tau)  

    # historisation des données
    if t % 10 == 0:
        Henergie.append(Ec)
        Htemps.append(t)
        HT.append(T)

# fin de boucle - affichage des états finaux
# affichage du réseau
fig1 = figure(1)
subplot(1,2,1)
xticks([])
yticks([])
plot(x[trajet_init],y[trajet_init],'k')
plot([x[trajet_init[-1]], x[trajet_init[0]]],[y[trajet_init[-1]], \
      y[trajet_init[0]]],'k')
plot(x,y,'ro')
title('Trajet initial')

subplot(1,2,2)
xticks([])
yticks([])
plot(x[trajet],y[trajet],'k')
plot([x[trajet[-1]], x[trajet[0]]],[y[trajet[-1]], y[trajet[0]]],'k')
plot(x,y,'ro')
title('Trajet optimise')
show()

# affichage des courbes d'évolution
fig2 = figure(2)
subplot(1,2,1)
semilogy(Htemps, Henergie)
title("Evolution de l'energie totale du systeme")
xlabel('Temps')
ylabel('Energie')
subplot(1,2,2)
semilogy(Htemps, HT)
title('Evolution de la temperature du systeme')
xlabel('Temps')
ylabel('Temperature')
    
