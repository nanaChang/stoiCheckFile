from pystoi.stoi import stoi
from scipy.io import wavfile

fs, ref_signal = wavfile.read('refSpeech.wav')
fs, audio_wBGM = wavfile.read('audio_withBGM.wav')
fs, audio_woBGM = wavfile.read('audio_withoutBGM.wav')

# pick channel two as interested channel
audio_wBGM = audio_wBGM[:, 2]
audio_woBGM = audio_woBGM[:, 2]

# STOI Evaluation
print(stoi(ref_signal, audio_wBGM, fs, extended=False))
print(stoi(ref_signal, audio_woBGM, fs, extended=False))
