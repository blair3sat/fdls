# FDLS Filter Design Algorithm

The FDLS (frequency-domain least squares) algorithm
converts discrete arrays of desired frequency, amplitude, and phase samples,
along with a desired group delay,
to the optimal numerator and denominator coefficients of a 
IIR transfer function or difference function.
To do this, it computes the desired output values in Y,
the sequences of inputs and outputs (u and y) for N and D 
time samples away in X, and then computes the pseudoinverse
of this linear system of equations to find theta, the coefficients
of b and a.

### Example usage
```python
import fdls
import data
import scipy
b, a = fdls.fdls(data.frequency, data.amplitude, data.phase, group_delay=data.delay, n=2, d=2, fs=1000)

w, h = scipy.signal.freqz(b, a)
```
Plot `w` (frequencies) against `h` (amplitudes) to see the
continuous version of the filter based on coefficients `a` and `b`.
a and b are taps that you can export to any filter chip
or block in GNURadio.
