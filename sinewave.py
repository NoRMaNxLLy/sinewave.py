#!/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def read_input():
    A = float(input('Amplitude: '))
    f = float(input('frequency: '))
    t_start = float(input('time domain: '))
    t_end = float(input('time domain: '))
    P = float(input('Phase: '))
    return A, f, t_start, t_end, P

if len(sys.argv) == 6:
    # return a list with integer values.
    A, f, t_start, t_end, P = [float(i) for i in sys.argv[1:]]
else:
    A, f, t_start, t_end, P = read_input()

T = 1 / f
s_rate = 2 * f
# convert the Phase shift from d to rad
P = P * 2 * np.pi / 360

# return a x and y list of cordinates
x = np.arange(t_start, t_end, 0.001)
y = A * np.sin(2 * np.pi * f * x + P)

# ploting
plt.plot(x, y)
plt.axhline(y=0, color='black')
plt.xlabel('Time')
plt.ylabel('Amplitude')
#plt.axis([-2, 2, -5, A])
plt.title(r'$S(t) = A \sin(2\pi ft + \O)$', loc='center')
plt.show()
