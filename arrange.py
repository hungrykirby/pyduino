import numpy as np
from scipy import signal
from pylab import *
import os

class Arrange:
    past_c = "xx"
    bwn_a = False
    ax = None
    n = np.arange(-0.5, 0.5, 0.01)
    plots_numbers = []
    MODE = "train"
    count = 0
    pattern = {"train": 30, "test":10}
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

    def write_ceps(self, ceps, fn_):
        fn = os.path.join(os.getcwd(), self.MODE, fn_)
        if not os.path.exists(fn):
            os.makedirs(fn)
        #base_fn,ext = os.path.splitext(fn)
        data_fn = os.path.join(self.MODE, fn_, str(self.count) + ".ceps")
        np.save(data_fn,ceps)
        self.count += 1

    def fetch_three_numbers(self, matched_group, c):
        if self.past_c != c:
            self.past_c = c
            self.count = 0
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
                print(c, pl)
                if self.count < self.pattern[self.MODE]:
                    self.write_ceps(np.array(pl).np.array(pl), c)
                    print(pl)
                    print(np.array(pl).astype(np.int64))
        except KeyboardInterrupt:
            ser.close()
