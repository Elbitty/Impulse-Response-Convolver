# Convolver-DSP_Impulses
Phase transform DSP Impulses.
---

BBE-44.1.wav
 - 32Bit, 44100Hz PCM Impulse
 
BBE-192.wav
 - 32Bit, 192000Hz PCM Impulse
 
위상 지연 및 시간 보정 DSP 임펄스입니다.

스피커, 이어폰, 헤드폰 등 기존의 오디오 시스템에서는 고주파 대역이 저주파 대역에 비해 지연되는 경향이 있습니다. 우리가 그러한 소리를 듣게되면, 음향 스펙트럼은 전기적인 입력 신호와 똑같아 보일지라도, 실제로는 저주파 대역이 고주파 대역을 가로막아(masking effect) 명료도와 해상도가 감소된 것 처럼 들립니다. 이처럼 감소되어 들리는 선명도와 명료도를 복구하기 위하여 Equal Loudness Contour에 따라 일반적인 이퀄라이저나 Tone control을 사용하여 고주파 대역을 증대시킵니다. 이 경우에 청감상의 소리는 어느 정도 향상되어 들리지만, 거칠고 부자연스러운 느낌이 생길 수 있습니다. 

단순히 고주파 대역을 증가시키는 대신, 중~저주파 대역을 지연시켜 주파수 스펙트럼의 시간정렬(time-align)을 수행할 경우 정보량이 많아 중요한 고주파 대역이 청자에게 먼저 도착하게 되어, 라이브 사운드처럼 느껴지게 됩니다. 이는 단순히 고주파 대역의 진폭만을 증가시키는 이퀄라이저나 Tone control과는 상당한 차이가 있습니다. 

# Usage:
---
 > python convolution.py input.wav BBE-44.1.wav output.wav
 
사용되는 모든 파일은 PCM 형식의 WAV여야만 합니다. 
