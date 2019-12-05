# -*- coding: Latin-1 -*-
# Calculs autour de la loi de Planck
# Dominique Lefebvre pour TangenteX.com
# 29 mars 2018
#

# importation des librairies
from scipy import power,exp,linspace
import matplotlib.pyplot as plt
import matplotlib.ticker as mtk

# Constantes physiques
h = 6.626070e-34   # constante de Planck en J.s
kb = 1.38065e-23   # constante de Boltzmann en J/K
c = 2.99792458e8   # vitesse de la lumière dans le vide en m/s

# Calcul de la luminance spectrale énergétique par la loi de Planck
def Luminance(T,nu):
    L = (2.0*h*power(nu*1e9,3.0)/(c*c))/(exp((h*nu*1e9)/(kb*T))-1.0)
    return L
    
# Choix de la température de rayonnement en Kelvin
T = 2.7

# Creation de la figure
fig, axes = plt.subplots(figsize=(15,10))
plt.subplots_adjust(left=0.25, bottom=0.25)

# Nombre de points
nbp=10000

# Limites en GHz
MinNu=10.0
MaxNu=1000.0

# Creation de l'axe des abscisses
nu = linspace(MinNu,MaxNu,nbp)

# Calcul de la courbe L = f(T,nu)
L = Luminance(T,nu)

# Tracé de la fonction de Planck en fonction de nu.
plt.plot(nu,L, lw=2, color='blue',visible=True)

# Titre de la figure
plt.title('Luminance spectrale energetique pour T = 2.7K ')

# Paramétrage du systèmed 'axes
plt.ylim(0.0,1.1*max(L))
plt.xlim(MinNu,MaxNu)
plt.xlabel(r"$\nu$ [$\mathrm{GHz}$]",fontsize=15)
plt.ylabel(r"$B_\nu$ [$\mathrm{W.m^{-2}.Hz^{-1}.sr^{-1}}$]"+"\n",fontsize=15)
for tick in axes.xaxis.get_major_ticks():tick.label.set_fontsize(10) 
for tick in axes.yaxis.get_major_ticks():tick.label.set_fontsize(10)
axes.xaxis.set_major_locator(mtk.MaxNLocator(20))
plt.grid(True,which='both')