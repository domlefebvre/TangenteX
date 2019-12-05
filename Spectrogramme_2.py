# -*- coding: Latin-1 -*-
# programme d'�tude de l'effet de fen�trage sur un spectre r�el
# tir� d'un fichier .wav
# Dominique Lefebvre pour TangenteX.com
# 10 mai 2017
#

# importation des librairies
from numpy import linspace
from scipy.fftpack import fft, fftfreq
from scipy.signal import hamming
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# param�tres
FreqBas  = 210.0     # fr�quence de coupure basse en Hz
FreqHaut = 230.0     # fr�quence de coupure haute en Hz

# lecture du fichier son 8 Khz mono
rate,signal = read('L3 Violoncelle.wav')

# dur�e du signal
NbEch = signal.shape[0]
duree = NbEch/rate

# d�termination du domaine fr�quentiel � analyser
dt = 1./rate
freq = fftfreq(signal.size,dt)
t = linspace(0,(NbEch-1)*dt,NbEch)
domaine = (freq > FreqBas) * (freq < FreqHaut)

# transform�e de Fourier
FFT = fft(signal)

# d�finition de la fen�tre et nouveau calcul du spectre
window = hamming(len(signal))
FFT_fen = fft(signal*window)

# affichage du spectre sans fenetrage
fig = plt.figure(figsize=(10,8))
plt.subplot(211)
plt.plot(freq[domaine],abs(FFT[domaine]))
plt.title('sans fenetrage')
plt.xlabel('Frequence (Hz)'); plt.ylabel('|FFT|')

# affichage du spectre avec fenetrage
plt.subplot(212)
plt.plot(freq[domaine],abs(FFT_fen[domaine]))
plt.title('avec fenetrage')
plt.xlabel('Frequence (Hz)'); plt.ylabel('|FFT|')

plt.tight_layout()
plt.show()

