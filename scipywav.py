import os
import numpy as np
from scipy.io.wavfile import write

# in VSCode install extension wav-preview to play the files created

sps = 44100

freq_hz = 440.0

duration_s = 5.0

# Create a Sine Wave
each_sample_number = np.arange(duration_s * sps)
waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32797)

# Save as .wav file
write('midi_library/first_sine_wave.wav', sps, waveform_integers)

# file = "midi_library/first_sine_wave.wav"

