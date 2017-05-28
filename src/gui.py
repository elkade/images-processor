import os
from time import gmtime, strftime
from tkinter import filedialog

import PIL.Image
import PIL.ImageTk
import matplotlib
import numpy as np

from GammaTab import GammaTab
from HistTab import HistTab
from MorphTab import MorphTab
from tabs import *
matplotlib.use('TkAgg')
root = Tk()
root.wm_title("Łukasz Dragan - Podstawy przetwarzania obrazow")

image_frame = Frame(root)
image_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

# Label(tab3, bg='white', text="Tab3 text").pack(
#     side=LEFT, expand=YES, fill=BOTH)
#
# f = Figure(figsize=(5, 4), dpi=100)
# a = f.add_subplot(111)
# t = arange(0.0, 3.0, 0.01)
# s = sin(2 * pi * t)
# a.plot(t, s)
# a.set_title('Tk embedding')
# a.set_xlabel('X axis label')
# a.set_ylabel('Y label')
#
# canvas = FigureCanvasTkAgg(f, master=tab3)
#
# canvas.show()
# canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# button = Button(master=image_frame, text='Quit', command=sys.exit)
# button.pack(side=BOTTOM)

tab_frame = Frame(root)
tab_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

image = PIL.Image.open("lenna.png")
X = np.asarray(image)
photo = PIL.ImageTk.PhotoImage(image)
original_image = Label(image_frame, image=photo)
original_image.image = photo
original_image.pack()


def save_image():
    global image
    file_path = "img_"+strftime("%Y-%m-%dT%H:%M:%S", gmtime())#filedialog.asksaveasfilename(defaultextension=".jpg")
    if not file_path:
        return
    image.save(file_path, "JPEG")
    load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path))


def load_image(file_path=None):
    if file_path is None:
        file_path = filedialog.askopenfilename()
    if not file_path:
        return
    global image
    global photo
    global X
    image = PIL.Image.open(file_path)
    X = np.asarray(image)
    photo = PIL.ImageTk.PhotoImage(image)
    original_image.config(image=photo)
    original_image.image = photo

Button(image_frame, text="Load image...", command=load_image).pack()
Button(image_frame, text="Save image", command=save_image).pack()

bar = TabBar(tab_frame, "Kontrast")


def update_image(fun, x):
    global X
    global original_image
    global image
    global photo
    im = fun(x, X)
    image = PIL.Image.fromarray(np.uint8(im))
    photo = PIL.ImageTk.PhotoImage(image)
    original_image.config(image=photo)
    original_image.image = photo


tab1 = HistTab(tab_frame, "Kontrast", update_image)

tab2 = GammaTab(tab_frame, "Jasność", update_image)

tab3 = MorphTab(tab_frame, "Filtry", update_image)

bar.add(tab1)
bar.add(tab2)
bar.add(tab3)

bar.show()

mainloop()
