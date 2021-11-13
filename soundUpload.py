import librosa
import soundfile
import IPython.display as ipd
audio_data = 'bensound-creativeminds.ogg'
y, sr = soundfile.load(audio_data)
print (len(y), sr)

for i in range(len(y)):




#ipd.Audio(audio_data)
