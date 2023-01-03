#Grabadora de audio

import sounddevice
from scipy.io.wavfile import write

fs=44100 #sample_rate

second=int(input('Introduce el tiempo de duracion en segundos'))

print('Recording....\n')

record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)

sounddevice.wait()

write('out.wav', fs,record_voice)

print('Finished...\nPlease Check it...')