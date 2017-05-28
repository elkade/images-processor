from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import filedialog
import numpy as np
import PIL.Image
import PIL.ImageTk
import matplotlib
from skimage.exposure import adjust_gamma
from skimage import data
from GammaTab import GammaTab
from HistTab import HistTab
from tabs import *

matplotlib.use('TkAgg')
root = Tk()
root.wm_title("Łukasz Dragan - Podstawy przetwarzania obrazow")

image_frame = Frame(root)
image_frame.pack(padx=5, pady=10, anchor=NW, side=LEFT)

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
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if not file_path:
        return
    image.save(file_path, "JPEG")


def load_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = PIL.Image.open(file_path)
    pht = PIL.ImageTk.PhotoImage(img)
    original_image.config(image=pht)
    original_image.image = pht


Button(image_frame, text="Load image...", command=load_image).pack()
Button(image_frame, text="Save image...", command=save_image).pack()

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

tab3 = Tab(tab_frame, "Filtry")
Label(tab3, bg='white', text="Tab3 text").pack(
    side=LEFT, expand=YES, fill=BOTH)

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2 * pi * t)
a.plot(t, s)
a.set_title('Tk embedding')
a.set_xlabel('X axis label')
a.set_ylabel('Y label')

canvas = FigureCanvasTkAgg(f, master=tab3)

canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# button = Button(master=image_frame, text='Quit', command=sys.exit)
# button.pack(side=BOTTOM)



bar.add(tab1)
bar.add(tab2)
bar.add(tab3)
# bar.add(tab4)
# bar.config(bd=2, relief=RIDGE)			# add some border
bar.show()

mainloop()
