# -*- coding: utf-8 -*-

# programme de calcul d'un histogramme d'une distribution
# de mesures avec des erreurs aléatoires
# Dominique Lefebvre
# TangenteX.com
# 6 octobre 2016

# importation des librairies
from scipy import sqrt, pi, exp, mean, std, arange, random
import matplotlib.pyplot as plt


# Définition des fonctions statistiques
def Gaussienne(x,moyenne,ecarttype):
    return 1/(ecarttype*sqrt(2*pi))*exp(-(x-moyenne)**2/(2*ecarttype**2))
    
def Ecart_Type(liste):
    n = len(liste)
    ecart = 0
    mu = mean(liste)
    for i in range(n):
        ecart = ecart + (liste[i] - mu)**2
    ecart = sqrt(ecart/(n-1))
    return ecart
    

# Définition des paramètres
NomFichier = 'MESURES1.CSV'

# ------------------------------------------------------------------------
# Début du programme
# ------------------------------------------------------------------------
   
# Création d'une liste de mesures avec des erreurs aléatoires
# contruite autour de la valeur de référence de la tension
U = 3.992           # tension de référence
NbMesures = 1000
ListeMesures = []
for i in range(NbMesures):
    ListeMesures.append(random.normal(U,0.002))


# Calcul des paramètres de la liste
NbMesures = len(ListeMesures)
MinListe = min(ListeMesures)
MaxListe = max(ListeMesures)
Moyenne = mean(ListeMesures)
EcartType = std(ListeMesures) 

# Affichage des paramètres statistiques
print "Expression du résultat : ", Moyenne, " +- ", EcartType



# Définition des classes de l'histogramme
NbClasses = 10
ClasseRange  = 0.002

# Affichage de l'histogramme
fig = plt.figure()
plt.hist(ListeMesures, NbClasses, facecolor='green')

# Tracé de la gaussienne théorique avec les paramètres de la distribution
x = arange(MinListe,MaxListe,0.0001)
y = Gaussienne(x,Moyenne,EcartType)
plt.plot(x,y,'blue')

# Affichage de l'histogramme de distribution des mesures
plt.xlabel('Tension')
plt.ylabel(u'Nb mesures') # string en unicode
plt.xticks(arange(MinListe, MaxListe, ClasseRange))
plt.grid(True)

plt.show()