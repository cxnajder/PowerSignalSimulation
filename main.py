import numpy
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import random

### configurable data ###
#frequency = 50
#amplitude = 325
#duration = 0.25
#step = 0.001
### ### ### ### ###

print(
    "1. polish power grid sin wave\n",
    "2. define own signal",
    sep = ""
)
user_choice = int(input())

if user_choice == 1:
    frequency_1 = 50
    amplitude_1 = 325
    duration = 0.1
    step = 0.0005
else:
    duration = float(input('time stop [s]: '))
    step = float(input('time step [s]: '))
    assert duration > step

    print('-------------------------')
    print('FIRST SIGNAL PARAMETERS')
    amplitude_1 = float(input('amplitude [V]: '))
    frequency_1 = int(input('frequency [Hz]: '))


time = numpy.arange(0, duration, step)
signal_1 = amplitude_1 * numpy.sin(2 * numpy.pi * time * frequency_1)


signal_2 = 0 * numpy.sin(2 * numpy.pi * time)

def signal_input():
    print('-------------------------')
    print('ADDING NOISE')
    amplitude = input('amplitude [V]: ')
    if amplitude == 'random':
        min_A = int(input('min: '))
        max_A = int(input('max: '))
        signal = []
        for i in time:
            signal.append(random.randrange(min_A, max_A + 1))

    else:
        amplitude = float(amplitude)
        frequency = int(input('frequency [Hz]: '))
        signal = amplitude * numpy.sin(2 * numpy.pi * time * frequency)
    return signal

repeat_loop = 'yes'

while(repeat_loop != 'no'):
    signal_2 += signal_input()
    repeat_loop = input('Would you like to add another signal? (yes/no): ')


signal_merge = signal_1 + signal_2

N = int(duration / step + 1)
#Fourier
def fourier(signal):
    yf = fft(signal)
    xf = fftfreq(N, step)[:N//2]
    tf =  2/N * numpy.abs(yf[0:N//2])
    return [xf, tf]




def plotSetup(title, signal, x, poz, xlab = "time"):
    plt.subplot(poz)
    plt.plot(x, signal, color='#0F4', linestyle='solid')
    ax = plt.gca()
    ax.set_facecolor('#0D0208')
    plt.xlabel("voltage")
    plt.ylabel(xlab)
    plt.title(title, color = '#0F4')

with plt.rc_context({'axes.edgecolor':'#0F4', 'xtick.color':'#0F4', 'ytick.color':'#0F4', 'figure.facecolor':'#0D0208'}):
    
    plt.figure('Signals', facecolor = "#0D0208", edgecolor="#0F4")


    plotSetup("Singal 1 - sinusoid", signal_1, time, 321)
    plotSetup("Singal 2 - noise", signal_2, time, 323)
    plotSetup("Merged Signals", signal_merge, time, 325)

    [s1_xf, s1_tf] = fourier(signal_1)
    plotSetup("Singal 1 Fourier", s1_tf, s1_xf, 322, "frequency")
    [s2_xf, s2_tf] = fourier(signal_2)
    plotSetup("Singal 2 Fourier", s2_tf, s2_xf, 324, "frequency")
    [sm_xf, sm_tf] = fourier(signal_merge)
    plotSetup("Merged Singal Fourier", sm_tf, sm_xf, 326, "frequency")

    plt.tight_layout()
    plt.show()


 
    
