# programme de trac� 2D en Python
# Dominique Lefebvre pour TangenteX.com
# 3 mars 2014
#

# importation des librairies
from pylab import *                # fonction de trac� de courbe

# d�finition du vecteur abscisse
x = arange(-pi, pi, pi/100)

# ouvre la fen�tre graphique standard
figure()

# d�finition du domaine de variation sur x et y
xlim(-pi,pi)
ylim(-1,1)

# trac� des courbes
plot(x,sin(x),'b-',label = 'sinus')     # en bleu trait continu
plot(x,cos(x),'r--', label = 'cosinus') # en rouge trait discontinu

# un titre ...
title('Sinus et cosinus')

# trac� des labels sur les axes
xlabel('abscisse')
ylabel('ordonnee')

# l�gende - je demande � Python de la placer au meilleur endroit en
# fonction du trac�
legend(loc = 'best')

# affiche les objets graphiques cr�es dans la fen�tre graphique
show()
