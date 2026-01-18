import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt


# --------------------------------------------------
# Function to create and apply a low-pass Butterworth filter
# --------------------------------------------------
def butter_lowpass_filter(data, cutoff, fs, order=4):
    # Nyquist frequency = half of sampling rate
    nyquist = 0.5 * fs
    
    # Normalize cutoff frequency (must be between 0 and 1)
    normal_cutoff = cutoff / nyquist
    
    # Design Butterworth low-pass filter
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    
    # Apply filter forward and backward to avoid phase shift
    y = filtfilt(b, a, data)
    
    return y


# --------------------------------------------------
# STEP 1: Generate synthetic noisy well-log data
# --------------------------------------------------
np.random.seed(42)  # Ensures reproducible results

# Depth range from 1000m to 3000m
depths = np.linspace(1000, 3000, 500)

# True pressure signal with smooth periodic variations
true_pressure = 4000 + 50 * np.sin(depths / 300)

# Add Gaussian noise to simulate sensor noise
noise = np.random.normal(0, 50, size=depths.shape)

# Noisy pressure data
noisy_pressure = true_pressure + noise


# --------------------------------------------------
# STEP 2: Filter parameters
# --------------------------------------------------
cutoff_frequency = 0.01  # Cutoff frequency for low-pass filter

# Sampling rate based on depth spacing
sampling_rate = 1 / (depths[1] - depths[0])


# --------------------------------------------------
# STEP 3: Apply low-pass Butterworth filter
# --------------------------------------------------
smoothed_pressure = butter_lowpass_filter(
    noisy_pressure,
    cutoff_frequency,
    sampling_rate
)


# --------------------------------------------------
# STEP 4: Plot original vs filtered data
# --------------------------------------------------
plt.figure(figsize=(10, 6))

# Plot noisy pressure data
plt.plot(
    depths,
    noisy_pressure,
    label='Noisy Pressure Data',
    color='red',
    alpha=0.5
)

# Plot filtered (smoothed) pressure data
plt.plot(
    depths,
    smoothed_pressure,
    label='Filtered Pressure Data (Low-Pass)',
    color='blue',
    linewidth=2
)

# Plot formatting
plt.title('Low-Pass Filtering of Noisy Well Log Pressure Data')
plt.xlabel('Depth (m)')
plt.ylabel('Pressure (psi)')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
