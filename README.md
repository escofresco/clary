# clary
## Make Music
Create .wav playable sound files using only math!

## Features:
- Generate sine waves and play them as digital music
- Modulate the digital sine wave through AM or FM 

### Generate sine waves entirely from scratch using Numpy arrays\
- Create a Numpy array of sample size recognizable to human ear\
- Calculate (sample) parts of a sine wave and map those values to the array\
- Play the array by converting to ints and saving as .wav file or using 'sounddevice' library\

### Modulate the digital music sine wave\
- In creating the sine wave, we can modify its properties to achieve any sound\
- Amplitude affects the volume which we simply multiply the array by another const\
- Frequency has another formula entirely which we use to gives us our different pitches\

### Objectives for Samir:
1. [x] Complete - be able to generate a library of modifiable sounds
2. [x] Complete - be able to play those sounds
3. [o] In Progress - combine them into a sequence of sounds