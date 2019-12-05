# -*- coding: Latin-1 -*-
# programme de simulation du problème à 3 corps
# Dominique Lefebvre pour TangenteX.com
# 21 mars 2017

# importation des librairies
from scipy import linspace, pi,arange
from scipy.integrate.odepack import odeint
from matplotlib.pyplot import figure, plot, show

# fonction de définition du système dynamique
# Y est le vecteur contenant les données de position et de vitesse
# du système différentiel
def TroisCorps(Y,t):
    global m1,m2,m3
    dY = arange(12,dtype=float)
    # extraction des coordonnées
    x1 = Y[0]; y1 = Y[2]
    x2 = Y[4]; y2 = Y[6]
    x3 = Y[8]; y3 = Y[10]
    # calcul des distances r(i,j)
    r12 = ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    r13 = ((x1 - x3)**2 + (y1 - y3)**2)**1.5
    r23 = ((x2 - x3)**2 + (y2 - y3)**2)**1.5
    # calcul de l'accélération
    dY[1] = -m2*(x1 - x2)/r12 - m3*(x1 - x3)/r13 
    dY[3] = -m2*(y1 - y2)/r12 - m3*(y1 - y3)/r13
    dY[5] = m1*(x1 - x2)/r12 - m3*(x2 - x3)/r23
    dY[7] = m1*(y1 - y2)/r12 - m3*(y2 - y3)/r23   
    dY[9] = m1*(x1 - x3)/r13 + m2*(x2 - x3)/r23
    dY[11] = m1*(y1 - y3)/r13 + m2*(y2 - y3)/r23   
    # retour des dérivées premières
    dY[0] = Y[1];dY[2] = Y[3]
    dY[4] = Y[5];dY[6] = Y[7]
    dY[8] = Y[9];dY[10] = Y[11]
    return dY
    
# constantes
periode = 2*pi/3.0   # periode pour la solution exacte du problème
dt = 5e-3            # pas de temps pour le calcul
   
# paramètres de la manipulation #################################
nbp = 10        # nombre de periodes
epsp = 0.0    # perturbation de position
epsm = 0.0     # perturbation de masse
#################################################################

# définition des paramètres du système - les paramètres ci-dessous 
# correspondentà la solution exacte du problème à 3 corps proposée 
# par Cris Moore.
# nota : la constante de gravitation G a été fixée à 1
# masses des corps
m1 = 1.0
m2 = 2.0
m3 = 2.0
# introduction d'une perturbation sur la masse
m1 = m1*(1.0 - epsm) 
# position initiale des corps - solution exacte
pos0_1 = [0.97000436,-0.24308753]
# introduction d'une perturbation sur les positions         
pos0_1[0] = pos0_1[0]*(1.0 - epsp)
pos0_1[1] = pos0_1[1]*(1.0 - epsp)
pos0_2 = [-pos0_1[0],-pos0_1[1]]
pos0_3 = [0.0,0.0]  
# vitesse initiale des corps - solution exacte
v0_3 = [-0.93240737,-0.86473146]
v0_2 = [-v0_3[0]/2.0, -v0_3[1]/2.0]
v0_1 = [-v0_3[0]/2.0, -v0_3[1]/2.0]
    
# vecteur conditions initiales du système différentiel
CI = [pos0_1[0],v0_1[0],pos0_1[1],v0_1[1],\
      pos0_2[0],v0_2[0],pos0_2[1],v0_2[1],\
      pos0_3[0],v0_3[0],pos0_3[1],v0_3[1]]

# définition du vecteur temps
tmin = 0
tmax = nbp*periode
nbpas = (tmax - tmin)/dt
t = linspace(tmin, tmax, nbpas)

# résolution du système différentiel
Y = odeint(TroisCorps,CI,t)

# contruction des vecteurs position pour affichage
x1 = Y[:,0]; y1 = Y[:,2]
x2 = Y[:,4]; y2 = Y[:,6]
x3 = Y[:,8]; y3 = Y[:,10]

# affichage des résultats
fig = figure()
plot(x1,y1,'b',x2,y2,'g',x3,y3,'r')
show()
