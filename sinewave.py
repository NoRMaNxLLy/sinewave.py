#!/usr/bin/python3

import sys
import numpy as np
import matplotlib.pyplot as plt

waves = {}
add_noise = False
decompose = False
t_start, t_end = 0, 1
noise_scale = 0.25

for i in range(1,len(sys.argv)):
    arg = sys.argv[i]

    if arg == '--wave' or arg == '-w':
        waves[i] = sys.argv[i+1].split()

    elif arg == '--noise' or arg == '-n':
        add_noise = True

    elif arg == '--time' or arg == '-t':
        t_start, t_end = [float(t) for t in sys.argv[i+1].split()]

    elif arg == '--decompose' or arg == '-d':
        decompose = True

    elif arg == '-ns' or arg == '--noise-scale':
        add_noise = True
        noise_scale = float(sys.argv[i+1])

#x = np.arange(t_start, t_end, 0.001)
x = np.linspace(t_start, t_end, 8000)
y = 0

for v in waves.values():
    # unpack the list
    A, f, P = [float(i) for i in v]

    # convert the Phase shift from d to rad
    P = P * 2 * np.pi / 360

    # return the y values
    y += A * np.sin(2 * np.pi * f * x + P)

    if decompose:
        i = A * np.sin(2 * np.pi * f * x + P)
        plt.plot(x, i, label=f'A = {A} f = {f} P = {P * 360 / (2 * np.pi)} ')

# add noise if needed
if add_noise:
    noise = np.random.normal(scale=noise_scale, size=x.size)
    y += noise

    if decompose:
        plt.plot(x, noise, label='noise')

# ploting
plt.plot(x, y, label='total')
plt.axhline(y=0, color='black')
plt.xlabel('Time')
plt.ylabel('Amplitude')
if decompose:
    plt.legend(loc='upper right')

# start drawing from 0
plt.xlim(left=t_start, right=t_end)
plt.show()
