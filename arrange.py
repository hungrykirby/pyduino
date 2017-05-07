import numpy as np
from scipy import signal
from pylab import *

class Arrange:
    bwn_a = False
    ax = None
    n = np.arange(-0.5, 0.5, 0.01)
    plots_numbers = []
    def __init__(self, serial):
        self.ser = serial

    def plots(self, x, y, z):
        #figure(figsize=(8, 8))
        #subplot(511)
        clf()
        axis([-1500, 1500, -0.5, 5.5])
        subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.5)
        plot(x, 1, 'o')
        plot(y, 3, '*')
        plot(z, 5, 'd')
        pause(0.00001)

    def fetch_three_numbers(self, matched_group):
        try:
            if matched_group == "a":
                self.bwn_a = True
                self.plots_numbers = []
            elif self.bwn_a:
                self.plots_numbers.append(matched_group)

            if len(self.plots_numbers) == 3:
                pl = self.plots_numbers
                #self.plots(pl[0], pl[1], pl[2])
                self.bwn_a = False
                self.ser.flushInput()
                print(pl)
        except KeyboardInterrupt:
            ser.close()
