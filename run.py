import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, butter, filtfilt

# Load Data
data = pd.read_csv('Raw Data.csv') 
time = data['Time (s)'].values
z_axis = data['Linear Acceleration z (m/s^2)'].values


#is it lupus

# remove noise
def lowpass_filter(data, cutoff, sample_rate, order=2):
    nyquist = 0.15 * sample_rate
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

# Sample rate (adjust based on your data , no change if your data is from phyphox)
sample_rate = 100  # Hz 

# Apply low-pass filter to smooth the signal
z_filtered = lowpass_filter(z_axis, cutoff=5, sample_rate=sample_rate)

# Dynamic threshold (e.g. 26% of the max amplitude)
threshold = 0.26 * np.max(z_filtered)

# Find peaks with a refractory period , peroid best kept between 0.22s-0.4s (assuming target doesn't have lupus)
# refactory peroid is tricky at the moment and may need change for different amplitudes, i can make this a bit more dynamic but i won't because i have no time uwu
peaks, _ = find_peaks(z_filtered, height=threshold, distance=int(0.3 * sample_rate))


intervals = np.diff(time[peaks])

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
