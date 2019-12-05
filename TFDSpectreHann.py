# -*- coding: utf-8 -*-
# Programme de calcul de la TFD d'un signal reel par FFT
# avec une fenêtre de Hann
# Dominique Lefebvre pour TangenteX.com
# 12 avril 2016

# importation des librairies
from scipy import arange
from scipy.fftpack import fft, fftfreq
from scipy.signal import hann,hamming, blackman
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import time

# lecture du fichier contenant le signal fe est la fréquence
# d'échantillonnage fixée à l'enregistrement du signal (8 kHz ici)
Fe,signal = read('BruitWav1.wav')
N = signal.shape[0]    # nb de points dans l'échantillon
Te = 1.0/Fe            # période d'échantillonnage

# construction du vecteur temps 
t = arange(0.0,N,1.0)*Te

# construction de la fenêtre de Hann
Win = blackman(N)

# boucle de calcul de la TFD
tdebut = time.time()
Xc = fft(signal*Win)
print 'Temps de calcul (s) : ',time.time() - tdebut

# calcul du spectre normalisé sur la partie positive du buffer FFT
FacteurNorm = 2.0/N
SP = FacteurNorm*abs(Xc[1:N/2])

# construction du vecteur fréquence
f = fftfreq(N,Te)[1:N/2]

# affichage des résultats
fig = plt.figure(figsize=(14,8))
#affichage du spectre du signal
plt.subplot(211)
plt.grid()
plt.plot(f,SP)
plt.xlabel('Frequence (Hz)')
plt.ylabel('Amplitude')

plt.show()


