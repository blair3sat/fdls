#%%
import data

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
plt.title("Linear frequency response (Amplitude vs Frequency)")
plt.plot(data.frequency, data.amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

#%%
import data
import fdls
coeffs = fdls.fdls(data.frequency, data.amplitude, data.phase, fs=1000)

# print(coeffs.shape)
