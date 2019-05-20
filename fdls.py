# %% FDLS Filter Design Algorithm
# Uses pseudoinverse to calculate filter coefficients

import numpy as np

khz = 1000


# %%

def fdls(frequency, amplitude, phase, n=2, d=2, group_delay=None, fs=44 * khz):
    """
    :param frequency: Numpy array of frequency points
    :param amplitude: Numpy array of amplitude points
    :param phase: Numpy array of phase points
    :param n: Number of coefficients in numerator
    :param d: Number of coefficients in denominator
    :param group_delay: Numpy array of delay samples by frequency
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
    # Check for array dimensions
    # if not amplitude.ndim == frequency.ndim == phase.ndim == 2:
    #     raise Exception("Invalid numpy array dimensions")

    # Make all of the  inputs into column vectors
    frequency = frequency.reshape((-1, 1))
    amplitude = amplitude.reshape((-1, 1))
    phase = phase.reshape((-1, 1))
    if (group_delay == None):
        group_delay = np.zeros(frequency.shape)
    group_delay = group_delay.reshape((-1, 1))

    # Calculate the basis frequencies
    w = 2 * np.pi * frequency
    w_scaled = w / fs

    # Calculate the expected output values
    y = amplitude * np.cos(phase)

    alpha = w_scaled

    # Generate the spread arrays for each order
    # in the filter coefficients.
    # This will take more samples in either direction
    ySpreadArray = np.arange(-1, -(d + 1), -1)
    uSpreadArray = np.arange(0, -(n + 1), -1)

    # Generate the X vector for both input (u) and output (y) values
    yX = -amplitude * np.cos(ySpreadArray * alpha + phase - group_delay * alpha)
    uX = np.cos(uSpreadArray * alpha)

    # Concatenate the X vector
    x = np.concatenate((yX, uX), axis=1)

    # Calculate the pseudoinverse of the X vector
    x_pinv = np.linalg.pinv(x)

    # Calculate the desired coefficients based on the pseudoinverse and the y vector
    theta = x_pinv.dot(y)

    # Make theta into a 1d vector
    t = theta.ravel()

    # Separate the output numerator coefficients (a) from the input denominator coefficients (b)
    a = np.append([1], t[:d])
    b = t[d:]

    return b, a
