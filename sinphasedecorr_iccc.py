# for adjust parameter to obtain desired ICCC
# based on Zotter et al. (2011) PHANTOM SOURCE WIDENING WITH DETERMINISTIC FREQUENCY DEPENDENT TIME DELAYS
# and Zotter et al. (2013) Efficient Phantom Source Widening
import numpy as np
from scipy.fftpack import fft, ifft
import corr

# assign phase modulation depth and period
phi = 0.82            # [0.3, 0.6, 0.6, 0.9] conditions from the research of Zotter
T = 5.0 / 1000       # [5.0, 2.5, 5.0, 1.7] conditions from the research of Zotter

# create impulse for compute ICCC of IR
impulse = np.zeros(44100)
impulse[0] = 1

# transfer function in frequency domain
N = 44100
f = np.linspace(1, 44100/2, N//2)
omega = 2 * np.pi * f

Hl = np.zeros(N, dtype='complex')
Hr = np.zeros(N, dtype='complex')
Hl[:N//2] = 1 / np.sqrt(2) * np.exp(1j*phi*np.sin(omega*T))
Hr[:N//2] = 1 / np.sqrt(2) * np.exp(-1j*phi*np.sin(omega*T))

Hl[-N//2:] = np.flipud(np.conjugate(Hl[:N//2]))
Hr[-N//2:] = np.flipud(np.conjugate(Hr[:N//2]))

# impulse response
IRL = np.real(ifft(Hl*fft(impulse, N)))
IRR = np.real(ifft(Hr*fft(impulse, N)))
print("ICCC of Impulse Response = ", corr.normcrosscorr(IRL, IRR))
