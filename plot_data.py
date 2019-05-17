#%%
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


#%%
import data
plt.figure(1)
plt.title("Linear frequency response (Amplitude vs Frequency)")
plt.plot(data.frequency, data.amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.show()

#%%
import fdls

import scipy.signal
import numpy as np

b, a = fdls.fdls(data.frequency, data.amplitude, data.phase, fs=1000)

w, h = scipy.signal.freqz(b, a)

#%%
# y = 20*np.log10(np.abs(h))

# dc = np.average(y)
plt.figure(2)
plt.title('Digital filter frequency response')

plt.plot(w, h)
# plt.plot(w, np.full(w.shape, dc))

plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency (Hz)')
plt.grid()


#%%
import signal, sys

# Must register singal handler before showing plot, enters TKAgg event loop
def handler(signum, frame):
    print('Quitting')
    try:
        plt.close()
    finally:
        sys.exit(0)

signal.signal(signal.SIGINT, handler)


plt.show()

# print(coeffs.shape)


#%%

