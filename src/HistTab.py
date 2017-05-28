from tkinter import *

from skimage.exposure import adjust_gamma

from tabs import Tab
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from skimage import data
from skimage.util.dtype import dtype_range
from skimage.util import img_as_ubyte
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank

class HistTab(Tab):
    def __init__(self, frame, name, fun):
        Tab.__init__(self, frame, name)
        Label(self, text="Gamma").pack(side=TOP, fill=BOTH, expand=YES)
        w = Scale(master=self, orient=HORIZONTAL, from_=1, to=20)
        def global_eq(x, img):
            img_1 = exposure.equalize_hist(img[:,:,0])
            img_2 = exposure.equalize_hist(img[:,:,1])
            img_3 = exposure.equalize_hist(img[:,:,2])
            x = np.stack((img_1, img_2, img_3), axis=-1)*255
            return x

        def local_eq(x, img):
            selem = disk(img.shape[0] / int(w.get()))
            img_1 = rank.equalize(img[:,:,0], selem=selem)
            img_2 = rank.equalize(img[:,:,1], selem=selem)
            img_3 = rank.equalize(img[:,:,2], selem=selem)
            x = np.stack((img_1, img_2, img_3), axis=-1)
            return x
        Label(master=self, text="stosunek wielkości obrazka do bloku:").pack()
        w.pack()
        #Button(master=self, text="Wyrównaj globalnie", command=lambda: fun(global_eq, 0)).pack()
        Button(master=self, text="Wyrównaj", command=lambda: fun(local_eq, 0)).pack()


