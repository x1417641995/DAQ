
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)
# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma
for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    '''for i in range(100000000):
        # Do calculations to attain next data point
        pass'''
    plt.pause(0.5)
    fig.canvas.draw()
    fig.canvas.flush_events()