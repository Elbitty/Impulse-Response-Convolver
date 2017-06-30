from wav_array import *
from FFT import fft, inverse_fft
from pylab import size
import sys

source = sys.argv[1]
impulse = sys.argv[2]
conv_output = sys.argv[3]

clip_factor = 1.01 # 클리핑 방지 계수

[impulse, fs_impulse, _] = wavread(impulse) # 임펄스 응답 파일
[target, fs_target, _] = wavread(source) # 처리할 대상 파일

if fs_impulse == fs_target: # 샘플율이 같을 경우
    r_p = fast_conv_vect(target, impulse).real # 과도히 세밀하고 복잡한 부분(e-18 근처)을 피하기 위해 실제 부분만을 취합니다.

    # 오디오 정규화 : "r_p = r_p / max(r_p)"-> "[-1, +1] 범위 밖의 값이 잘리는 경우"
    r_p = r_p/(max(r_p) * clip_factor) # 클리핑을 방지하기 위함.
    wavwrite(r_p, fs_impulse, conv_output)

else:
    # 샘플율이 다를 경우
    pass


def fast_conv_vect(input_signal, impulse):
    # FFT를 수행하는 데 필요한 포인트의 양을 찾아 벡터화 합니다.
    length = size(impulse) + size(input_signal) - 1 # 선형 컨벌루션 길이
    next_pow = nextpow2(length)
    # 곱셈의 IDFT가 순환 컨벌루션이기에 공통적으로 일치시키기 위해서는 N>=L을 충족해야만 합니다.
    # (여기서 L=N1+N2-1;N1=length(input_signal);N2=length(impulse))
    # fft(x, n)는 n개의 포인트를 가지는 FFT입니다. x가 n보다 적으면 남는 부분을 0으로 채우고, 더 많은 경우에는 잘립니다.
    spectral_m = fft(impulse, next_pow) * fft(input_signal, next_pow) # 임펄스와 입력 신호를 FFT하여 곱합니다.
    return inverse_fft(spectral_m) # 타임 도메인 재계산 후 반환.


def nextpow2(length):
    next_no = 2
    while next_no < length:
        next_no = next_no * 2
    return next_no
