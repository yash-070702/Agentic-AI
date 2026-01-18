# ---------------------------------------------
# Installation command (run once in terminal)
# ---------------------------------------------
# pip install scipy

import numpy as np
from scipy import signal, datasets   # (not used here, but often used in SciPy workflows)
import matplotlib.pyplot as plt
from scipy import interpolate


# ---------------------------------------------
# STEP 1: Known depth values (in meters)
# ---------------------------------------------
# These represent measured depths in an oil well
depths = np.array([1000, 1500, 2000, 2500, 3000]) 


# ---------------------------------------------
# STEP 2: Known pressure values (in psi)
# ---------------------------------------------
# Each pressure value corresponds to the same index depth
pressures = np.array([3500, 4000, 4500, 5000, 5500])


# ---------------------------------------------
# STEP 3: Plot original data (without interpolation)
# ---------------------------------------------
plt.figure(figsize=(8,6))
plt.plot(depths, pressures, 'o', label='Original Data Points', color='red')
plt.title('Pressure vs Depth in an Oil Well - Without Interpolation')
plt.xlabel('Depth (m)')
plt.ylabel('Pressure (psi)')
plt.legend()
plt.grid(True)
plt.show()


# ---------------------------------------------
# STEP 4: Create interpolation function
# ---------------------------------------------
# interp1d creates a function that estimates pressure
# at any depth within the given range
# kind='cubic' gives a smooth curve (cubic spline)
pressure_interpolation = interpolate.interp1d(
    depths,
    pressures,
    kind='cubic'
)


# ---------------------------------------------
# STEP 5: Generate new depth values
# ---------------------------------------------
# These are depths where pressure is not measured
depths_to_interpolate = np.linspace(1000, 3000, 100)


# ---------------------------------------------
# STEP 6: Compute interpolated pressure values
# ---------------------------------------------
interpolated_pressures = pressure_interpolation(depths_to_interpolate)


# ---------------------------------------------
# STEP 7: Plot original data + interpolated curve
# ---------------------------------------------
plt.figure(figsize=(8,6))
plt.plot(depths, pressures, 'o', label='Original Data Points', color='red')
plt.plot(
    depths_to_interpolate,
    interpolated_pressures,
    '--',
    label='Cubic Interpolation',
    color='blue'
)
plt.title('Pressure vs Depth Interpolation in an Oil Well')
plt.xlabel('Depth (m)')
plt.ylabel('Pressure (psi)')
plt.legend()
plt.grid(True)
plt.show()
