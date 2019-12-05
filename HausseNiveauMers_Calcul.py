# -*- coding: Latin-1 -*-
# Programme de calcul de la dilatation des mers par réchauffement climatique
# Dominique Lefebvre pour TangenteX.com
# 8 août 2017
#

# importation des librairies
from scipy import interpolate, array, arange, integrate

# Table de variation de la température (°C) de l'eau en fonction de la profondeur
xTemp = array([0.0,100.0,200.0,300.0,400.0,500.0,600.0,700.0,800.0,900.0,
               1000.0,1250.0,1500.0,2000.0,2500.0,3000.0,4000.0,5000.0])
yTemp = array([22.0,22.0,21.8,21.2,18.0,13.5,10.5,8.3,7.0,6.0,5.5,4.8,4.4,
               4.0,3.7,3.5,3.2,2.9])

# Table de variation du coeff de dilatation thermique (°C^-1) en fonction de la 
# température (°C)
xCDT = array([0.0,2.0,4.0,6.0,10.0,20.0,40.0,60.0,80.0,100.0])
yCDT = array([-0.5e-04,-0.5e-04,0.15e-04,0.15e-04,0.6e-04,1.5e-04,3.01e-04,
              4.56e-04,5.84e-04,6.82e-04])

# paramètres de modélisation
# je choisis la profondeur d'eau qui est en équilibre thermique avec l'atmosphère
# et l'élévation de température max dans le meilleur des scénarii de RC
hColonne = 1000.0 # profondeur en mètres
dh = 1.0          # épaisseur d'une tranche horizontale de la colonne en mètres
dT = 0.6          # variation de température en °C


# Calcul des fonctions d'interpolation (spline cubique) sur les différentes tables
fTemp = interpolate.interp1d(xTemp,yTemp,kind='linear')
fCDT  = interpolate.interp1d(xCDT,yCDT,kind='linear')


# calcul de la hausse du niveau de la mer
h = arange(0.0,hColonne,dh)
zh = []
for i in h:
    # chercher la température en fonction de la profondeur
    Ti = fTemp(i)
    # chercher le CDT en fonction de la température
    CDTi = fCDT(Ti)
    # calculer la variation verticale de la tranche i
    dz = CDTi*dT
    zh.append(dz)

# intégration des hausses unitaires   
hausseTotale = integrate.simps(zh,x=h)
print 'Hausse du niveau de la mer: ',hausseTotale,' m'


