# clary
## Make Music

Synthesizer made from scratch\
Create waveform sound files using **only math!**

## Features:
:file_folder: scipiwav.py -- Generate sine waves and play them as digital music\
:file_folder: amp_modulator.py -- Modulate amplitude of digital sine wave AM\
:file_folder: freq_modulator.py -- Modulate frequency of digital sine wave FM
:file_folder: midi_library -- Store musical notes in wav format

## :loud_sound: Generate sine waves entirely from scratch using Numpy arrays
**scipiwav.py**
- Create a Numpy array of sample size recognizable to human ear
- Calculate/sample (analog to digital) parts of a sine wave and map those values to the array
- Play the array by converting to ints and saving as .wav file or using 'sounddevice' library

## :notes: Modulate the digital music sine wave
**amp_modulator.py & freq_modulator.py**
- In creating the sine wave, we can modify its properties to achieve any sound
- Amplitude affects the volume which we simply multiply the array by another const
- Frequency has additional steps which we use to give us different pitches, we use the k const as the deviation metric


[Frequencies of Notes](https://pages.mtu.edu/~suits/notefreqs.html)


## Objectives Samir:
1. [x] Complete - Generate sounds (sine waves)
2. [x] Complete - Modulate sounds (AM/FM)
3. [x] Almost complete - Combine sequence of sounds

Acknowledgements:
alicia.science