from tkinter import *

import numpy as np
from skimage import exposure
from skimage.filters import rank
from skimage.morphology import disk

from tabs import Tab


class HistTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)
        group_wyr = LabelFrame(self, text="Wyrównanie", padx=5, pady=5)
        group_wyr.pack(padx=10, pady=10)
        group_roz = LabelFrame(self, text="Rozciągnięcie", padx=5, pady=5)
        group_roz.pack(padx=10, pady=10)
        w = Scale(master=group_wyr, orient=HORIZONTAL, from_=0, to=20)
        s1 = Scale(master=group_roz, orient=HORIZONTAL, from_=0, to=100)
        s1.set(0)
        s2 = Scale(master=group_roz, orient=HORIZONTAL, from_=0, to=100)
        s2.set(100)

        def global_eq(x, img):
            new_img = tuple([exposure.equalize_hist(img[:, :, i]) for i in range(0, 3)])
            x = np.stack(new_img, axis=-1) * 255
            return x

        def local_eq(x, img):
            size = int(w.get())
            if size == 0:
                return img
            selem = disk(img.shape[0] / size)
            new_img = tuple([rank.equalize(img[:, :, i], selem=selem) for i in range(0, 3)])
            x = np.stack(new_img, axis=-1)
            return x

        Label(master=group_wyr, text="Stosunek szerokości obrazka do bloku:").pack()
        w.pack()
        # Button(master=self, text="Wyrównaj globalnie", command=lambda: fun(global_eq, 0)).pack()
        Button(master=group_wyr, text="Wyrównaj", command=lambda: fun(local_eq, 0)).pack()
        Label(master=group_wyr, text="Percentyle:").pack()
        s1.pack()
        s2.pack()

        def stretch(x, img):
            p1 = np.percentile(img, int(s1.get()))
            p2 = np.percentile(img, int(s2.get()))
            if p1 > p2: p1 = p2
            return exposure.rescale_intensity(img, in_range=(p1, p2))

        Button(master=group_roz, text="Rozciągnij", command=lambda: fun(stretch, 0)).pack()
