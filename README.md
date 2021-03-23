# clary
## Make Music

Synthesizer made from scratch
Create waveform sound files using only math!

## Features:
- Generate sine waves and play them as digital music ------->   scipiwav.py
- Modulate the digital sine wave via AM or FM -------------->   amp_modulator.py & freq_modulator.py

### :loud_sound: Generate sine waves entirely from scratch using Numpy arrays
**:file_folder: scipiwav.py**
- Create a Numpy array of sample size recognizable to human ear
- Calculate/sample (analog to digital) parts of a sine wave and map those values to the array
- Play the array by converting to ints and saving as .wav file or using 'sounddevice' library

### :notes: Modulate the digital music sine wave
**:file_folder: amp_modulator.py & freq_modulator.py**
- In creating the sine wave, we can modify its properties to achieve any sound
- Amplitude affects the volume which we simply multiply the array by another const
- Frequency has additional steps which we use to give us different pitches, we use the k const as the deviation metric

**Generated music notes and modulations are available in the midi_library folder.**

[Frequencies of Notes](https://pages.mtu.edu/~suits/notefreqs.html)


### Objectives Samir:
1. [x] Complete - Generate sounds (sine waves)
2. [x] Complete - Modulate sounds (AM/FM)
3. [x] Almost complete - Combine sequence of sounds

Acknowledgements:
alicia.science