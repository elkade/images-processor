from tkinter import *

from skimage.exposure import adjust_gamma

from tabs import Tab
import numpy as np


class GammaTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)
        Label(self, text="Gamma").pack(side=TOP, fill=BOTH, expand=YES)

        def gamma(x, X):
            l = np.log(int(x) / 100) * -1
            print(l)
            return adjust_gamma(X, gamma=l, gain=1)

        w = Button(master=self, command=lambda x: fun(gamma, x))
        w.pack()
