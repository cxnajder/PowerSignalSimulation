import numpy
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

### configurable data ###
#frequency = 50
#amplitude = 325
#duration = 0.25
#step = 0.001
### ### ### ### ###


duration = float(input('time stop [s]: '))
step = float(input('time step [s]: '))
assert duration > step
time = numpy.arange(0, duration, step)

print('-------------------------')
print('FIRST SIGNAL PARAMETERS')
frequency_1 = int(input('frequency [Hz]: '))
amplitude_1 = int(input('amplitude [V]: '))

print('-------------------------')
print('SECOND SIGNAL PARAMETERS')
frequency_2 = int(input('frequency [Hz]: '))
amplitude_2 = int(input('amplitude [V]: '))

#generating signals
signal_1 = amplitude_1 * numpy.sin(2 * numpy.pi * time * frequency_1)
signal_2 = amplitude_2 * numpy.sin(2 * numpy.pi * time * frequency_2)
signal_merge = signal_1 + signal_2

N = int(duration / step + 1)
#Fourier
def fourier(signal):
    yf = fft(signal)
    xf = fftfreq(N, step)[:N//2]
    tf =  2/N * numpy.abs(yf[0:N//2])
    return [xf, tf]




def plotSetup(title, signal, x, poz):
    plt.subplot(poz)
    plt.plot(x, signal, color='#0F4', linestyle='solid')
    ax = plt.gca()
    ax.set_facecolor('#0D0208')
    plt.xlabel("voltage")
    plt.ylabel("time")
    plt.title(title, color = '#0F4')

with plt.rc_context({'axes.edgecolor':'#0F4', 'xtick.color':'#0F4', 'ytick.color':'#0F4', 'figure.facecolor':'#0D0208'}):
    
    plt.figure('Signals', facecolor = "#0D0208", edgecolor="#0F4")


    plotSetup("Singal 1 - sinusoid", signal_1, time, 321)
    plotSetup("Singal 2 - noise", signal_2, time, 323)
    plotSetup("Merged Signals", signal_merge, time, 325)

    [s1_xf, s1_tf] = fourier(signal_1)
    plotSetup("Singal 1 Fourier", s1_tf, s1_xf, 322)
    [s2_xf, s2_tf] = fourier(signal_2)
    plotSetup("Singal 2 Fourier", s2_tf, s2_xf, 324)
    [sm_xf, sm_tf] = fourier(signal_merge)
    plotSetup("Merged Singal Fourier", sm_tf, sm_xf, 326)

    plt.tight_layout()
    plt.show()
