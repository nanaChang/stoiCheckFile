# stoiCheckFile

File Description:
- refSpeech.wav: 1-channel reference audio signal, with speeches only present in 10s ~ 20s, 30s ~ 40s, 50s ~ 60s time intervals. 
- audio_withBGM.wav: 4-channels microphone received signal with background music playing
- audio_withoutBGM.wav: 4-channels microphone received signal when there's no background music playing
- stoiEvaluation.py: My code for calculating STOI for each signals, taking only channel 2 as interested signal

My STOI Result (taking channel 2 as example):
- 0.1960 for 'audio_withBGM.wav'
- 0.1030 for 'audio_withoutBGM.wav'
