# -*- coding: utf-8 -*-

# programme de calcul d'une distribution de mesures
# Dominique Lefebvre
# TangenteX.com
# 5 octobre 2016

# importation des librairies
import csv
from scipy import sqrt, pi, exp, mean, std, arange
import matplotlib.pyplot as plt


# Fonction de chargement des mesures contenues dans le fichier csv
# dans une liste (ouverture du fichier en mode universal-newline)
def ChargementListe(NomFic):
    liste = []
    Fic1 = open(NomFic,'rU')
    Fic1CSV = csv.reader(Fic1, delimiter = ';')
    for row in Fic1CSV:
        if row :
          mesure = float(row[1])
          liste.append(mesure)
    Fic1.close()
    return liste


# Définition des fonctions statistiques
def Gaussienne(x,moyenne,ecarttype):
    return 1/(ecarttype*sqrt(2*pi))*exp(-(x-moyenne)**2/(2*ecarttype**2))
    

# Définition des paramètres
NomFichier = 'MESURES1.CSV'

# ------------------------------------------------------------------------
# Début du programme
# ------------------------------------------------------------------------

# Chargement du fichier de mesures dans une liste
ListeMesures = ChargementListe(NomFichier)
NbMesures = len(ListeMesures)
MinListe = min(ListeMesures)
MaxListe = max(ListeMesures)

# Affichage des paramètres statistiques
print "Moyenne de l'échantillon : ",mean(ListeMesures)
print "Ecart type de l'échantillon : ",std(ListeMesures)
print "Minimum : ",MinListe, " Maximum : ", MaxListe

# Définition des classes de l'histogramme
NbClasses = 8
ClasseRange  = 0.005

# Affichage de l'histogramme
fig = plt.figure()
plt.hist(ListeMesures, NbClasses, facecolor='green')

# Tracé de la gaussienne théorique avec les paramètres de la distribution
x = arange(MinListe,MaxListe,0.001)
y = Gaussienne(x,mean(ListeMesures),std(ListeMesures))
plt.plot(x,y,'blue')

# Affichage de l'histogramme de distribution des mesures
plt.xlabel('Tension')
plt.ylabel(u'Nb mesures') # string en unicode
plt.xticks(arange(MinListe, MaxListe, ClasseRange))
plt.grid(True)

plt.show()