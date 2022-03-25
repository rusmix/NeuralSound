import soundfile as sf
import numpy as np
from scipy.fft import rfft, rfftfreq, irfft
from matplotlib import pyplot as plt
import math
# SAMPLE_RATE = 44100  # Hertz
# DURATION = 5  # Seconds

data, samplerate = sf.read('startingCar.wav')
print(samplerate, len(data))

yf = rfft(data)
xf = rfftfreq(len(data), 1 / samplerate)
print(len(yf))
# The maximum frequency is half the sample rate
points_per_freq = len(xf) / (samplerate  / 2)
yf [:int(500 * points_per_freq)] = 0
plt.plot(data)
# plt.plot(xf,np.abs(yf))
# plt.show()

new_sig = irfft(yf)
# plt.plot(new_sig)
# plt.show()
sf.write('startingCar2.wav', new_sig, samplerate)
# write("startingCar2.wav", samplerate, normalized_tone)