# programme de tracé 2D en Python
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from pylab import *                # fonction de tracé de courbe

# définition du vecteur abscisse
x = arange(-pi, pi, pi/100)

# ouvre la fenêtre graphique standard
figure()

# définition du domaine de variation sur x et y
xlim(-pi,pi)
ylim(-1,1)

# tracé des courbes
plot(x,sin(x),'b-',label = 'sinus')     # en bleu trait continu
plot(x,cos(x),'r--', label = 'cosinus') # en rouge trait discontinu

# un titre ...
title('Sinus et cosinus')

# tracé des labels sur les axes
xlabel('abscisse')
ylabel('ordonnee')

# légende - je demande à Python de la placer au meilleur endroit en
# fonction du tracé
legend(loc = 'best')

# affiche les objets graphiques crées dans la fenêtre graphique
show()
