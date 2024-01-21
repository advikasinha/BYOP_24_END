import ctypes
import numpy as np
import time

# Function to set gamma ramp
def set_gamma_ramp(gamma_ramp):
    hdc = ctypes.windll.user32.GetDC(0)

    # Convert gamma_ramp to a contiguous 1D array of 16-bit unsigned integers
    gamma_ramp_flat = np.require(gamma_ramp, dtype=np.uint16, requirements='C')

    # Pass the pointer to the data as the second argument
    ctypes.windll.gdi32.SetDeviceGammaRamp(hdc, gamma_ramp_flat.ctypes.data_as(ctypes.POINTER(ctypes.c_ushort)))
    ctypes.windll.user32.ReleaseDC(0, hdc)

# Function to generate a gamma ramp with modified hues
def generate_hue_gamma_ramp(hue_factor):
    gamma_ramp_size = 256
    gamma_ramp = np.zeros((3, gamma_ramp_size), dtype=np.uint16)

    for i in range(gamma_ramp_size):
        intensity = i / (gamma_ramp_size - 1)
        adjusted_intensity = intensity ** hue_factor
        gamma_ramp[0, i] = gamma_ramp[1, i] = gamma_ramp[2, i] = int(adjusted_intensity * 65535)

    return gamma_ramp
'''
# Function to gradually change hues over time
def change_hues_over_time(duration_seconds, steps):
    for step in range(steps):
        hue_factor = 1.0 + 0.2 * np.sin(2 * np.pi * step / steps)
        gamma_ramp = generate_hue_gamma_ramp(hue_factor)
        set_gamma_ramp(gamma_ramp)
        time.sleep(duration_seconds / steps)

# Example usage: Change hues gradually over 10 seconds in 100 steps
change_hues_over_time(10, 100)


#ambient
def change_hues_over_time_reading(duration_seconds, steps):
    for step in range(steps):
        # Use a sinusoidal function for smooth variation
        hue_factor = 0.9 + 0.1 * np.sin(2 * np.pi * step / steps)
        gamma_ramp = generate_hue_gamma_ramp(hue_factor)
        set_gamma_ramp(gamma_ramp)
        time.sleep(duration_seconds / steps)

# Example usage for ambient mode during reading
change_hues_over_time_reading(60, 100)  # 10 minutes with 100 steps

'''

#constant hue factor
def keep_hue_factor_around_one(duration_seconds, steps):
    constant_hue_factor = 0.8
    #would have to change this value each time
    gamma_ramp = generate_hue_gamma_ramp(constant_hue_factor)

    for step in range(steps):
        set_gamma_ramp(gamma_ramp)
        time.sleep(duration_seconds / steps)

# Example usage for keeping hue factor around 1.0 for browsing/watching
keep_hue_factor_around_one(10, 100)  # Keep hue factor around 1.0 for 10 seconds with 100 steps


#constant hue for play and watch 
#dynamic hue of 0.8 to 1.0 for read and write
#constant hue of 1.0 for browse and debug too

#1.0 natural colour appearance
#0.8 subtle warm 
#1.2 cool tone
