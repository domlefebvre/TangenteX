#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Exemple d'utilisation de l'algorithme de Metropolis
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "3 février 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import exp, zeros
import time
from numpy.random import random, randint, random_integers
from matplotlib.pyplot import figure, grid, xlabel, ylabel, title, plot, show

# initialisation du réseau avec une température et une énergie initiales nulles
def InitReseauT0(n):
    res = zeros(n)
    Ei = 1
    return res,Ei
    
# initialisation du réseau avec une température et une énergie initiales aléatoires
def InitReseauAleatoire(n):
    # construction du réseau avec des états aléatoires variant entre 0 et 2    
    res = random_integers(0, 2, n)
    # calcul de l'énergie initiale
    Ei = 0    
    for i in xrange(n):
        Ei += res[i]
    return res,Ei
    
# algorithme de Metropolis
def Metropolis(res,beta,En):
    n = len(res)    
    # choix aléatoire de la particule à traiter
    j = randint(0,n-1)
    # je tire au hasard une variation d'énergie discrète +1 ou -1
    if res[j] == 0:
        dE = 1
    else:
        if random() < 0.5:
            dE = 1
        else:
            dE = -1    
    # si la variation d'énergie est négative, je l'accepte
    if dE == -1:
        res[j] += dE
        En += dE
   # sinon je la prends si la proba est inférieur à exp(-beta*dE)    
    else:
        if random() < exp(-dE*beta):
            res[j] += dE
            En += dE            
    return[res, En]
    
# paramètres de la simulation
N = 500                    # taille du système
Iterations = 1000000         # nombre d'itérations

#définition de l'état initial du réseau hors équilibre
T = 30.0                            # température initiale du réseau
beta = 1.0/T                        # coefficient de Boltzmann simplifié
Reseau, E0 = InitReseauAleatoire(N) # initialisation du réseau
Energie = [E0]                      # énergie initiale du réseau

# état des particules avant thermalisation
figure(1, figsize=(10,8))
xlabel('Reseau')
ylabel('Niveau energie')
title("""Repartition de l'energie avant thermalisation""")
plot(Reseau,'b.')

# boucle de thermalisation
t0 = time.time()
for i in xrange(Iterations):
    En = Energie[i]
    Reseau,En = Metropolis(Reseau,beta,En)
    Energie.append(En)
print "temps de calcul : %3.4f secondes\n" % (time.time() - t0)
        
# courbe d'évolution vers l'état d'équilibre
figure(2)
grid(True)
title("""Courbe d'evolution vers l'equilibre""")
xlabel('Iterations')
ylabel('Energie')
plot(Energie)

# état des particules après thermalisation
figure(3, figsize=(10,8))
xlabel('Reseau')
ylabel('Niveau energie')
title("""Repartition de l'energie apres thermalisation""")
plot(Reseau,'r.')

show()
