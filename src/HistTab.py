from tkinter import *

import numpy as np
from skimage import exposure
from skimage.filters import rank
from skimage.morphology import disk

from tabs import Tab


class HistTab(Tab):
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

        group_wyr = LabelFrame(self, text="Wyrównanie", padx=5, pady=5)
        group_wyr.pack(padx=10, pady=10)
        group_roz = LabelFrame(self, text="Rozciągnięcie", padx=5, pady=5)
        group_roz.pack(padx=10, pady=10)
        w = Scale(master=group_wyr, orient=HORIZONTAL, from_=0, to=20, length=200)
        s1 = Scale(master=group_roz, orient=HORIZONTAL, from_=0, to=100, length=200)
        s1.set(0)
        s2 = Scale(master=group_roz, orient=HORIZONTAL, from_=0, to=100, length=200)
        s2.set(100)

        def local_eq(np_image):
            size = int(w.get())
            if size == 0:
                return np_image
            selem = disk(np_image.shape[0] / size)
            new_img = tuple(
                [(rank.equalize(np_image[:, :, i], selem=selem)) if vars[i].get() == 1 else np_image[:, :, i] for i in
                 range(0, 3)])
            x = np.stack(new_img, axis=-1)
            return x

        Label(master=group_wyr, text="Stosunek szerokości obrazka do bloku:").pack()
        w.pack()
        # Button(master=self, text="Wyrównaj globalnie", command=lambda: fun(global_eq, 0)).pack()
        Button(master=group_wyr, text="Wyrównaj", command=lambda: fun(local_eq)).pack()
        Label(master=group_roz, text="Percentyle:").pack()
        s1.pack()
        s2.pack()

        def stretch(np_image):
            p1 = np.percentile(np_image, int(s1.get()))
            p2 = np.percentile(np_image, int(s2.get()))
            if p1 > p2: p1 = p2
            new_img = tuple([exposure.rescale_intensity(np_image[:, :, i], in_range=(p1, p2)) if vars[
                                                                                                     i].get() == 1 else np_image[
                                                                                                                        :,
                                                                                                                        :,
                                                                                                                        i]
                             for i in range(0, 3)])
            x = np.stack(new_img, axis=-1)
            return x

        Button(master=group_roz, text="Rozciągnij", command=lambda: fun(stretch)).pack()
