# 1. Successfully import matplotlib
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

# 2. FDLS example
import data
(b, a) = fdls.fdls(data.frequency, data.amplitude, data.phase, fs=khz)

# 3. Clear all local variables
import sys
sys.modules[__name__].__dict__.clear()

# 4. Handle SIGINT ^+C signals, remember to register singal handler
# before showing the plot, otherwise enters TKAgg event loop and is hard to interupt
import signal, sys

def handler(signum, frame):
    print('Quitting')
    try:
        plt.close()
    finally:
        sys.exit(0)

signal.signal(signal.SIGINT, handler)
