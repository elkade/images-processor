import os
from time import gmtime, strftime
from tkinter import filedialog

import PIL.Image
import PIL.ImageTk
import matplotlib
import numpy as np

from GammaTab import GammaTab
from HistTab import HistTab
from ImageFrame import ImageFrame
from MorphTab import MorphTab
from tabs import *

matplotlib.use('TkAgg')
root = Tk()
root.wm_title("Łukasz Dragan - Podstawy przetwarzania obrazow")

initial_image = PIL.Image.open("lenna.png")

original_image_frame = ImageFrame(root, initial_image, "Original image")
original_image_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

transformed_image_frame = ImageFrame(root, initial_image, "Transformed image")
transformed_image_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

tab_frame = Frame(root)
tab_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)


def save_image():
    file_path = os.path.join('img', "img_" + strftime("%Y-%m-%dT%H:%M:%S", gmtime()))
    # filedialog.asksaveasfilename(defaultextension=".jpg")
    if not file_path:
        return

    transformed_image_frame.get_image().save(file_path, "JPEG")
    load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path))


def load_image(file_path=None):
    if file_path is None:
        file_path = filedialog.askopenfilename()
    if not file_path:
        return
    image = PIL.Image.open(os.path.join('img', file_path))
    original_image_frame.update(image)
    transformed_image_frame.update(image)


def update_image(fun):
    image = original_image_frame.get_image()
    np_image = np.asarray(image)
    new_np_image = fun(np_image)
    image = PIL.Image.fromarray(np.uint8(new_np_image))
    transformed_image_frame.update(image)


Button(original_image_frame, text="Load image...", command=load_image).pack(anchor=NW, side=LEFT)
Button(original_image_frame, text="Save image", command=save_image).pack(anchor=NW, side=LEFT)

bar = TabBar(tab_frame, "Kontrast")

tab1 = HistTab(tab_frame, "Kontrast", update_image)

tab2 = GammaTab(tab_frame, "Jasność", update_image)

tab3 = MorphTab(tab_frame, "Filtry", update_image)

bar.add(tab1)
bar.add(tab2)
bar.add(tab3)

bar.show()

mainloop()
