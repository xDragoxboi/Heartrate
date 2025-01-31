import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt

# Load data
data = pd.read_csv('Raw Data.csv') 
time = data['Time (s)'].values
z_axis = data['Linear Acceleration z (m/s^2)'].values




# remove noise
def lowpass_filter(data, cutoff, sample_rate, order=2):
    nyquist = 0.15 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

# Sample rate (adjust based on your data)
sample_rate = 100  # Hz (common for Phyphox)

# Apply low-pass filter to smooth the signal
z_filtered = lowpass_filter(z_axis, cutoff=5, sample_rate=sample_rate)

# Dynamic threshold (e.g. 24% of the max amplitude)
threshold = 0.24 * np.max(z_filtered)

# Find peaks with a refractory period , peroid best kept between 0.28s-0.4s
peaks, _ = find_peaks(z_filtered, height=threshold, distance=int(0.4 * sample_rate))


intervals = np.diff(time[peaks])
#Final calculation 
bpm = 60 / np.mean(intervals)

print(f"Average Heart Rate: {bpm:.2f} BPM")





plt.figure(figsize=(16, 6))
plt.plot(time, z_axis, label='Raw Data', alpha=0.5)
plt.plot(time, z_filtered, label='Filtered Data', linewidth=2)
plt.scatter(time[peaks], z_filtered[peaks], color='red', label='Detected Peaks')
plt.axhline(threshold, color='green', linestyle='--', label='Threshold')
plt.xlabel('Time (s)')
plt.ylabel('Linear Acceleration z (m/s²)')
plt.legend()
plt.title(f'Rate: {bpm:.2f} BPM')
plt.show()
