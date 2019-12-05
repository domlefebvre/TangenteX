# -*- coding: Latin-1 -*-
# trac� du spectrogramme d'un signal audio r�el
# tir� d'un fichier .wav
# Dominique Lefebvre pour TangenteX.com
# 10 mai 2017
#

# importation des librairies
from numpy import log, sum, zeros
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# param�tres
FreqBas  = 0.0         # fr�quence de coupure basse en Hz
FreqHaut = 800.0       # fr�quence de coupure haute en Hz
tz = 0.5               # dur�e d'un �chantillon �l�mentaire du spectrogramme

# lecture du fichier son 8 Khz mono
rate,signal = read('L3 Violoncelle.wav')

# d�finition de la taille d'un �chantillon �l�mentaire du spectrogramme
NbEch = int(rate*tz)

# d�finition du domaine fr�quentiel du spectrogramme
dt = 1.0/rate
freq = fftfreq(NbEch,dt)
domaine = (freq > FreqBas) * (freq < FreqHaut)

# d�finition de la matrice de construction du spectrogramme
n = int(signal.shape[0]/NbEch)       # nombre d'�chantillons �l�mentaires
fr = sum(1*domaine)               # domaine de fr�quence
spectro = zeros((n,fr))

# d�finition de la fen�tre de traitement pour FFT, de la taille d'un
# �chantillon �l�mentaire
# window = signal.blackman(len(signal[:N]))

# boucle de calcul du spectrogramme
for i in range(0,n):
    signalElem = signal[(NbEch*i):(NbEch*(i+1))]
    FFT = fft(signalElem)
    spectro[i,:] = log(abs(FFT[domaine]))

# affichage du signal
fig,ax = plt.subplots(1,1,figsize=(10,8))
p = ax.imshow(spectro,origin='lower',extent=(FreqBas,FreqHaut,0,n),
              aspect='auto',cmap='RdBu_r')
cb = fig.colorbar(p,ax=ax)
plt.title('Spectrogramme du signal')
ax.set_xlabel('Frequence (Hz)')
ax.set_ylabel('Temps (s)')
cb.set_label("log|F|")

plt.tight_layout()
plt.show()

