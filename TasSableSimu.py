#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Simulation d'avalanches sur un tas de sable
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "12 février 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
import time, pickle
from scipy import zeros
from numpy.random import randint, normal

# fonction du tirage aléatoire site loi uniforme
def TirageSiteUniforme(n):
    i = randint(0,n-1)
    j = randint(0,n-1)    
    return i,j
    
# fonction du tirage aléatoire site loi gaussienne
def TirageSiteGaussien(n,moyenne, ecart):
    i = int(normal(moyenne,ecart))
    j = int(normal(moyenne,ecart)) 
    if i > n-1:
        i = n-1
    if j > n-1:
        j = n-1
    return i,j

# fonction de détection et de traitement des avalanches
def DetectionAvalanche(tas,n):
    nbav = 0      # nombre d'avalanches
    nbgrains = 0  # nombre de grains impliqués dans les avalanches
    indicav = True   # indicateur d'avalanches
    
    # boucle de traitement des avalanches    
    while indicav :        
        # traitement des sites intérieurs
        for i in xrange(1,n-1):
            for j in xrange(1, n-1):                      
                # détection de pente critique
                if tas[i][j] - tas[i][j+1] > Zc or \
                   tas[i][j] - tas[i][j-1] > Zc or \
                   tas[i][j] - tas[i+1][j] > Zc or \
                   tas[i][j] - tas[i-1][j] > Zc :                      
                       # éboulement des grains sur le voisinage                      
                       tas[i][j] = tas[i][j] - 4    
                       tas[i+1][j] += 1
                       tas[i-1][j] += 1
                       tas[i][j+1] += 1
                       tas[i][j-1] += 1
                       nbgrains += 4
                       nbav += 1
                else:
                     indicav = False                 
        # traitement des bords (conditions aux limites = 0)
        for i in xrange(n):
            tas[i][0] = 0
            tas[i][-1] = 0
        for j in xrange(n):
            tas[0][j] = 0
            tas[-1][j] = 0                 
    
    return tas,nbav,nbgrains
    
# définition du réseau simulant le tas
N = 40                  # taille du réseau carré
Tas = zeros([N,N],int)  # réseau pour la simulation

# définition des paramètres de la simulation
NbIter = 100000
PasGrain = 1
Zc = 3
# paramètres de la gaussienne de distribution des grains
mu = int(N/2)
sigma = 5
# initialisation des listes de stockage des résulats
NbAvalanches = []
NbGrains = []
Remplissage = []

# boucle de simulation
t0 = time.time()
print "Temps de calcul estimé : %3.1f minutes\n" % (int((0.7*NbIter*1e-2)/60))
for k in xrange(NbIter):   
    # désignation d'un site aléatoire
    i,j = TirageSiteUniforme(N)
    # ajout de grain de sable
    Tas[i][j] += PasGrain
    # application des règles de simulation d'avalanche  
    Tas, NbAval,NbGr = DetectionAvalanche(Tas,N) 
    NbAvalanches.append(NbAval)
    NbGrains.append(NbGr)
    # calcul et stockage du remplissage
    Remplissage.append(Tas.sum())
print "Temps de calcul : %3.1f minutes\n" % (int((time.time() - t0)/60))

# sauvegarde des paramètres et des résultats pour exploitation ultèrieure
fic = open('Data/TasSableZc3.dat','w')
pickle.dump(N,fic)
pickle.dump(NbIter,fic)
pickle.dump(Zc,fic)
pickle.dump(PasGrain,fic)
pickle.dump(Tas,fic)
pickle.dump(NbAvalanches,fic)
pickle.dump(NbGrains,fic)
pickle.dump(Remplissage,fic)
fic.close()

print "Fin de simulation \n"

