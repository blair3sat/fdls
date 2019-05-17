# %% FDLS Filter Design Algorithm
# Uses pseudoinverse to calculate filter coefficients

import numpy as np

khz = 1000

# %%

def fdls(frequency, amplitude, phase, n=2, d=2, fs=44 * khz):
    """

    :param frequency: Numpy array of frequency points
    :param amplitude: Numpy array of amplitude points
    :param phase: Numpy array of phase points
    :param n: Number of coefficients in numerator
    :param d: Number of coefficients in denominator
    :param fs: Sample rate
    :return: coefficients of transfer function and
    difference function representation of an IIR filter
     (accesses both current and past inputs and outputs

    The FDLS (frequency-domain least squares) algorithm
    implements the pseudoinverse of a matrix of desired
    frequency samples to find transfer function and thus
    difference function coefficients
    """
    if not type(frequency) == type(amplitude) == type(phase) == np.ndarray:
        raise TypeError("Input parameter arrays are of wrong type: must be numpy array")
    if not amplitude.shape == frequency.shape == phase.shape:
        raise Exception("Shape of numpy arrays does not match")
    # if not amplitude.ndim == frequency.ndim == phase.ndim == 2:
    #     raise Exception("Invalid numpy array dimensions")

    frequency = frequency.reshape((-1, 1))
    amplitude = amplitude.reshape((-1, 1))
    phase = phase.reshape((-1, 1))

    w = 2 * np.pi * frequency
    w_scaled = w / fs

    y = amplitude * np.cos(phase) # good

    alpha = w_scaled

    ySpreadArray = np.arange(-1, -(d + 1), -1)
    uSpreadArray = np.arange(0, -(n + 1), -1)

    print(ySpreadArray, uSpreadArray)

    yX = -amplitude * np.cos(ySpreadArray * alpha + phase)
    uX = np.cos(uSpreadArray * alpha)

    x = np.concatenate((yX, uX), axis=1)

    x_pinv = np.linalg.pinv(x)
    theta = x_pinv.dot(y)

    t = theta.ravel()
    print(t)
    a = np.append([1], t[:d])
    b = t[d:]

    return (b, a)

# # %%
# import data
#
# # a = data.amplitude
# (b, a) = fdls(data.frequency, data.amplitude, data.phase, fs=khz)
#
# #%%
# import sys
# sys.modules[__name__].__dict__.clear()
