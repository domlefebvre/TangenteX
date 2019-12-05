# -*- coding: Latin-1 -*-
# calcul du seuil de percolation sur un réseau carré
# Dominique Lefebvre pour TangenteX.com
# 6 janvier 2016
#
from numpy import zeros, arange, exp
from numpy.random import rand
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

"""
calcul du seuil de percolation

"""
# D�finition des �tats possibles des sites
ISOLANT = 0.0       # en blanc
CONDUCTEUR = 1.0    # en rouge
PERCO = 0.5         # en vert

# D�finition des param�tres de la simulation
N = 50
    
# D�finition de la fonction sigmo�de
def Sigmoide(x,x0,k,a,c):
    return a/(1.0 + exp(-k*(x-x0))) + c
     
# Fonction de cr�ation de la matrice carr�e de simulation.
# la probabilit� p repr�sente la proportion de billes conductrices parmi
# l'ensemble des billes.
def Grid(n,p):
    grid = zeros((n,n))
    for i in range(n):
        for j in range(n):
            if rand() < p:
                grid[i][j] = CONDUCTEUR
    return grid

# Algorithme de percolation isolant/conducteur
def Percolate(grid,n):
    pgrid = grid.copy()
    chemin = []
    # recherche des particules conductrices en haut de la matrice    
    for j in range(n):
        if pgrid[0][j] == CONDUCTEUR:
            chemin.append((0,j))
            pgrid[0][j] = PERCO
    # recherche d'un chemin percolant      
    while len(chemin) > 0:
        (i,j) = chemin.pop()
        pgrid[i][j] = PERCO
        if i > 0 and pgrid[i-1][j] == CONDUCTEUR:
            chemin.append((i-1,j))
            pgrid[i-1][j] = PERCO
        if i < n-1 and pgrid[i+1][j] == CONDUCTEUR:
            chemin.append((i+1,j))
            pgrid[i+1][j] = PERCO
        if j > 0 and pgrid[i][j-1] == CONDUCTEUR:
            chemin.append((i,j-1))
            pgrid[i][j-1] = PERCO
        if j < n-1 and pgrid[i][j+1] == CONDUCTEUR:
            chemin.append((i,j+1))
            pgrid[i][j+1] = PERCO
    return pgrid

# Fonction de calcul de la densit� de percolation
def PercolateDensity(grid,n):
    a,b = 0.0,0.0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == PERCO:
                a += 1.
            elif grid[i][j] == CONDUCTEUR:
                b += 1.
    if a+b > 0:
        return a/(a+b)
    else:
        return 0

# Fonction de calcul de la densit� de probabilit� de percolation
# pour un �chantillon de NbEch donn�
def DPM(p):
    d = 0.0
    for i in range(NbEch):
        mat = Grid(N,p)
        pmat = Percolate(mat,N)
        d += PercolateDensity(pmat,N)
    densite = d/NbEch
    return densite

# D�finition des param�tres du calcul
PasProba = 0.01
NbEch = 40
    
# pour chaque probabilit� p comprise entre 0.0 et 1.0 par pas de 0.05
# calculer la densit� de probablit� pour un �chantillon de NbEss
# essais de percolations.
px = arange(0.0,1.0,PasProba)
y = [DPM(p) for p in px]
     
# trac� de la courbe DPM(p)
plt.plot(px,y)
plt.grid()

# regression sigmo�de
# popt[0] = x0  donne le point d'inflexion
# popt[1] = k
# popt[2] = a
# popt[3] = c
popt,pcov = curve_fit(Sigmoide,px,y)
print popt
y = Sigmoide(px,*popt)
plt.plot(px,y,'red')

plt.show()




