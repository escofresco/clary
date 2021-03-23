# clary
## Make Music

Synthesizer made from scratch
Create waveform sound files using only math!

## Features:
- Generate sine waves and play them as digital music ------->   scipiwav.py
- Modulate the digital sine wave via AM or FM -------------->   amp_modulator.py & freq_modulator.py

### Generate sine waves entirely from scratch using Numpy arrays
**scipiwav.py**
- Create a Numpy array of sample size recognizable to human ear
- Calculate/sample (analog to digital) parts of a sine wave and map those values to the array
- Play the array by converting to ints and saving as .wav file or using 'sounddevice' library

### Modulate the digital music sine wave
**amp_modulator.py & freq_modulator.py**
- In creating the sine wave, we can modify its properties to achieve any sound
- Amplitude affects the volume which we simply multiply the array by another const
- Frequency has another formula entirely which we use to gives us our different pitches

**Generated music notes and modulations are available in the midi_library folder.**

**Frequencies of Notes[!https://pages.mtu.edu/~suits/notefreqs.html]**


### Objectives Samir:
1. [x] Complete - Generate sounds (sine waves)
2. [x] Complete - Modulate sounds (AM/FM)
3. [x] Almost complete - Combine sequence of sounds

Acknowledgements:
alicia.science