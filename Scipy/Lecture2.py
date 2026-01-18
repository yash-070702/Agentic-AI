import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.signal import butter, filtfilt


# -------------------------------------------------
# STEP 1: Create a time axis
# -------------------------------------------------
# Generate 100 equally spaced points between 0 and 10
t = np.linspace(0, 10, 100)


# -------------------------------------------------
# STEP 2: Create a clean sine signal
# -------------------------------------------------
# sin(t) gives a smooth periodic signal
signal = np.sin(t)


# -------------------------------------------------
# STEP 3: Add random noise to the signal
# -------------------------------------------------
# Noise is drawn from a normal (Gaussian) distribution
# mean = 0, standard deviation = 0.3
noise = np.random.normal(0, 0.3, size=len(t))

# Combine clean signal and noise
noisy_signal = signal + noise


# -------------------------------------------------
# STEP 4: Print noisy signal values (for observation)
# -------------------------------------------------
print(noisy_signal)


# -------------------------------------------------
# STEP 5: Plot the original (clean) sine signal
# -------------------------------------------------
plt.plot(t, signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Clean Sine Signal")
plt.show()


# -------------------------------------------------
# STEP 6: Plot the noisy sine signal
# -------------------------------------------------
plt.plot(t, noisy_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Noisy Sine Signal")
plt.show()


# -------------------------------------------------
# STEP 7: Smooth the signal using Savitzky–Golay filter
# -------------------------------------------------
# window_length = number of points used for smoothing (must be odd)
# polyorder = degree of polynomial used for fitting
smoothed = savgol_filter(
    noisy_signal,
    window_length=11,
    polyorder=2
)

# Plot smoothed signal
plt.plot(t, smoothed)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Smoothed Signal (Savitzky–Golay Filter)")
plt.show()


# -------------------------------------------------
# STEP 8: Apply Butterworth low-pass filter
# -------------------------------------------------
# N = filter order (higher = sharper cutoff)
# Wn = normalized cutoff frequency (0 to 1)
b, a = butter(
    N=3,
    Wn=0.1
)

# filtfilt applies the filter forward and backward
# This avoids phase shift in the signal
filtered = filtfilt(b, a, noisy_signal)

# Plot Butterworth filtered signal
plt.plot(t, filtered)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Filtered Signal (Butterworth Low-Pass Filter)")
plt.show()
