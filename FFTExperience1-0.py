# programme d'experimentation FFT FFTExperience1-0
# Dominique Lefebvre pour TangenteX.com
# 12 aout 2014
#

# importation des librairies
from numpy import pi, sin, linspace, log10
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt       

# d�finition des constantes du signal
K = 2*pi       # facteur conversion p�riode/fr�quence
A0 = 4         # amplitude fr�quence fondamentale
A1 = 8         # amplitude premi�re harmonique
f0 = 2         # fr�quence fondamentale (Hz)
f1 = 8         # fr�quence premi�re harmonique (Hz)

# d�finition temporelle du signal
t0 = 0         # d�but de l'acquisition du signal
t1 = 10        # fin de l'acquisition (s)

# d�finition des param�tres d'�chantillonnage
FreqEch = 1024                  # fr�quence d'�chantillonage
PerEch = 1./FreqEch             # p�riode d'�chantillonnage
N = FreqEch*(t1 - t0)           # nombre de points �chantillonn�s sur l'intervalle

# d�finition du temps
t = linspace(t0, t1, N)

# d�finition du signal
signal = A0*sin(f0*K*t) + A1*sin(f1*K*t)

# d�finition des donn�es de FFT
FenAcq = signal.size             # taille de la fenetre temporelle
    
# calcul de la TFD par l'algo de FFT
signal_FFT = abs(fft(signal))    # on ne r�cup�re que les composantes r�elles

# r�cup�ration du domaine fr�quentiel
signal_freq = fftfreq(FenAcq,PerEch)

# extraction des valeurs r�elles de la FFT et du domaine fr�quentiel
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

#affichage du signal
plt.subplot(211)
plt.title('Signal et son spectre')
plt.ylim(-(A1+5), A1+5)
plt.plot(t, signal)
plt.xlabel('Temps (s)'); plt.ylabel('Amplitude')

#affichage du spectre du signal
plt.subplot(212)
plt.xlim(0,f1+5)
plt.plot(signal_freq,signal_FFT)
plt.xlabel('Frequence (Hz)'); plt.ylabel('Amplitude')
#plt.title('Signal et son spectre')
plt.show()
