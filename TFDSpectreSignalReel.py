# -*- coding: utf-8 -*-
# Programme de calcul de la TFD d'un signal reel par FFT
# Dominique Lefebvre pour TangenteX.com
# 10 avril 2016

# importation des librairies
from scipy import arange,log10
from scipy.fftpack import fft, fftfreq
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# lecture du fichier contenant le signal fe est la fréquence
# d'échantillonnage fixée à l'enregistrement du signal (8 kHz ici)
Fe,signal = read('BruitWav1.wav')
N = signal.shape[0]    # nb de points dans l'échantillon
Te = 1.0/Fe            # période d'échantillonnage

# Restitution du signal physique (tension électrique) à partir de
# la série d'échantillons numérisés sur 16 bits signés, soit 2**15
FacteurQuantification = 1.0/2**15
signal = FacteurQuantification*signal

# construction du vecteur temps 
t = arange(0.0,N,1.0)*Te

# boucle de calcul de la TFD
N = 32768
Xc = fft(signal,N)

# calcul du spectre normalisé sur la partie positive du buffer FFT
FacteurNorm = 2.0/N
SP = FacteurNorm*abs(Xc[1:N/2])

# construction du vecteur fréquence
f = fftfreq(N,Te)[1:N/2]

# affichage des résultats
fig = plt.figure(figsize=(14,8))

# Affichage du signal
plt.subplot(211)
plt.grid()
plt.title('Signal reel et son spectre')
plt.plot(t,signal)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude (V)')


#affichage du spectre du signal
plt.subplot(212)
plt.grid()
plt.plot(f,20*log10(SP/SP.max()))
plt.xlabel('Frequence (Hz)')
plt.ylabel('Amplitude (dB)')

plt.show()


