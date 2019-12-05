#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Analyse des données de simulation d'avalanches sur un tas de sable
"""

__author__      = "Dominique Lefebvre"
__copyright__   = "Copyright 2019 - TangenteX.com"
__version__     = "1.0"
__date__        = "28 février 2019" 
__email__       = "dominique.lefebvre@tangentex.com"

# importation des librairies
from scipy import arange,meshgrid
import pickle
from scipy.fftpack import fft, fftfreq
from matplotlib.pyplot import figure,grid,show,plot,xlabel,ylabel,\
                              title,loglog,semilogy,psd,imshow
import matplotlib.mlab as mlab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


# fonction de construction de la distribution de probabilité des avalanches
def DistributionProba(Liste):
    densiteproba = []
    Max = max(Liste)+1
    n = float(len(Liste))
    classes = range(4,Max,4)
    for i in classes:
        nbelem = 0
        for j in Liste:
            if j == i:
                nbelem += 1
        # normalisation à 1 de l'histogramme -> densité de proba        
        densiteproba.append(nbelem/n)       
    return classes,densiteproba
    
# récupération des données de simulation
# Tas : grille NxN de simulation du tas de sable. Chaque case de la grille
#       contient p grains
# NbAvalanches : liste contenant pour chaque itération, le nombre d'avalanches
#                survenues jusqu'à l'équilibre après l'ajout d'un grain de sable.
# NbGrains :     liste contenant pour chaque itération, le nombre de grains
#                impliqués dans les avalanches ayant eu lieu pendant l'itération
# Remplissage :  liste contenant pour chaque itération, la quantité de grains
#                contenus dans le tas de sable
# Attention : les données doivent être récupérées dans le même ordre qu'elles
#             ont été stockées.
fic = open('Data/TasSableZc3.dat','r')
N = pickle.load(fic)
NbIter = pickle.load(fic)
Zc = pickle.load(fic)
PasGrain = pickle.load(fic)
Tas = pickle.load(fic)
NbAvalanches = pickle.load(fic)
NbGrains = pickle.load(fic)
Remplissage = pickle.load(fic)
fic.close()

# définition de l'état stationnaire
T = 50000        # itération de début du régime stationnaire

# affichage du tas de sable en 2D        
fig1 = figure(1,figsize=(10,8)) 
xlabel('X')
ylabel('Y')
title('Hauteur du tas de sable')
imshow(Tas,cmap=cm.binary)   

# affichage du tas de sable 3D
fig2 = figure(2,figsize=(10,8))
ax = Axes3D(fig2)
grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Hauteur')
ax.set_title(u'Modèle du tas de sable')
X = arange(0,N,1.0)
Y = arange(0,N,1.0) 
X, Y = meshgrid(X, Y)
ax.plot_surface(X, Y, Tas, rstride=1, cstride=1, cmap=cm.binary)


# affichage de la courbe de remplissage du tas
fig3 = figure(3,figsize=(10,8))
grid(True)
xlabel(u'Itérations')
ylabel('Nombre de grains')
title('Evolution du remplissage du tas de sable')
plot(Remplissage)

# calcul du remplissage du tas de sable à l'état stationnaire
Vremp = sum(Remplissage[T:])/(NbIter - T)
print "Volume moyen du tas : %3.1f \n" % Vremp
htas = Tas.max()
print "Hauteur max du tas %3.1f grains\n" % htas

# affichage du nombre d'avalanches
fig4 = figure(4,figsize=(10,8))
grid(True)
xlabel(u'Itérations')
ylabel("Nombre d'avalanches")
title("Evolution du nombre d'avalanches")
plot(NbAvalanches)

# affichage de la courbe de la taille des avalanches
fig6 = figure(6,figsize=(10,8))
grid(True)
xlabel(u'Itérations')
ylabel(u'Nombre de grains')
title(u'Taille des avalanches')
plot(NbGrains)

# loi de distribution de la probabilité d'une avalanche en fonction de sa
# taille en nombre de grains
Classes, DistribAv = DistributionProba(NbGrains[T:])
fig7 = figure(7,figsize=(10,8))
grid(True)
xlabel(u"Taille de l'avalanche (en nombre de grains)")
ylabel(u'Probabilité')
title(u"Distribution de probabilité d'une avalanche en fonction de sa taille")
loglog(Classes,DistribAv)


# calcul et affichage du spectre de la taille des avalanches en régime stationnaire
NbEch = 2048              # taille de l'échantillon pour FFT (sur NbEch itérations)
Ech = NbGrains[T:T+NbEch]
X = abs(fft(Ech))/NbEch
freq = fftfreq(len(X))
freq = freq[range(NbEch/2)]
X = X[range(NbEch/2)]

fig8 = figure(8,figsize=(10,8))
grid(True)
xlabel(u"Fréquence (Hz)")
ylabel(u'Amplitude')
title(u"Taille des avalanches - Spectre normalisé")
semilogy(freq,X)

# periodogramme moyen
Echantillon = NbAvalanches[T:]
fig9 = figure(9,figsize=(10,8))
title(u"Energie totale - Densité spectrale")
spectre, frequence = psd(Echantillon,NFFT=512,Fs=1.0,window=mlab.window_none)

fig10 = figure(10,figsize=(10,8))
grid(True)
xlabel(u"Fréquence (Hz)")
ylabel(u'Amplitude spectrale')
title(u"Caractérisation du bruit en 1/f")
loglog(frequence,spectre)

show()