# -*- coding: Latin-1 -*-
# programme de simulation d'un syst�me d'acquisition
# Dominique Lefebvre pour TangenteX.com
# 23 f�vrier 2017

# importation des librairies
import numpy as np
from threading import Thread
from Queue import Queue
import time
import random

# D�finition des param�tres de la simulation
PeriodeAcquisition = 5.0      # p�riode d'acquisition (secondes)
NbAcq = 10                    # nombre d'acquisitions
nbcapteurs = 10               # nombre de capteurs

# d�finition de la classe Mesure
class Mesure(object):
    def __init__(self):
        self.CapteurId  = None
        self.CapteurNum = None
        self.Valeur     = None
        self.Unit       = None

# d�finition de la classe BDTR
class BDTR(object):
    def __init__(self):
        self.AcqNum = None
        self.Tableau = np.zeros(nbcapteurs)
        self.Unit = None

# d�finition de la routine de traitement de chaque thread
def SimuCapteur(i,queue, periode):
    TInit  = 20.0  
    while True:       
        # cr�ation d'une nouvelle mesure
        mesure = Mesure()
        mesure.CapteurId = 'Capteur%d' % i
        mesure.CapteurNum = i
        mesure.Valeur = TInit*(1 + random.random()/2.)
        mesure.Unit = "�C"            
        # �criture de la mesure dans l'unit� d'acquisition
        queue.put(mesure)
        queue.task_done()
        # attendre t secondes pour la prochaine mesure
        time.sleep(periode)

 
# Cr�ation d'une pile FIFO de taille ind�finie
pileAcq = Queue(maxsize=0)

# cr�ation et activation des capteurs
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
    print 'Acquisition n�%2d' % AcqNum  
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

# Impression des donn�es acquises dans BD
# item.Tableau[0], item.Tableau[1]
for item in BD:
    print ('Acq:%2d %s %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f' % (item.AcqNum, item.Unit, \
           item.Tableau[0], item.Tableau[1],item.Tableau[2],item.Tableau[3],\
           item.Tableau[4], item.Tableau[5],item.Tableau[6],item.Tableau[7],\
           item.Tableau[8], item.Tableau[9]))
    
    
