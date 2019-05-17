#%% FDLS Filter Design Algorithm
# Uses pseudoinverse to calculate filter coefficients

import numpy as np

khz = 1000

#%%
def fdls(frequency, amplitude, phase, N=2, D=2, fs=44*khz):
    if not type(frequency) == type(amplitude) == type(phase) == np.ndarray:
        raise TypeError("Input parameter arrays are of wrong type: must be numpy array")
    if not amplitude.shape == frequency.shape == phase.shape:
        raise Exception("Shape of numpy arrays does not match")
    if not amplitude.ndim == frequency.ndim == phase.ndim == 1:
        raise Exception("Invalid numpy array dimensions")

    w = 2*np.pi*frequency
    w_scaled = w / fs

    # print(w_scaled)

    alpha = w_scaled*frequency
    Y = np.cos(alpha)

    n = np.arange(1,N+1).reshape((-1, 1))
    d = np.arange(0,D+1).reshape((-1, 1))

    X_y = -amplitude * np.cos(-n * alpha + phase)
    X_u = amplitude * np.cos(-d * alpha + phase)
    # print(X_y.T)
    # print(X_y.shape)
    # print(X_u.T)
    # print(X_u.shape)
    X = np.concatenate((X_y, X_u))
    # print(X, X.shape)
    # print(Y.shape)
    X_pinv = np.linalg.pinv(X)
    # print("X")
    # print(X_pinv, X_pinv.shape)
    # print("Y")
    # print(Y)
    theta = X_pinv.T * Y
    return theta

#%%
import data
fdls(data.frequency, data.amplitude, data.phase, fs=khz)
