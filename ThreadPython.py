# -*- coding: Latin-1 -*-
# programme de simulation d'un système d'acquisition
# Dominique Lefebvre pour TangenteX.com
# 23 février 2017

# importation des librairies
import numpy as np
from threading import Thread
from Queue import Queue
import time
import random

# Définition des paramètres de la simulation
PeriodeAcquisition = 5.0      # période d'acquisition (secondes)
NbAcq = 10                    # nombre d'acquisitions
nbcapteurs = 10               # nombre de capteurs

# définition de la classe Mesure
class Mesure(object):
    def __init__(self):
        self.CapteurId  = None
        self.CapteurNum = None
        self.Valeur     = None
        self.Unit       = None

# définition de la classe BDTR
class BDTR(object):
    def __init__(self):
        self.AcqNum = None
        self.Tableau = np.zeros(nbcapteurs)
        self.Unit = None

# définition de la routine de traitement de chaque thread
def SimuCapteur(i,queue, periode):
    TInit  = 20.0  
    while True:       
        # création d'une nouvelle mesure
        mesure = Mesure()
        mesure.CapteurId = 'Capteur%d' % i
        mesure.CapteurNum = i
        mesure.Valeur = TInit*(1 + random.random()/2.)
        mesure.Unit = "°C"            
        # écriture de la mesure dans l'unité d'acquisition
        queue.put(mesure)
        queue.task_done()
        # attendre t secondes pour la prochaine mesure
        time.sleep(periode)

 
# Création d'une pile FIFO de taille indéfinie
pileAcq = Queue(maxsize=0)

# création et activation des capteurs
capteurs = []
for i in xrange(0,nbcapteurs):
    capteur = Thread(target=SimuCapteur, args=(i,pileAcq,PeriodeAcquisition))
    capteurs.append(capteur)
    capteurs[-1].setDaemon(True)
    capteurs[-1].start()    

# process d'acquisition
AcqNum = 1
BD = []       # liste des acquisitions
while AcqNum <= NbAcq:
    # lecture de la pile d'acquisition tant qu'elle n'est pas vide   
    print 'Acquisition n°%2d' % AcqNum  
    record = BDTR()
    while not pileAcq.empty():               
        mesure = Mesure()                        
        mesure = pileAcq.get()
        record.AcqNum = AcqNum
        record.Tableau[mesure.CapteurNum] = mesure.Valeur
        record.Unit = mesure.Unit              
    # ajout sur la liste BD
    BD.append(record)    
    AcqNum += 1
    # attente de la prochaine acquisition
    time.sleep(PeriodeAcquisition)

# Impression des données acquises dans BD
# item.Tableau[0], item.Tableau[1]
for item in BD:
    print ('Acq:%2d %s %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f' % (item.AcqNum, item.Unit, \
           item.Tableau[0], item.Tableau[1],item.Tableau[2],item.Tableau[3],\
           item.Tableau[4], item.Tableau[5],item.Tableau[6],item.Tableau[7],\
           item.Tableau[8], item.Tableau[9]))
    
    
