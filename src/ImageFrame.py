from tkinter import *

import PIL.Image
import PIL.ImageTk
from hist_plot import get_hist_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from tabs import Tab, TabBar


class ImageHistogramTab(Tab):
    def __init__(self, frame, name, index, image):
        Tab.__init__(self, frame, name)
        self._widget = None
        self._index = index
        self.update(image)

    def update(self, image):
        figure = Figure(figsize=(5, 4), dpi=100)
        plot = figure.add_subplot(111)
        np_image = np.asarray(image)
        get_hist_plot(np_image[:,:,self._index], plot)
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.show()
        if self._widget:
            self._widget.pack_forget()
        self._widget = canvas.get_tk_widget()
        self._widget.pack(side=TOP, fill=BOTH, expand=1)


class ImageFrame(Frame):
    def __init__(self, master, image, name):
        Frame.__init__(self, master)
        self._frame = LabelFrame(self, text=name, padx=5, pady=5)
        self._frame.pack()
        self._image = image
        w, h = self._get_w_h(image)
        pil_image = PIL.ImageTk.PhotoImage(image.resize((w, h)))

        self._image_widget = Label(self._frame, image=pil_image)
        self._image_widget.image = pil_image
        self._image_widget.pack()

        bar = TabBar(self._frame, "R")

        self._tabs = [
            ImageHistogramTab(self._frame, "R", 0, image),
            ImageHistogramTab(self._frame, "G", 1, image),
            ImageHistogramTab(self._frame, "B", 2, image)
        ]
        for tab in self._tabs:
            bar.add(tab)
        bar.show()

    def get_image(self):
        return self._image

    def update(self, image):
        self._image = image
        w, h = self._get_w_h(image)
        pil_image = PIL.ImageTk.PhotoImage(image.resize((w, h)))
        self._image_widget.config(image=pil_image)
        self._image_widget.image = pil_image
        for tab in self._tabs:
            tab.update(image)

    def _get_w_h(self, image):
        w, h = image.size
        if w > h:
            if w > 512:
                scale = 512/w
                w = 512
                h *= scale
        else:
            if h > 512:
                scale = 512/h
                h = 512
                w *= scale
        return int(w), int(h)