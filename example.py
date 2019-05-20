# %%

import scipy.signal
import signal
import sys

import data
import fdls

import matplotlib

gui_env = ['TKAgg', 'GTKAgg', 'Qt4Agg', 'WXAgg']
for gui in gui_env:
    try:
        print("Testing backend: ", gui)
        matplotlib.use(gui, warn=False, force=True)
        from matplotlib import pyplot as plt

        break
    except:
        continue
print("Using:", matplotlib.get_backend())

# %%

plt.figure(1)
plt.title("Discretized linear frequency response")
plt.plot(data.frequency, data.amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
# plt.show()

# %%

b, a = fdls.fdls(data.frequency, data.amplitude, data.phase, fs=1000)

w, h = scipy.signal.freqz(b, a)

# %%
plt.figure(2)
plt.title('Continuous digital filter frequency response')

plt.plot(w, h)

plt.ylabel('Amplitude')
plt.xlabel('Frequency (Hz)')
plt.grid()

# %%
# Must register singal handler before showing plot, enters TKAgg event loop
def handler(signum, frame):
    print('Quitting')
    try:
        plt.close()
    finally:
        sys.exit(0)


signal.signal(signal.SIGINT, handler)

plt.show()
