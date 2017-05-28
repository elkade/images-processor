from tkinter import *

from skimage.exposure import adjust_gamma

from tabs import Tab
import numpy as np


class GammaTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)
        Label(self, text="Gamma").pack(side=TOP, fill=BOTH, expand=YES)
        w = Scale(master=self, orient=HORIZONTAL, from_=-100, to=100)

        def gamma(x, X):
            size = int(w.get())
            l = 1.03**size
            print(l)
            return adjust_gamma(X, gamma=l, gain=1)

        w.pack()
        Button(master=self, text="Gamma", command=lambda: fun(gamma, 0)).pack()

