import numpy as np

def normcrosscorr(a, v):
    # return the correlation of two decorrelated signal, x and y,
    # by computing the normalized cross-correlation and obtaining the maximun value
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    v = (v - np.mean(v)) /  np.std(v)
    # y = np.correlate(a,v, "same") moving
    y = np.correlate(a,v) # no moving
    omega = y[abs(y).argmax()]
    return omega
