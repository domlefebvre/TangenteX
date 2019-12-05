# -*- coding: utf-8 -*-
# programme AnalSpectrale05
# tracé du spectre d'un signal réel tiré d'un fichier .wav
# avec fenetrage de Hann
# Dominique Lefebvre pour TangenteX.com
# 29 décembre 2014
#

# importation des librairies
from numpy import linspace, mean, log10
from scipy.fftpack import fft, fftfreq
from scipy.signal import hanning
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# nom du fichier à étudier
nomfile = 'L3 Violoncelle.wav'

# lecture du fichier son 8 Khz mono
rate,signal = read(nomfile)

# définition du vecteur temps
dt = 1./rate
FFT_size = 2**18
NbEch = signal.shape[0]

t = linspace(0,(NbEch-1)*dt,NbEch)
t = t[0:FFT_size]

# application de la fenetre de Hann
signal = signal*hanning(NbEch)

# calcul de la TFD par l'algo de FFT
signal = signal[0:FFT_size]
signal = signal - mean(signal) # soustraction de la valeur moyenne du signal
                               # la fréquence nulle ne nous intéresse pas 
signal_FFT = abs(fft(signal))  # on ne récupère que les composantes réelles


# récupération du domaine fréquentiel en passant la période d'échantillonnage
signal_freq = fftfreq(signal.size, dt)

# extraction des valeurs réelles de la FFT et du domaine fréquentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

# conversion en dB du spectre
spectredB = 20*log10(signal_FFT)

#affichage du signal
plt.subplot(211)
plt.title('Signal reel et son spectre')
plt.plot(t,signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

#affichage du spectre du signal
plt.subplot(212)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude en dB')
Fmin = 0
Fmax = 2000

plt.xlim(Fmin,Fmax)
plt.ylim(spectredB.min(), spectredB.max())
plt.plot(signal_freq,spectredB)

plt.show()
