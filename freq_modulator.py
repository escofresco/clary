import numpy as np 
from scipy.io.wavfile import write

import sounddevice as sd
import time

# Synthesized Raw Waveform with Math

# To play music:
# VSCcode extension "wav-preview"
# or sounddevice from requirements

# Samples per second
# Compact Digital Audio encoding signal processing standard is 16 bit values sampled at 44100 Hz (based on what the sound human ear can capture)
sps = 44100
# Frequency / pitch of sine wav
freq_hz = 440.0
# Duration (seconds)
duration_s = 5.0

# Attenuation (amplitude - volume)
attenuation = 0.3

# Modulator Hz
modulator_hz = 0.25  # 0.25 Hz is a period of a quarter second 
# amplitude of waveform/carrier
aw = 1.0
# amplitude sensitivity
ka = 0.75

# Frequency of modulator
fm = 110.0
# deviation constant. no units
# k = 1.0
# k = 11.0
# k = 440.0 # A4
# k = 493.88 # B4
# k = 523.25 # C5
# k = 587.33 # D5
# k = 659.25 # E5


# CREATE a Sine Wave with Numpy
# using python's array instead of list -> drops into C and calculates multiple values at once
each_sample_number = np.arange(duration_s * sps) # a range -> array of numbers we specify (sample number for every sample we want in the wav file comes out to 220,500)
carrier = 2 * np.pi * each_sample_number * freq_hz / sps # numpy calculates our sine wave -> waveform formula (numpy can take an arithmetic operation and broadcast it across an array -> we can multiply sine wave by a value to get the amplitude, we can modify that amplitude to modify the loudness)

# MODULATE
modulator = k * np.sin(2 * np.pi * each_sample_number * fm / sps)

waveform = np.cos(carrier + modulator)

# we don't want the wave to reach an amplitude of 0 -> so we use this envelope. 
# envelope = aw * (1.0 + ka * modulator)
# multiply original waveform values with modulated values -> changed to envelope values
# waveform * modulator -> waveform * envelope
# modulated =  waveform * envelope
# modulated *= attenuation
# modulated_ints = np.int16(modulated * 32797)

# waveform is a series of floats from -1.0 and 1.0, we don't want it to go to the edges of those values bc that's v loud. 
waveform_quiet = waveform * attenuation # attenuation -> everything from max values 1 and -1 to 0.3 and -0.3
waveform_integers = np.int16(waveform_quiet * 32797) # convert floats to ints -> need signed 16bit values


# SAVE as .wav file
write('midi_library/frequency_E5_659.25_modulated.wav', sps, waveform_integers)
# file = "midi_library/first_sine_wave.wav"

# PLAY from speakers
sd.play(waveform_quiet), sps
time.sleep(duration_s)
sd.stop()



