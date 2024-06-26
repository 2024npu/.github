import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler

output_dir = 'output_data'
os.makedirs(output_dir, exist_ok=True)

def read_data(filename):
    x = pickle._Unpickler(open(filename, 'rb'))
    x.encoding = 'latin1'
    data = x.load()
    return data

labels = []
data = []

fileph = ".\output_data/data_n0_i0.dat"
d = read_data(fileph)
labels.append(d['label'])
data.append(d['data'])

print(d['label'])
print(data)

import numpy as np
import pywt
import matplotlib.pyplot as plt

# Generate a sample pulse signal
np.random.seed(0)
signal = 2+np.sin(np.linspace(0, 4 * np.pi, 512)) + 0.5 * np.random.randn(512)

# Step 1: Smooth the signal using a moving average filter
def moving_average(signal, window_size=5):
    cumsum_vec = np.cumsum(np.insert(signal, 0, 0)) 
    ma_signal = (cumsum_vec[window_size:] - cumsum_vec[:-window_size]) / window_size
    return ma_signal

smoothed_signal = moving_average(signal, window_size=5)

# Step 2: Remove baseline using wavelet transform
def remove_baseline(signal, wavelet='db4', level=1):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    coeffs[0] = np.zeros_like(coeffs[0])  # Set approximation coefficients to zero
    baseline_removed_signal = pywt.waverec(coeffs, wavelet)
    return baseline_removed_signal

baseline_removed_signal = remove_baseline(smoothed_signal, wavelet='db4', level=1)

# Step 3: Downsample the signal to 128 points
downsampled_signal = baseline_removed_signal[::4]

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(signal, label='Original Signal')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(smoothed_signal, label='Smoothed Signal')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(downsampled_signal, label='Baseline Removed & Downsampled Signal')
plt.legend()

plt.tight_layout()
plt.show()
