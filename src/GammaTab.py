from tkinter import *

from skimage.exposure import adjust_gamma

from tabs import Tab

import numpy as np

class GammaTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)

        vars = [None] * 3
        col_frame = Frame(self, padx=5, pady=5)
        col_frame.pack(padx=10, pady=10)
        cb = [None] * 3
        c = ["R", "G", "B"]
        for i in range(3):
            vars[i] = IntVar()
            cb[i] = Checkbutton(col_frame, text=c[i], variable=vars[i])
            cb[i].pack(anchor=NW, side=LEFT)

        w = Scale(master=self, orient=HORIZONTAL, from_=-100, to=100, length=200)

        def gamma(np_image):
            size = int(w.get())
            l = 1.03**size
            new_img = tuple(
                [(adjust_gamma(np_image[:, :, i], gamma=l, gain=1)) if vars[i].get() == 1 else np_image[:, :, i] for i in
                 range(0, 3)])
            x = np.stack(new_img, axis=-1)
            return x

        w.pack()
        Button(master=self, text="Gamma", command=lambda: fun(gamma)).pack()

