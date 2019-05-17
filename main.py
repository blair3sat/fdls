#%% Filter Design in Scipy

import numpy as np
import scipy.signal as signal

# Matplotlib import
import matplotlib
gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        print("Testing backend: ", gui)
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
print("Using:", matplotlib.get_backend())

# import matplotlib.pyplot as plt
# from pylab import *

#%%
samp_rate = 44000 # Hz

cutoff = 5000 # Hz

type = 'cheby1'
ripple_passband = 10
ripple_stopband = 0.5

N, Wn = signal.buttord(1000, 1200, 0.5, 5, fs=samp_rate)
print(N, Wn)

b, a = signal.iirfilter(N, Wn, rp=ripple_passband, rs=ripple_stopband, btype='lowpass', ftype=type, fs=samp_rate)

w, h = signal.freqz(b, a, fs=samp_rate)

y = 20*np.log10(np.abs(h))

dc = np.average(y)

plt.title(f'Digital filter frequency response: {type}, Cutoff: {cutoff}, PB: {ripple_passband}, SB: {ripple_stopband}')

plt.plot(w, y)
plt.plot(w, np.full(w.shape, dc))

plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency (Hz)')
plt.grid()
plt.show()
