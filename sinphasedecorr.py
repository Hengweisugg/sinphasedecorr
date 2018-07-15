# create 2ch decorrelated signal by sinusoidal phase all-pass pair
# based on Zotter et al. (2011) PHANTOM SOURCE WIDENING WITH DETERMINISTIC FREQUENCY DEPENDENT TIME DELAYS
# and Zotter et al. (2013) Efficient Phantom Source Widening
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import soundfile as sf
import corr

# assign phase modulation depth and period
phi = 0.6            # [0.3, 0.6, 0.6, 0.9] conditions from the research of Zotter
T = 2.5 / 1000       # [5.0, 2.5, 5.0, 1.7] conditions from the research of Zotter

# read signal file
signal, fs1 = sf.read('Cello.wav')

# create impulse for compute ICCC of IR
impulse = np.zeros(100)
impulse[0] = 1

# transfer function in frequency domain
N = len(signal)
f = np.linspace(1, fs1/2, N//2)
omega = 2 * np.pi * f

Hl = np.zeros(N, dtype='complex')
Hr = np.zeros(N, dtype='complex')
Hl[:N//2] = 1 / np.sqrt(2) * np.exp(1j*phi*np.sin(omega*T))
Hr[:N//2] = 1 / np.sqrt(2) * np.exp(-1j*phi*np.sin(omega*T))

Hl[-N//2:] = np.flipud(np.conjugate(Hl[:N//2]))
Hr[-N//2:] = np.flipud(np.conjugate(Hr[:N//2]))

# plot magnitude and phase response
plt.figure(1)
plt.plot(abs(Hl))
plt.plot(np.angle(Hl))

plt.figure(2)
plt.plot(abs(Hr))
plt.plot(np.angle(Hr))
plt.show()

# fft convolution to generate decorrelated signal pair
lsignal = np.real(ifft(Hl*fft(signal)))
rsignal = np.real(ifft(Hr*fft(signal)))

print("ICCC of signal input = ", corr.normcrosscorr(lsignal, rsignal))

# impulse response
IRL = np.real(ifft(Hl*fft(impulse, N)))
IRR = np.real(ifft(Hr*fft(impulse, N)))
print("ICCC of Impulse Response = ", corr.normcrosscorr(IRL, IRR))

# generate wav files
if np.max(lsignal) > 1 :
    raise Warning('output signal value exceed 1, writting wave file could clip')
sf.write('lsignal.wav', lsignal, fs1)

if np.max(rsignal) > 1 :
    raise Warning('output signal value exceed 1, writting wave file could clip')
sf.write('rsignal.wav', rsignal, fs1)
