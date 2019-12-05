# -*- coding: Latin-1 -*-
# programme d'�tude du spectre d'un signal r�el
# tir� d'un fichier .wav
# Dominique Lefebvre pour TangenteX.com
# 10 mai 2017
#

# importation des librairies
from numpy import linspace
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# param�tres
FreqBas  = 0.0         # fr�quence de coupure basse en Hz
FreqHaut = 800.0       # fr�quence de coupure haute en Hz

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

# affichage du signal
fig = plt.figure(figsize=(10,8))
plt.subplot(211)
plt.plot(t,signal)
plt.title('Signal')
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

# affichage du spectre du signal
plt.subplot(212)
plt.plot(freq[domaine],abs(FFT[domaine]))
plt.title('Spectre du signal')
plt.xlabel('Frequence (Hz)'); plt.ylabel('|FFT|')

plt.tight_layout()
plt.show()

