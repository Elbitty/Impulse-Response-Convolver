# Convolver DSP Impulses
### Phase transform and  time correction DSP Impulses.
In conventional audio systems (such as speakers and headphones), the high frequency band tends to be delayed as compared with the low frequency band. When we hear such sounds, although the acoustic spectrum looks the same as the electrical input signal, but it actually sounds like the low frequency band has masked the high frequency band so the clarity and resolution have been reduced. Generally to restore this reduced clarity and resolution, increase the high frequency band using a common equalizer or tone control, according to the Equal Loudness Contour. In this case, the sound of audition may sound somewhat improved, but it may cause a rough and unnatural feeling.

When time-aligning the frequency spectrum by delaying the middle-low frequency band instead of merely increasing the high frequency band, due to the large amount of information, the more important high-frequency band reach to the listener first, and feels like a live sound. This is significantly different from the equalizer or tone control, which simply controls the amplitude.

---

BBE-44.1.wav
 - 32Bit, 44100Hz PCM Impulse, 50% applied.
 
BBE-192.wav
 - 32Bit, 192000Hz PCM Impulse, 50% applied.
 
 ---
 
### 위상 지연 및 시간 보정 DSP 임펄스입니다.

스피커, 이어폰, 헤드폰 등 기존의 오디오 시스템에서는 고주파 대역이 저주파 대역에 비해 지연되는 경향이 있습니다. 우리가 그러한 소리를 듣게 되면, 음향 스펙트럼은 전기적인 입력 신호와 똑같아 보일지라도, 실제로는 저주파 대역이 고주파 대역을 가로막아(masking effect) 명료도와 해상도가 감소된 것 처럼 들립니다. 일반적인 경우에는 이처럼 감소되어 들리는 선명도와 명료도를 복구하기 위하여 Equal Loudness Contour에 따라 일반적인 이퀄라이저나 Tone control을 사용하여 고주파 대역을 증대시킵니다. 이 경우에 청감상의 소리는 어느 정도 향상되어 들리지만, 거칠고 부자연스러운 느낌이 생길 수 있습니다. 

단순히 고주파 대역을 증대시키는 대신, 중~저주파 대역을 지연시켜 주파수 스펙트럼의 시간정렬(time-align)을 수행할 경우 정보량이 많아 중요한 고주파 대역이 청자에게 먼저 도착하게 되어, 라이브 사운드처럼 느껴지게 됩니다. 이는 단순히 진폭만을 조절하는 이퀄라이저나 Tone control과는 상당한 차이가 있습니다. 


Usage:
---
`python convolution.py --input.wav --BBE-44.1.wav --output.wav`
 
 
Only files in PCM WAV format can be used.
 
사용되는 모든 파일은 PCM 형식의 WAV여야만 합니다. 
