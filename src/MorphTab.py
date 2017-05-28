from tkinter import *

import numpy as np
from skimage.morphology import dilation
from skimage.morphology import disk
from skimage.morphology import erosion
from skimage.morphology import square

from tabs import Tab


class MorphTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)
        group_dil = LabelFrame(self, text="Dylatacja", padx=5, pady=5)
        group_dil.pack(padx=10, pady=10)
        group_er = LabelFrame(self, text="Erozja", padx=5, pady=5)
        group_er.pack(padx=10, pady=10)
        w1 = Scale(master=group_dil, orient=HORIZONTAL, from_=1, to=20)
        w2 = Scale(master=group_er, orient=HORIZONTAL, from_=1, to=20)

        def dil(np_image):
            size = int(w1.get())
            if size == 0: return np_image
            new_img = tuple([dilation(np_image[:, :, i], selem=disk(size)) for i in range(0, 3)])
            return np.stack(new_img, axis=-1)

        Label(master=group_dil, text="Stosunek szerokości obrazka do bloku:").pack()
        w1.pack()
        Button(master=group_dil, text="Dylatacja", command=lambda: fun(dil)).pack()

        def er(np_image):
            size = int(w2.get())
            if size == 0: return np_image
            new_img = tuple([erosion(np_image[:, :, i], selem=disk(size)) for i in range(0, 3)])
            x = np.stack(new_img, axis=-1)
            return x

        Label(master=group_er, text="Stosunek szerokości obrazka do bloku:").pack()
        w2.pack()
        Button(master=group_er, text="Erozja", command=lambda: fun(er)).pack()
