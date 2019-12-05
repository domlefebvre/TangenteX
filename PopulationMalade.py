# -*- coding: Latin-1 -*-
# programme de simulation d'une population d'animaux infectés
# Dominique Lefebvre pour TangenteX.com
# 7 février 2017
#

# importation des librairies
from scipy import array, sin, arange, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# paramètres de la simulation
NbInit = 100     # effectif initial de la population
NbInfInit = 1    # effectif initial infecté
NbMortInit = 0   # effectif initial mort
Pop0 = [NbInit,NbInfInit,NbMortInit]

# définition du système différentiel
def Evolution(Pop,t):
    x,y,z = Pop
    # système différentiel
    x1 = -c*x*y        # contamination
    y1 = c*x*y - l*y   # variation de la population infectée
    z1 = l*y           # mortalité de la population infectée
    return [x1,y1,z1]

# définition du vecteur temps de l'expérience
t0 = 0.0
tmax = 10.0
pastemps = 0.1
time = arange(t0, tmax, pastemps)


# lancement de la simulation
plt.figure(1)
plt.grid(True)

# simulation 1
c = 0.1          # contagiosité
l = 0.3          # létalité
# intégration
Pop = odeint(Evolution,Pop0,time)
# affichage du résultat
plt.subplot(221)
plt.grid(True)
plt.plot(time, Pop[:,0],'green',label="Sains")    # population saine
plt.plot(time, Pop[:,1],'red',label="Malades")    # population malade
plt.plot(time, Pop[:,2],'black',label="Morts")    # population morte
plt.legend(loc='upper right', shadow=True)
plt.xlim((t0,tmax))
plt.ylim((0,NbInit))
plt.xlabel('temps')
plt.ylabel('effectif')

# simulation 2
c = 0.1         # taux d'infection
l = 4.0         # taux de mortalité
# intégration
Pop = odeint(Evolution,Pop0,time)
# affichage du résultat
plt.subplot(222)
plt.grid(True)
plt.plot(time, Pop[:,0],'green',label="Sains")    # population saine
plt.plot(time, Pop[:,1],'red',label="Malades")    # population malade
plt.plot(time, Pop[:,2],'black',label="Morts")    # population morte
plt.xlim((t0,tmax))
plt.ylim((0,NbInit))
plt.xlabel('temps')
plt.ylabel('effectif')

# simulation 3
c = 3.0        # taux d'infection
l = 5.0         # taux de mortalité
# intégration
Pop = odeint(Evolution,Pop0,time)
# affichage du résultat
plt.subplot(223)
plt.grid(True)
plt.plot(time, Pop[:,0],'green',label="Sains")    # population saine
plt.plot(time, Pop[:,1],'red',label="Malades")    # population malade
plt.plot(time, Pop[:,2],'black',label="Morts")    # population morte
plt.xlim((t0,tmax))
plt.ylim((0,NbInit))
plt.xlabel('temps')
plt.ylabel('effectif')
