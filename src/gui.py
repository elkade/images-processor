from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib

matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def destroy(e):
    sys.exit()


root = Tk.Tk()
root.wm_title("Lukasz Dragan - Podstawy przetwarzania obrazow")

image = Image.open("lenna.png")
photo = ImageTk.PhotoImage(image)
original_image = Tk.Label(root, image=photo)
original_image.image = photo
original_image.pack()

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2 * pi * t)


def callback():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    original_image.config(image=photo)
    original_image.image = photo


b = Tk.Button(root, text="OK", command=callback)
b.pack()

a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=root, text='Quit', command=sys.exit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
